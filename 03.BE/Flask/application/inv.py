# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 14:46:37 2020

@author: ACMD-YYB
"""

from flask import request, make_response, jsonify, Response
from datetime import datetime as dt, timedelta as td
from flask import current_app as app
from .models_inv import db, Inv
from .models_angel import db, Angel
from .models_human import db, HumanBasic as Human
from sqlalchemy import func, exists, text
import pandas as pd
import string, random, json, requests, time


@app.route('/inv/updater', methods=['POST'])
def inv_updater():
    inv = request.get_json(force=True)
    iSerial = inv['iSerial']
    invStep = inv['invStep']
    
    print ('invStep :: ', invStep, flush=True)
    
    row = Inv.query.filter(Inv.iSerial == func.binary(iSerial)).first()
    
    if iSerial and invStep:
        row.invStep  = invStep,
        row.chngDate = dt.now()
        db.session.commit()
    
    row = Inv.query.filter(Inv.iSerial == func.binary(iSerial))
    df = pd.read_sql(row.statement, row.session.bind)
    res = json.loads(df.to_json(orient='records'))   
    
    db.session.close()
    
    return jsonify({'updateRes': res})

@app.route('/inv/getDetail', methods=['POST'])
def inv_getDetail():
    serials = request.get_json(force=True)
    
    aSerial = serials['aSerial']
    hSerial = serials['hSerial']
    
    res = []
    
    row = Angel.query.filter(Angel.aSerial == func.binary(aSerial))
    
    df = pd.read_sql(row.statement, row.session.bind)
    res.append(json.loads(df.to_json(orient='records')))
    
    row = Human.query.filter(Human.hSerial == func.binary(hSerial))
    
    df = pd.read_sql(row.statement, row.session.bind)
    res.append(json.loads(df.to_json(orient='records')))
    
    db.session.close()
    
    return jsonify(res)
    
@app.route('/inv/list', methods=['POST'])
def inv_list():
    accountInfo = request.get_json(force=True)
    chkUser = accountInfo['emailIdF']
    
    aco = accountInfo['accountCo']
    mode = '='
    
    if chkUser == 'admin':
        aco = '%'
        mode = 'LIKE '
        
    sql = text(
                'SELECT *, humanBasic.coNameKor AS hCoName FROM humanBasic JOIN \
                    (SELECT *, angel.coNameKor AS aCoName FROM angel \
                     JOIN (SELECT * FROM yb.investment \
                     WHERE yb.investment.invASerial {} \'{}\' || yb.investment.invHSerial {} \'{}\') as inv \
                         WHERE angel.aSerial = inv.invASerial) as invAngel\
                        WHERE humanBasic.hSerial = invAngel.invHSerial'.format(mode, aco, mode, aco)
                )
                        
    row = db.engine.execute(sql)
    
    db.session.close()
    
    return json.dumps({'invList':[dict(r) for r in row]}, indent=4, sort_keys=True, default=str)
    

@app.route('/inv/register', methods=['POST'])
def inv_register():
    iSerial = iSerial_GEN()
    inv = request.get_json(force=True)
    invASerial = inv['invAserial']
    invHSerial = inv['invHserial']
    
    row = Inv.query.filter(Inv.invASerial == func.binary(invASerial)).\
                    filter(Inv.invHSerial == func.binary(invHSerial)).first()
        
    if row:
        return ('Registration aleady exist', 200)
    
    if iSerial :
        new_inv = Inv(
            iSerial    = iSerial,
            invASerial = invASerial,
            invHSerial = invHSerial,
            invType    = inv['invType'],
            reqDate    = dt.now(),
            invStep    = 'a00',
            chngDate   = dt.now(),
            )
        
        db.session.add(new_inv)
        
        db.session.commit()  # Commits all changes
        db.session.close()
    
    return ('Registration completed', 200) if new_inv else ('', 400)

def iSerial_GEN():
    # 15자리 
    _LENGTH = 15 
    
    # 숫자 + 대소문자 
    string_pool = string.ascii_letters + string.digits 
    
    # 랜덤한 문자열 생성 
    serial = '' 
    for i in range(_LENGTH): 
        serial += random.choice(string_pool) 
        
    _serial = Inv.query.filter(Inv.iSerial == func.binary(serial)).first()
    
    if _serial :
        iSerial_GEN()
    else :
        return serial    
    