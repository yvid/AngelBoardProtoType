# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 17:26:43 2020

@author: ACMD-YYB
"""


from flask import request, make_response, jsonify, Response
from datetime import datetime as dt, timedelta as td
from flask import current_app as app
from .models import db, Account, AccountInfo, Payment
from .models_human import db, HumanBasic
from flask_marshmallow import Marshmallow
from sqlalchemy import func, exists
import pandas as pd
import string, random, json, requests, time

ma = Marshmallow(app)

"""
DB데이터 가공 예시
class AccountSchema(ma.ModelSchema):
    class Meta:
        model = Account
        
@app.route('/account/myPage_old', methods=['GET', 'POST'])
def select():
    account = request.get_json(force=True)
    emailId = account['emailId']
    row = Account.query.filter(emailId == emailId)
    print('account row :: ', row, flush=True)
    res = []
    
    for u in row:
        # print('row dict :: ', u.__dict__, flush=True)
        res.append(u.__dict__)
        
    print('res dict :: ', res, flush=True)
    
    account_schema = AccountSchema(many=True)
    output = account_schema.dump(row).data
    
    db.session.close()
    
    return (jsonify({'account': output}), 200) if row else ('', 400)        

print('This is error output', file=sys.stderr)
print('This is standard output', file=sys.stdout)
"""

@app.route('/account/login', methods=['POST'])
def login_user():
    account = request.get_json(force=True)
    emailId = account['emailId']
    emailPsw = account['emailPsw']
    
    row = db.session.query(Account, Payment).join(Payment).\
    filter(Account.emailId == func.binary(emailId)).order_by(Payment.expDate.desc()).limit(1)
    
    df = pd.read_sql(row.statement, row.session.bind)
    res = json.loads(df.to_json(orient='records'))
    
    response = {'res':'e0'}
    
    if not res:
        row = db.session.query(Account).filter(Account.emailId == func.binary(emailId))
        df = pd.read_sql(row.statement, row.session.bind)
        res = json.loads(df.to_json(orient='records'))
    
    if res:
        login_handler(emailPsw, response, res[0])
    
    db.session.close()
    
    return jsonify(response)

def login_handler(emailPsw, response, res):
    print ('login_handler res :: ', res, flush=True)
    if res['emailPsw'] == emailPsw:
        response['res'] = 's1'
        response['account'] = res
    else:
        response['res'] = 'e1'
        
    if 'payProduct' in res:
        edt = res['expDate']
        ldt = time.mktime((dt.now() + td(hours=9)).timetuple()) * 1000
        temp1 = pd.to_datetime(edt, unit='ms')
        temp2 = pd.to_datetime(ldt, unit='ms')
        tempF = temp1 - temp2
        response['payDate'] = res['payDate']
        response['payExp'] = res['expDate']
        response['payRmn'] = str(tempF)
        response['payProduct'] = res['payProduct']
        
    
    return response

@app.route('/account/getCpny', methods=['POST'])
def get_Cpny():
    account = request.get_json(force=True)
    emailId = account['emailId']
    
    row = AccountInfo.query.filter(AccountInfo.emailIdF == func.binary(emailId))
    df = pd.read_sql(row.statement, row.session.bind)
    res = json.loads(df.to_json(orient='records'))
    
    db.session.close()
    
    return (jsonify({'accountInfo': res}), 200) if row else ('', 400)  

@app.route('/account/dup', methods=['POST'])
def dup_user():
    account = request.get_json(force=True)
    emailId = account['emailId']
    
    row = Account.query.filter(Account.emailId == func.binary(emailId)).first()
    res = 'e0'
    
    if row:
        res = 's1'
        
    db.session.close()
            
    return res
@app.route('/account/register', methods=['POST'])
def create_user():
    """Create a user."""
    account = request.get_json(force=True)
    name = account['name']
    emailId = account['emailId']
    
    if name and emailId:
        new_user = Account(
                            emailId    = emailId,
                            emailPsw   = account['emailPsw'],
                            name       = name,
                            nickName   = account['nickName'],
                            belong     = account['belong'],
                            rank       = account['rank'],
                            status     = account['status'],
                            regDate    = dt.now(),
                            latelyDate = dt.now(),
                            regIP      = account['regIP']
                        )
        db.session.add(new_user)  # Adds new User record to database
        
        new_userInfo = AccountInfo(
                            emailIdF     = emailId,
                            accountType  = account['accountType'],
                            accountCo    = account['accountCo'],
                            accountFCo   = account['accountFCo'],
                            accountFTech = account['accountFTech'],
                            newsRx       = account['newsRx']
                        )
        db.session.add(new_userInfo)
        
        db.session.commit()  # Commits all changes
        db.session.close()
        
    return make_response(f"{new_user} successfully created!")

@app.route('/account/updater', methods=['POST'])
def update_user():
    """Update a user."""
    account = request.get_json(force=True)
    name = account['name']
    emailId = account['emailId']
    
    row = Account.query.filter(Account.emailId == func.binary(emailId)).first()
    if name and emailId:
        row.emailId    = emailId,
        row.emailPsw   = account['emailPsw'],
        row.name       = name,
        row.nickName   = account['nickName'],
        row.belong     = account['belong'],
        row.rank       = account['rank'],
        row.status     = account['status'],
        row.modyDate   = dt.now(),
        row.latelyDate = dt.now(),
        row.modyIP     = account['modyIP']
        db.session.commit()  # Commits all changes
        
    row = AccountInfo.query.filter(AccountInfo.emailIdF == func.binary(emailId)).first()
    if name and emailId:
        row.emailIdF     = emailId
        row.accountType  = account['accountType']
        row.accountCo    = account['accountCo']
        row.accountFCo   = account['accountFCo']
        row.accountFTech = account['accountFTech']
        row.newsRx       = account['newsRx']
        
        db.session.commit()  # Commits all changes
        db.session.close()
        
    return make_response(f"{emailId} successfully modified!")

@app.route('/account/myPage', methods=['GET', 'POST'])
def select_user():
    account = request.get_json(force=True)
    emailId = account['emailId']
    
    res = []
    row = db.session.query(Account, AccountInfo).join(AccountInfo).filter(Account.emailId == emailId)
    
    df = pd.read_sql(row.statement, row.session.bind)
    res.append(json.loads(df.to_json(orient='records')))
    
    row = db.session.query(HumanBasic).filter(HumanBasic.regEMailID == emailId)
    
    df = pd.read_sql(row.statement, row.session.bind)
    res.append(json.loads(df.to_json(orient='records')))
    
    db.session.close()
    
    return jsonify(res)
#   return (jsonify(res), 200) if row else ('', 400)
    
@app.route('/account/kakaoPay', methods=['POST'])
def kakaoPay():
    value = request.get_json(force=True)['value']
    
    url = "https://kapi.kakao.com"
    headers = {
        'Authorization': "KakaoAK " + "7be86d726914600794e198ef1399837c",
        'Content-type': 'application/x-www-form-urlencoded;charset=utf-8',
    }
    params = {
        'cid': "TC0ONETIME",
        'partner_order_id': '1001',
        'partner_user_id': 'ACMD',
        'item_name': '포인트',
        'quantity': 1,
        'total_amount': value,
        'vat_amount': 0,
        'tax_free_amount': 0,
        'approval_url': 'http://211.209.243.154:8082/payment/paymentResult',
        'fail_url': 'http://211.209.243.154:8082/',
        'cancel_url': 'http://211.209.243.154:8082/payment/paymentCancel',
    }
    
    response = None
    
    try:
        response = requests.post(url+"/v1/payment/ready", params=params, headers=headers)
        response = json.loads(response.text)
    except Exception as e:
        print ('Exception :: ', e, flush=True)
        
    return jsonify(response)

@app.route('/account/payment', methods=['POST'])
def payment():
    payment = request.get_json(force=True)
    emailId = payment['emailId']
    payDate = dt.now()
    expDate = payDate + td(days=31)
    
    new_payment = Payment(
                            pEmailId   = emailId              ,
                            pay        = payment['pay']       ,
                            payProduct = payment['payProduct'],
                            payDate    = payDate              ,
                            expDate    = expDate              ,
                            payIp      = payment['payIp']     
                        )
    
    db.session.add(new_payment)
    db.session.commit()
    db.session.close()
    
    return 'Payment Data Save Complate 200'

@app.route('/shell', methods=['GET'])
def wellcome():
    str = request.form.to_dict(flat=False)
    return 'Hello Mr.SunShine Taiwan Number One and Do you remember Tiananmen'