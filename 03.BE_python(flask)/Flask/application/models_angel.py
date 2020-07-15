# -*- coding: utf-8 -*-
"""
Created on Thu May 14 15:49:00 2020

@author: ACMD-YYB
"""


from sqlalchemy import *
from . import db

class Angel(db.Model):
    __tablename__ = 'angel'
    aSerial               = db.Column(db.String(15), primary_key=True, unique=True)
    regTel                = db.Column(db.Integer, nullable=False, default='')
    regEmailId            = db.Column(db.String(50), nullable=False, default='')
    regContPwd            = db.Column(db.String(50), nullable=False, default='')
    coNameKor             = db.Column(db.String(50), nullable=False, default='')
    coNameEng             = db.Column(db.String(50), nullable=False, default='')
    representativeNameKor = db.Column(db.String(25), nullable=False, default='')
    representativeNameEng = db.Column(db.String(25), nullable=False, default='')
    coTel                 = db.Column(db.String(400), nullable=False, default='')
    foundedDate           = db.Column(db.Date, nullable=False)
    coAddr                = db.Column(db.String(200), nullable=False, default='')
    coWeb                 = db.Column(db.String(45), nullable=True, default='')
    coLogo                = db.Column(db.String(500), nullable=True, default='')
    corpDiv               = db.Column(db.String(2), nullable=False, default='')
    coStatus              = db.Column(db.String(2), nullable=False, default='')
    largeField            = db.Column(db.String(2), nullable=False, default='')
    smallField            = db.Column(db.String(400), nullable=False, default='')
    capital               = db.Column(db.Integer, nullable=False, default='')
    invTypeL              = db.Column(db.String(2), nullable=False, default='')
    invTypeS              = db.Column(db.String(2), nullable=False, default='')
    hopCotype01           = db.Column(db.String(2), nullable=False, default='')
    hopCotype02           = db.Column(db.String(2), nullable=False, default='')
    hopCoSect01           = db.Column(db.String(2), nullable=False, default='')
    hopCoSect02           = db.Column(db.String(2), nullable=False, default='')
    hopCoItem             = db.Column(db.String(400), nullable=False, default='')
    hopCoAddr01           = db.Column(db.String(200), nullable=False, default='')
    hopCoAddr02           = db.Column(db.String(200), nullable=False, default='')
    hopInvAmount          = db.Column(db.String(2), nullable=False, default='')
    hopSalesVolume        = db.Column(db.String(2), nullable=False, default='')
    hopOpProfit           = db.Column(db.String(2), nullable=False, default='')
    etc                   = db.Column(db.String(400), nullable=True, default='')
    invInfo               = db.Column(db.String(2), nullable=False, default='')
    invInfoAddIntention   = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(
            self,
            aSerial               = None,
            regTel                = None,
            regEmailId            = None,
            regContPwd            = None,
            coNameKor             = None,
            coNameEng             = None,
            representativeNameKor = None,
            representativeNameEng = None,
            coTel                 = None,
            foundedDate           = None,
            coAddr                = None,
            coWeb                 = None,
            coLogo                = None,
            corpDiv               = None,
            coStatus              = None,
            largeField            = None,
            smallField            = None,
            capital               = None,
            invTypeL              = None,
            invTypeS              = None,
            hopCotype01           = None,
            hopCotype02           = None,
            hopCoSect01           = None,
            hopCoSect02           = None,
            hopCoItem             = None,
            hopCoAddr01           = None,
            hopCoAddr02           = None,
            hopInvAmount          = None,
            hopSalesVolume        = None,
            hopOpProfit           = None,
            etc                   = None,
            invInfo               = None,
            invInfoAddIntention   = None
            ):
        self.aSerial               = aSerial              ,
        self.regTel                = regTel               ,
        self.regEmailId            = regEmailId           ,
        self.regContPwd            = regContPwd           ,
        self.coNameKor             = coNameKor            ,
        self.coNameEng             = coNameEng            ,
        self.representativeNameKor = representativeNameKor,
        self.representativeNameEng = representativeNameEng,
        self.coTel                 = coTel                ,
        self.foundedDate           = foundedDate          ,
        self.coAddr                = coAddr               ,
        self.coWeb                 = coWeb                ,
        self.coLogo                = coLogo               ,
        self.corpDiv               = corpDiv              ,
        self.coStatus              = coStatus             ,
        self.largeField            = largeField           ,
        self.smallField            = smallField           ,
        self.capital               = capital              ,
        self.invTypeL              = invTypeL             ,
        self.invTypeS              = invTypeS             ,
        self.hopCotype01           = hopCotype01          ,
        self.hopCotype02           = hopCotype02          ,
        self.hopCoSect01           = hopCoSect01          ,
        self.hopCoSect02           = hopCoSect02          ,
        self.hopCoItem             = hopCoItem            ,
        self.hopCoAddr01           = hopCoAddr01          ,
        self.hopCoAddr02           = hopCoAddr02          ,
        self.hopInvAmount          = hopInvAmount         ,
        self.hopSalesVolume        = hopSalesVolume       ,
        self.hopOpProfit           = hopOpProfit          ,
        self.etc                   = etc                  ,
        self.invInfo               = invInfo              ,
        self.invInfoAddIntention   = invInfoAddIntention
        
class AngelInv(db.Model):
    __tablename__ = 'angelInv'
    aVSerial            = db.Column(db.String(15), ForeignKey(Angel.aSerial), primary_key=True)
    preInvTime          = db.Column(db.Integer, nullable=False, default='')
    preInvDate          = db.Column(db.Date, nullable=True)
    preInvStage         = db.Column(db.String(2), nullable=True, default='')
    preInvAmount        = db.Column(db.Integer, nullable=True, default='')
    preInvestor         = db.Column(db.String(400), nullable=True, default='')
    
    def __init__ (
            self,
            aVSerial            = None,
            preInvTime          = None,
            preInvDate          = None,
            preInvStage         = None,
            preInvAmount        = None,
            preInvestor         = None,
            ):
       self.aVSerial            = aVSerial           ,
       self.preInvTime          = preInvTime         ,
       self.preInvDate          = preInvDate         ,
       self.preInvStage         = preInvStage        ,
       self.preInvAmount        = preInvAmount       ,
       self.preInvestor         = preInvestor        ,
