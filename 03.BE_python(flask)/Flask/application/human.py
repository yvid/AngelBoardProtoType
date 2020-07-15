# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 17:26:43 2020

@author: ACMD-YYB
"""

# from sqlalchemy.inspection import inspect
from flask import request, make_response, jsonify
from flask import current_app as app
from sqlalchemy import func
from sqlalchemy.exc import SQLAlchemyError
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

@app.route('/human/updater', methods=['POST'])
def human_updater(human):
    hSerial = human['hSerial']
    res = jsonify({'hSerial': hSerial})
    
    try:
        regEMailID  = human['regEMailID']
        invInfo = human['invInfo']
        invInfoAddIntention = human['invInfoAddIntention']
        
        row = HumanBasic.query.filter(HumanBasic.hSerial == func.binary(hSerial)).first()
        
        row.hSerial     = hSerial,
        row.regEMailID  = regEMailID,
        row.regTel      = human['regTel'],
        row.regContPwd  = human['regContPwd'],
        row.coNameKor   = human['coNameKor'],
        row.coNameEng   = human['coNameEng'],
        row.foundedDate = human['foundedDate'],
        row.corpDiv     = human['corpDiv'],
        row.coStatus    = human['coStatus'],
        row.coAddr      = human['coAddr'],
        row.coEmail     = human['coEmail'],
        row.coWeb       = human['coWeb'],
        row.coLogo      = human['coLogo'],
        row.coTel       = human['coTel']
        
        db.session.commit()
        
        row = HumanDiv.query.filter(HumanDiv.hSerial == func.binary(hSerial)).delete(synchronize_session='fetch')
        
        coDiv = human['coDiv']
        # 회사 구분 - 다중 선택
        for str in coDiv:
            new_humanDiv = HumanDiv(
                    hSerial  = hSerial,
                    coDiv    = str
                )
            db.session.add(new_humanDiv)
            
        db.session.commit()
                
        row = HumanHead.query.filter(HumanHead.hHDSerial == func.binary(hSerial)).first()
        row.hHDSerial                 = hSerial,
        row.representativeNameKor     = human['representativeNameKor'],
        row.representativeNameEng     = human['representativeNameEng'],
        row.representativeTel         = human['representativeTel'],
        row.representativeNationality = human['representativeNationality'],
        row.representativeGender      = human['representativeGender'],
        row.representativeFounderSame = human['representativeFounderSame']['value'],
        row.founderNameKor            = human['founderNameKor'],
        row.coRepresentative          = human['coRepresentative']['value'],
        row.coRepresentativeNameKor   = human['coRepresentativeNameKor']
        
        db.session.commit()
        
        row = HumanItem.query.filter(HumanItem.hITMSerial == func.binary(hSerial)).first()
        row.hITMSerial     = hSerial,
        row.serviceNameKor = human['serviceNameKor'],
        row.serviceNameEng = human['serviceNameEng'],
        row.serviceSummary = human['serviceSummary'],
        row.patent         = human['patent'],
        row.tech           = human['tech'],
        row.largeField     = human['largeField'],
        row.smallField     = human['smallField'],
        row.o2o            = human['o2o'],
        row.businessType   = human['businessType'],
        row.serviceType    = human['serviceType'],
        row.serviceStatus  = human['serviceStatus'],
        row.serviceURL     = human['serviceURL'],
        row.similarService = human['similarService'],
        row.serviceLogo    = human['serviceLogo']
        
        db.session.commit()
        
        row = HumanStatus.query.filter(HumanStatus.hSTSerial == func.binary(hSerial)).first()
        
        capital             = human['capital']
        totalAssets         = human['totalAssets']
        totalLiabilities    = human['totalLiabilities']
            
        row.hSTSerial           = hSerial,
        row.invStage            = human['invStage'],
        row.prevYearSaleVolume  = human['prevYearSaleVolume'],
        row.invAttrTargetAmount = human['invAttrTargetAmount'],
        row.problemsToSolve     = human['problemsToSolve'],
        row.ourSolution         = human['ourSolution'],
        row.aboutTeam           = human['aboutTeam'],
        row.capital             = capital,
        row.totalAssets         = totalAssets,
        row.totalLiabilities    = totalLiabilities,
        row.numberOfEmp         = human['numberOfEmp'],
        row.invInfo             = invInfo,
        row.invInfoAddIntention = invInfoAddIntention  
                    
        db.session.commit()
        
        row = HumanInvPps.query.filter(HumanInvPps.hVPSerial == func.binary(hSerial)).delete(synchronize_session='fetch')
        invFundPurpose = human['invFundPurpose']
        
        for str in invFundPurpose:
                new_humanInvPps = HumanInvPps(
                        hVPSerial  = hSerial,
                        invFundPurpose    = str
                    )
                db.session.add(new_humanInvPps)
        db.session.commit()
        
        if invInfo == '01':
           row = HumanInv.query.filter(HumanInv.hVSerial == func.binary(hSerial)).delete(synchronize_session='fetch')
           db.session.expire_all()
           
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
            
        db.session.commit()
        db.session.close()
    except Exception as e:
        print ('HUMAN UPDATER EXCEPTION E :: ', e, flush=True)
        
    return res
        
@app.route('/human/register', methods=['POST'])
def human_register():
    human = request.get_json(force=True)
    res = 'fail'
    
    hSerial = None
    
    if not human['hSerial']:
        hSerial = hSerial_GEN()
    else:
        return human_updater(human)
    
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
                
            print ('human register check01 :: ', flush=True)
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
            print ('human register check02 :: ', flush=True)
            
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
            
            print ('human register check03 :: ', flush=True)
            capital             = human['capital']
            totalAssets         = human['totalAssets']
            totalLiabilities    = human['totalLiabilities']
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
        
            res = jsonify({'hSerial': hSerial})
        
        return res
    except Exception as e:
        print ('Exception :: ',e , flush=True)
        res = '500'
        return res
    except (SQLAlchemyError, SQLAlchemyError) as e:
        err = str(e.__dict__['orig'])
        print ('SQLAlchemyError :: ',err , flush=True)
        res = '500'
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
    
    
