# -*- coding: utf-8 -*-
"""
Created on Thu May 14 15:48:22 2020

@author: ACMD-YYB
"""

# from sqlalchemy.inspection import inspect
from flask import request, make_response, jsonify
from flask import current_app as app
from sqlalchemy import *
from .models_angel import db, Angel, AngelInv
from .models import db, AccountInfo
import pandas as pd
import string, random, json
from sqlalchemy import inspect

@app.route('/angel/detail', methods=['POST'])
def angel_detail():
    aSerial = request.get_json(force=True)['aSerial']
    
    res = []
    
    row = Angel.query.filter(Angel.aSerial == aSerial)
    
    df = pd.read_sql(row.statement, row.session.bind)
    res.append(json.loads(df.to_json(orient='records')))
    
    # 휴먼 회사구 (다중 선택)
    row = AngelInv.query.filter(AngelInv.aVSerial == aSerial)
    
    df = pd.read_sql(row.statement, row.session.bind)
    res.append(json.loads(df.to_json(orient='records')))
    
    
    db.session.close()
    
    print ('angel detail :: ', res, flush=True)
    
    return jsonify(res)

@app.route('/angel/list', methods=['POST'])
def angel_list():
    res = []
    
    row = db.session.query(Angel.coNameKor.label('회사명(한글)'),
                           Angel.coNameEng.label('회사명(영문)'),
                           Angel.etc.label('기업소개'),
                           Angel.hopCotype01,
                           Angel.hopCotype02,
                           Angel.hopCoSect01,
                           Angel.hopCoSect02,
                           Angel.aSerial)
    
    df = pd.read_sql(row.statement, row.session.bind)
    res.append(json.loads(df.to_json(orient='records')))
    
    db.session.close()
    
    return jsonify(res)

def angel_updater(angel):
    aSerial = angel['aSerial']
    capital = angel['capital']
    invInfo = angel['invInfo']
    invInfoAddIntention = angel['invInfoAddIntention']
    res = jsonify({'aSerial': aSerial})
    
    try:
        row = Angel.query.filter(Angel.aSerial == func.binary(aSerial)).first()
    
        row.aSerial               = aSerial,
        row.regTel                = angel['regTel'],
        row.regEmailId            = angel['regEmailId'],
        row.regContPwd            = angel['regContPwd'],
        row.coNameKor             = angel['coNameKor'],
        row.coNameEng             = angel['coNameEng'],
        row.representativeNameKor = angel['representativeNameKor'],
        row.representativeNameEng = angel['representativeNameEng'],
        row.coTel                 = angel['coTel'],
        row.foundedDate           = angel['foundedDate'],
        row.coAddr                = angel['coAddr'],
        row.coWeb                 = angel['coWeb'],
        row.coLogo                = angel['coLogo'],
        row.corpDiv               = angel['corpDiv'],
        row.coStatus              = angel['coStatus'],
        row.largeField            = angel['largeField'],
        row.smallField            = angel['smallField'],
        row.capital               = capital,
        row.invTypeL              = angel['invTypeL'],
        row.invTypeS              = angel['invTypeS'],
        row.hopCotype01           = angel['hopCotype01'],
        row.hopCotype02           = angel['hopCotype02'],
        row.hopCoSect01           = angel['hopCoSect01'],
        row.hopCoSect02           = angel['hopCoSect02'],
        row.hopCoItem             = angel['hopCoItem'],
        row.hopCoAddr01           = angel['hopCoAddr01'],
        row.hopCoAddr02           = angel['hopCoAddr02'],
        row.hopInvAmount          = angel['hopInvAmount'],
        row.hopSalesVolume        = angel['hopSalesVolume'],
        row.hopOpProfit           = angel['hopOpProfit'],
        row.etc                   = angel['etc'],
        row.invInfo               = invInfo,
        row.invInfoAddIntention   = invInfoAddIntention
    
        db.session.commit()
        
        AngelInv.query.filter(AngelInv.aVSerial == func.binary(aSerial)).delete(synchronize_session='fetch')
        db.session.expire_all()
        
        if invInfo == '01' and invInfoAddIntention: 
            invArr = angel['invArr']    
                    
            # 기업 투자 정보(이력) - 다중 입력
            for str in invArr:
                new_angelInv = AngelInv(
                        aVSerial            = aSerial,
                        preInvTime          = str['preInvTime'],
                        preInvDate          = str['preInvDate'],
                        preInvStage         = str['preInvStage'],
                        preInvAmount        = str['preInvAmount'],
                        preInvestor         = str['preInvestor']
                    )
                db.session.add(new_angelInv)
                db.session.commit()
                
        db.session.close()
    except Exception as e:
        print ('ANGEL UPDATER EXCEPTION E :: ', e, flush=True)
    
    return res

@app.route('/angel/register', methods=['POST'])
def angel_register():
    angel = request.get_json(force=True)
    res = 'fail'
    
    aSerial = None
    
    if not angel['aSerial']:
        aSerial = aSerial_GEN()
    else:
        return angel_updater(angel)
    
    try:
        capital = angel['capital']
        invInfo = angel['invInfo']
        invInfoAddIntention = angel['invInfoAddIntention']
        
        
        if aSerial :
            # 기업 기본 정보
            new_angel = Angel(
                    aSerial               = aSerial,
                    regTel                = angel['regTel'],
                    regEmailId            = angel['regEmailId'],
                    regContPwd            = angel['regContPwd'],
                    coNameKor             = angel['coNameKor'],
                    coNameEng             = angel['coNameEng'],
                    representativeNameKor = angel['representativeNameKor'],
                    representativeNameEng = angel['representativeNameEng'],
                    coTel                 = angel['coTel'],
                    foundedDate           = angel['foundedDate'],
                    coAddr                = angel['coAddr'],
                    coWeb                 = angel['coWeb'],
                    coLogo                = angel['coLogo'],
                    corpDiv               = angel['corpDiv'],
                    coStatus              = angel['coStatus'],
                    largeField            = angel['largeField'],
                    smallField            = angel['smallField'],
                    capital               = capital,
                    invTypeL              = angel['invTypeL'],
                    invTypeS              = angel['invTypeS'],
                    hopCotype01           = angel['hopCotype01'],
                    hopCotype02           = angel['hopCotype02'],
                    hopCoSect01           = angel['hopCoSect01'],
                    hopCoSect02           = angel['hopCoSect02'],
                    hopCoItem             = angel['hopCoItem'],
                    hopCoAddr01           = angel['hopCoAddr01'],
                    hopCoAddr02           = angel['hopCoAddr02'],
                    hopInvAmount          = angel['hopInvAmount'],
                    hopSalesVolume        = angel['hopSalesVolume'],
                    hopOpProfit           = angel['hopOpProfit'],
                    etc                   = angel['etc'],
                    invInfo               = invInfo,
                    invInfoAddIntention   = invInfoAddIntention
                )
            db.session.add(new_angel)
            
            # add된 테이블 모델의 컬럼을 확인 할 때 사용
            columns = [column.name for column in inspect(Angel).c]
            print('columns :: ', columns, flush=True)

            # print('invInfo :: ', invInfo, flush=True)
            # print('invInfoAddIntention :: ', invInfoAddIntention, flush=True)
            
            # print('Error Check 01 :: ', flush=True)
            
            # 기업 투자 정보(이력)유무 / 정보 등록 의사
            if invInfo == '01' and invInfoAddIntention:
                invArr = angel['invArr']    
                
                # 기업 투자 정보(이력) - 다중 입력
                for str in invArr:
                    new_angelInv = AngelInv(
                            aVSerial            = aSerial,
                            preInvTime          = str['preInvTime'],
                            preInvDate          = str['preInvDate'],
                            preInvStage         = str['preInvStage'],
                            preInvAmount        = str['preInvAmount'],
                            preInvestor         = str['preInvestor']
                        )
                    db.session.add(new_angelInv)
                    
                
            db.session.commit()
            
            # 등록자 계정의 업체정보테이블에 해당 업체의 등록관리번호를 저장
            row = AccountInfo.query.filter(AccountInfo.emailIdF == func.binary(angel['regEmailId'])).first()
            row.emailIdF     = row.emailIdF
            row.accountType  = row.accountType
            row.accountCo    = aSerial
            row.accountFCo   = row.accountFCo
            row.accountFTech = row.accountFTech
            row.newsRx       = row.newsRx 
            
            db.session.commit()
            db.session.close()
            
            res = jsonify({'aSerial': aSerial})
            
        return res
    
    except Exception as e:
        print ('Exception :: ',e , flush=True)
        res = '500'
    
    return res

def aSerial_GEN():
    # 15자리 
    _LENGTH = 15 
    
    # 숫자 + 대소문자 
    string_pool = string.ascii_letters + string.digits 
    
    # 랜덤한 문자열 생성 
    serial = '' 
    for i in range(_LENGTH): 
        serial += random.choice(string_pool) 
        
    _serial = Angel.query.filter(Angel.aSerial == func.binary(serial)).first()
    
    if _serial :
        aSerial_GEN()
    else :
        return serial  