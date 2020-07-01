# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 17:26:43 2020

@author: ACMD-YYB
"""

# from sqlalchemy.inspection import inspect
from flask import request, make_response, jsonify
from flask import current_app as app
from sqlalchemy import func
from .models_human import db, HumanBasic, HumanDiv, HumanHead, HumanItem, HumanStatus, HumanInvPps, HumanInv
from .models import db, AccountInfo
from flask_marshmallow import Marshmallow
import pandas as pd
import string, random, json
import traceback


ma = Marshmallow(app)

class HumanBasicSchema(ma.ModelSchema):
    class Meta:
        model = HumanBasic
        
class HumanDivSchema(ma.ModelSchema):
    class Meta:
        model = HumanDiv
        
class HumanHeadchema(ma.ModelSchema):
    class Meta:
        model = HumanHead        

@app.route('/human/list', methods=['POST'])
def human_list():
    res = []
    
    row = db.session.query(HumanBasic, HumanItem).\
            join(HumanItem)
    
    df = pd.read_sql(row.statement, row.session.bind)
    res.append(json.loads(df.to_json(orient='records')))
    
    db.session.close()
    
    return jsonify(res)

@app.route('/human/detail', methods=['POST'])
def human_detail():
    hSerial = request.get_json(force=True)['hSerial']
    
    print ('hSerial :: ', hSerial, flush=True)
    
    res = []
    
    row = db.session.query(HumanBasic, HumanHead, HumanItem, HumanStatus).\
            join(HumanHead, HumanItem, HumanStatus).\
            filter(HumanBasic.hSerial == hSerial)
    
    df = pd.read_sql(row.statement, row.session.bind)
    res.append(json.loads(df.to_json(orient='records')))
    
    # 휴먼 회사구 (다중 선택)
    row = HumanDiv.query.filter(HumanDiv.hSerial == hSerial)
    
    df = pd.read_sql(row.statement, row.session.bind)
    res.append(json.loads(df.to_json(orient='records')))
    
    # 휴먼 투자금 사용 목적 (다중 선택)
    row = HumanInvPps.query.filter(HumanInvPps.hVPSerial == hSerial)
    
    df = pd.read_sql(row.statement, row.session.bind)
    res.append(json.loads(df.to_json(orient='records')))
    
    # 휴먼 투자 실적 (다중 입력)
    row = HumanInv.query.filter(HumanInv.hVSerial == hSerial)
    
    df = pd.read_sql(row.statement, row.session.bind)
    res.append(json.loads(df.to_json(orient='records')))
    
    db.session.close()
    
    return jsonify(res)
        
@app.route('/human/register', methods=['POST'])
def human_register():
    human = request.get_json(force=True)
    res = 'fail'
    
    hSerial = hSerial_GEN()
    
    print ('human register check01, human :: ', human, flush=True)
    
    try:
        regEMailID  = human['regEMailID']
        invInfo = human['invInfo']
        invInfoAddIntention = human['invInfoAddIntention']
    
        if hSerial :
            # 기업 기본 정보
            new_humanBasic = HumanBasic(
                    hSerial     = hSerial,
                    regEMailID  = regEMailID,
                    regTel      = human['regTel'],
                    regContPwd  = human['regContPwd'],
                    coNameKor   = human['coNameKor'],
                    coNameEng   = human['coNameEng'],
                    foundedDate = human['foundedDate'],
                    corpDiv     = human['corpDiv'],
                    coStatus    = human['coStatus'],
                    coAddr      = human['coAddr'],
                    coEmail     = human['coEmail'],
                    coWeb       = human['coWeb'],
                    coLogo      = human['coLogo'],
                    coTel       = human['coTel']
                )
            
            db.session.add(new_humanBasic)
            db.session.commit()
            
            
            coDiv = human['coDiv']
            
            # 회사 구분 - 다중 선택
            for str in coDiv:
                new_humanDiv = HumanDiv(
                        hSerial  = hSerial,
                        coDiv    = str
                    )
                db.session.add(new_humanDiv)
                
            
            # 기업 대표자 정보
            new_humanHead = HumanHead(
                    hHDSerial                 = hSerial,
                    representativeNameKor     = human['representativeNameKor'],
                    representativeNameEng     = human['representativeNameEng'],
                    representativeTel         = human['representativeTel'],
                    representativeNationality = human['representativeNationality'],
                    representativeGender      = human['representativeGender'],
                    representativeFounderSame = human['representativeFounderSame']['value'],
                    founderNameKor            = human['founderNameKor'],
                    coRepresentative          = human['coRepresentative']['value'],
                    coRepresentativeNameKor   = human['coRepresentativeNameKor']
                )
            db.session.add(new_humanHead)
            
            # 기업 아이템 정보
            new_humanItem = HumanItem(
                    hITMSerial     = hSerial,
                    serviceNameKor = human['serviceNameKor'],
                    serviceNameEng = human['serviceNameEng'],
                    serviceSummary = human['serviceSummary'],
                    patent         = human['patent'],
                    tech           = human['tech'],
                    largeField     = human['largeField'],
                    smallField     = human['smallField'],
                    o2o            = human['o2o'],
                    businessType   = human['businessType'],
                    serviceType    = human['serviceType'],
                    serviceStatus  = human['serviceStatus'],
                    serviceURL     = human['serviceURL'],
                    similarService = human['similarService'],
                    serviceLogo    = human['serviceLogo']
                )
            db.session.add(new_humanItem)
            
            capital             = human['capital'].replace(',', '')
            totalAssets         = human['totalAssets'].replace(',', '')
            totalLiabilities    = human['totalLiabilities'].replace(',', '')
            
            print ('capital :: ', capital, flush=True)
            print ('totalAssets :: ', totalAssets, flush=True)
            print ('totalLiabilities :: ', totalLiabilities, flush=True)
            
            # 기업 상태 정보
            new_humanStatus = HumanStatus(
                    hSTSerial           = hSerial,
                    invStage            = human['invStage'],
                    prevYearSaleVolume  = human['prevYearSaleVolume'],
                    invAttrTargetAmount = human['invAttrTargetAmount'],
                    problemsToSolve     = human['problemsToSolve'],
                    ourSolution         = human['ourSolution'],
                    aboutTeam           = human['aboutTeam'],
                    capital             = capital,
                    totalAssets         = totalAssets,
                    totalLiabilities    = totalLiabilities,
                    numberOfEmp         = human['numberOfEmp'],
                    invInfo             = invInfo,
                    invInfoAddIntention = invInfoAddIntention  
                )
            db.session.add(new_humanStatus)           
            invFundPurpose = human['invFundPurpose']
            
            # 투자금 사용 목적 - 다중 선택
            for str in invFundPurpose:
                new_humanInvPps = HumanInvPps(
                        hVPSerial  = hSerial,
                        invFundPurpose    = str
                    )
                db.session.add(new_humanInvPps)
                
            if invInfo == '01':
                # 기업 투자 정보(이력)유무 / 정보 등록 의사
                invArr = human['invArr']    
                
                # 기업 투자 정보(이력) - 다중 입력
                for str in invArr:
                    new_humanInv = HumanInv(
                            hVSerial            = hSerial,
                            preInvTime          = str['preInvTime'],
                            preInvDate          = str['preInvDate'],
                            preInvStage         = str['preInvStage'],
                            preInvAmount        = str['preInvAmount'],
                            preInvestor         = str['preInvestor']
                            
                        )
                    db.session.add(new_humanInv)
                    
            db.session.commit()
            
            row = AccountInfo.query.filter(AccountInfo.emailIdF == func.binary(regEMailID)).first()
            row.emailIdF     = row.emailIdF
            row.accountType  = row.accountType
            row.accountCo    = hSerial
            row.accountFCo   = row.accountFCo
            row.accountFTech = row.accountFTech
            row.newsRx       = row.newsRx 
            
            db.session.commit()
            db.session.close()
        
        res = '200'
        return res
    except Exception as e:
        print ('Exception :: ',e , flush=True)
        res = '500'
        return res
    
    return res

def hSerial_GEN():
    # 15자리 
    _LENGTH = 15 
    
    # 숫자 + 대소문자 
    string_pool = string.ascii_letters + string.digits 
    
    # 랜덤한 문자열 생성 
    serial = '' 
    for i in range(_LENGTH): 
        serial += random.choice(string_pool) 
        
    _serial = HumanBasic.query.filter(HumanBasic.hSerial == func.binary(serial)).first()
    
    if _serial :
        hSerial_GEN()
    else :
        return serial    
    
    
