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
from flask_marshmallow import Marshmallow
import pandas as pd
import string, random, json


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

@app.route('/human/detail', methods=['POST'])
def human_detail():
    hSerial = request.get_json(force=True)
    # row = HumanBasic.query.order_by('hSerial').first()
    row = HumanBasic.query.filter(HumanBasic.hSerial == hSerial['hSerial']).first()
    
    res = []
    
    arr = []
    arr.append(row.__dict__)
    
    HumanBasic_schema = HumanBasicSchema(many=True)
    output = HumanBasic_schema.dump(arr).data
    
    res.append(output)
    
    hSerial = row.hSerial
    
    print ('hSerial :: ', hSerial, flush=True)
    
    # row = HumanDiv.query.filter(HumanDiv.hSerial == hSerial).all()
    # HumanDiv_schema = HumanDivSchema(many=True)
    # output = HumanDiv_schema.dump(row).data
    
    # row = db.session.query(HumanDiv).join(HumanHead, HumanDiv.hSerial == HumanHead.hHDSerial).\
    #         filter(HumanDiv.hSerial == hSerial).all()
    
    # row = db.session.query(HumanDiv, HumanHead).filter(HumanDiv.hSerial == HumanHead.hHDSerial).\
    #         filter(HumanDiv.hSerial == hSerial).all()
    
    row = db.session.query(HumanBasic, HumanHead, HumanItem, HumanStatus, HumanInv).join(HumanHead, HumanItem, HumanStatus, HumanInv).\
            filter(HumanBasic.hSerial == hSerial)
    
    # print('row :: ', row, flush=True)
    # for u in row:
    #     print('row dict :: ', u.__dict__, flush=True)
    
    # res.append(output)
    
    db.session.close()
    
    df = pd.read_sql(row.statement, row.session.bind)
    
    return df.to_json(orient='records')

    # return (jsonify(res), 200) if row else ('', 400)
    
    #! res = row.__dict__
    
    # return 'str'
    
    # res = app.response_class(
    #     row.__dict__
    #     )
    
    #! return json.dumps(row.__dict__)
        
@app.route('/human/register', methods=['POST'])
def human_register():
    res = '200'
    
    try:
        human = request.get_json(force=True)
        hSerial = hSerial_GEN()
    
        # print ('human row :: ', new_humanBasic.hSerial, flush=True)
        
        if hSerial :
            # 기업 기본 정보
            new_humanBasic = HumanBasic(
                    hSerial     = hSerial,
                    regEMailID  = human['regEMailID'],
                    regTel      = human['regTel'],
                    regContPwd  = human['regContPwd'],
                    coNameKor   = human['coNameKor'],
                    coNameEng   = human['coNameEng'],
                    foundedDate = human['foundedDate'],
                    corpDiv     = human['corpDiv']['value'],
                    coStatus    = human['coStatus']['value'],
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
                        coDiv    = str['value']
                    )
                db.session.add(new_humanDiv)
                
            # 기업 대표자 정보
            new_humanHead = HumanHead(
                    hHDSerial                 = hSerial,
                    representativeNameKor     = human['representativeNameKor'],
                    representativeNameEng     = human['representativeNameEng'],
                    representativeTel         = human['representativeTel'],
                    representativeNationality = human['representativeNationality'],
                    representativeGender      = human['representativeGender']['value'],
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
                    tech           = human['tech']['value'],
                    largeField     = human['largeField']['value'],
                    smallField     = human['smallField'],
                    o2o            = human['o2o']['value'],
                    businessType   = human['businessType']['value'],
                    serviceType    = human['serviceType']['value'],
                    serviceStatus  = human['serviceStatus']['value'],
                    serviceURL     = human['serviceURL'],
                    similarService = human['similarService'],
                    serviceLogo    = human['serviceLogo']
                )
            
            db.session.add(new_humanItem)
            
            capital             = human['capital'].replace(',', ''),
            totalAssets         = human['totalAssets'].replace(',', ''),
            totalLiabilities    = human['totalLiabilities'].replace(',', ''),
            
            # 기업 상태 정보
            new_humanStatus = HumanStatus(
                    hSTSerial           = hSerial,
                    invStage            = human['invStage']['value'],
                    prevYearSaleVolume  = human['prevYearSaleVolume']['value'],
                    invAttrTargetAmount = human['invAttrTargetAmount'],
                    problemsToSolve     = human['problemsToSolve'],
                    ourSolution         = human['ourSolution'],
                    aboutTeam           = human['aboutTeam'],
                    capital             = capital,
                    totalAssets         = totalAssets,
                    totalLiabilities    = totalLiabilities,
                    numberOfEmp         = human['numberOfEmp']
                )
            
            db.session.add(new_humanStatus)
            
            invFundPurpose = human['invFundPurpose']
            
            # 투자금 사용 목적 - 다중 선택
            for str in invFundPurpose:
                new_humanInvPps = HumanInvPps(
                        hVPSerial  = hSerial,
                        invFundPurpose    = str['value']
                    )
                db.session.add(new_humanInvPps)
                
            invArr = human['invArr']    
                
            # 기업 투자 정보(이력) - 다중 입력
            for str in invArr:
                new_humanInv = HumanInv(
                        hVSerial            = hSerial,
                        preInvTime          = str['preInvTime'],
                        preInvDate          = str['preInvDate'],
                        preInvStage         = str['preInvStage']['value'],
                        preInvAmount        = str['preInvAmount'],
                        preInvestor         = str['preInvestor'],
                        invInfo             = human['invInfo']['value'],
                        invInfoAddIntention = human['invInfoAddIntention']
                    )
                db.session.add(new_humanInv)
            
            db.session.commit()
            db.session.close()
        
        res = '200'
        return res
    except Exception as e:
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
    print ('_serial :: ', _serial, flush=True)
    
    if _serial :
        hSerial_GEN()
    else :
        return serial    
    
    
