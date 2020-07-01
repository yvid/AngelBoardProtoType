# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 17:24:28 2020

@author: ACMD-YYB
"""

from sqlalchemy import ForeignKey
from . import db

class Account(db.Model):
    __tablename__  = 'account'
    emailId        = db.Column(db.String(50), nullable=False, primary_key=True, unique=True)
    emailPsw       = db.Column(db.String(50), nullable=False, default='')
    name           = db.Column(db.String(25), nullable=False, default='')
    nickName       = db.Column(db.String(2), nullable=False, default='')
    belong         = db.Column(db.String(25), nullable=False, default='')
    rank           = db.Column(db.String(2), nullable=False, default='')
    status         = db.Column(db.String(20), nullable=False, default='')
    regDate        = db.Column(db.Date, nullable=False, default='')
    modyDate       = db.Column(db.Date, nullable=True, default='')
    latelyDate     = db.Column(db.Date, nullable=False, default='')
    regIP          = db.Column(db.String(15), nullable=False, default='')
    modyIP         = db.Column(db.String(15), nullable=True, default='')
    

    def __init__(
                self,
                emailId    = None,
                emailPsw   = None,
                name       = None,
                nickName   = None,
                belong     = None,
                rank       = None,
                status     = None,
                regDate    = None,
                modyDate   = None,
                latelyDate = None,
                regIP      = None,
                modyIP     = None  
                ):
            self.emailId   = emailId   ,
            self.emailPsw  = emailPsw  ,
            self.name      = name      ,
            self.nickName  = nickName  ,
            self.belong    = belong    ,
            self.rank      = rank      ,
            self.status    = status    ,
            self.regDate   = regDate   ,
            self.modyDate  = regDate   ,
            self.latelyDate= latelyDate,
            self.regIP     = regIP     ,
            self.modyIP    = modyIP  
            
class AccountInfo(db.Model):
    __tablename__ = 'accountInfo'            
    emailIdF     = db.Column(db.String(50), ForeignKey(Account.emailId), primary_key=True)
    accountType  = db.Column(db.String(2), nullable=False, default='')
    accountCo    = db.Column(db.String(15), nullable=False, default='')
    accountFCo   = db.Column(db.String(2), nullable=False, default='')
    accountFTech = db.Column(db.String(2), nullable=False, default='')
    newsRx       = db.Column(db.Boolean, nullable=False, default=False)
    
    def __init__(
                self,
                emailIdF     = None,
                accountType  = None,
                accountCo    = None,
                accountFCo   = None,
                accountFTech = None,
                newsRx       = None
                ):
            self.emailIdF     = emailIdF    ,
            self.accountType  = accountType ,
            self.accountCo    = accountCo   ,
            self.accountFCo   = accountFCo  ,
            self.accountFTech = accountFTech,
            self.newsRx       = newsRx      
            
class Payment(db.Model):
    __tablename__ = 'payment'            
    pEmailId    = db.Column(db.String(50), ForeignKey(Account.emailId), primary_key=True)
    pay         = db.Column(db.Integer, nullable=False, default='')
    payProduct  = db.Column(db.String(2), nullable=False, default='')
    payDate     = db.Column(db.DateTime, nullable=False, default='', primary_key=True)
    expDate     = db.Column(db.DateTime, nullable=False, default='')
    payIp       = db.Column(db.String(452), nullable=False, default='')
    
    def __init__(
                self,
                pEmailId   = None,
                pay        = None,
                payProduct = None,
                payDate    = None,
                expDate    = None,
                payIp      = None
                ):
            self.pEmailId    = pEmailId  ,
            self.pay         = pay       ,
            self.payProduct  = payProduct,
            self.payDate     = payDate   ,
            self.expDate     = expDate   ,
            self.payIp       = payIp          
            
        
""" 표시하기        
    def __repr__(self):
        return "{emailId='%s',\
                emailPsw='%s',\
                name='%s',\
                nickName='%s',\
                gender='%s',\
                belong='%s',\
                rank='%s',\
                status='%s',\
                regDate='%s',\
                latelyDate='%s',\
                regIP='%s'}"   %(self.emailId,
                                self.emailPsw,
                                self.name,
                                self.nickName,
                                self.gender,
                                self.belong,
                                self.rank,
                                self.status,
                                self.regDate,
                                self.latelyDate,
                                self.regIP
                                )

    
    def __repr__(self):
        return '<Account {}>'.format(self.emailId)
"""    