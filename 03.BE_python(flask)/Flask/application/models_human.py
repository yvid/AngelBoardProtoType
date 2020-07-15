# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 19:43:56 2020

@author: ACMD-YYB
"""

from sqlalchemy import ForeignKey
from . import db
# from sqlalchemy.ext.declarative import declarative_base
# Base = declarative_base()

class HumanBasic(db.Model):
    __tablename__ = 'humanBasic'
    hSerial       = db.Column(db.String(15), primary_key=True, unique=True)
    regEMailID    = db.Column(db.String(45), nullable=False, default='')
    regTel        = db.Column(db.String(50), nullable=False, default='')
    regContPwd    = db.Column(db.String(45), nullable=False, default='')
    coNameKor     = db.Column(db.String(45), nullable=False, default='')
    coNameEng     = db.Column(db.String(45), nullable=False, default='')
    foundedDate   = db.Column(db.Date, nullable=False)
    corpDiv       = db.Column(db.String(2), nullable=False, default='')
    coStatus      = db.Column(db.String(2), nullable=False, default='')
    coAddr        = db.Column(db.String(200), nullable=False, default='')
    coEmail       = db.Column(db.String(45), nullable=False, default='')
    coWeb         = db.Column(db.String(45), nullable=True, default='')
    coLogo        = db.Column(db.String(500), nullable=True, default='')
    coTel         = db.Column(db.String(50), nullable=False, default='')
    
    def __init__(
            self,
            hSerial     = None,
            regEMailID  = None,
            regTel      = None,
            regContPwd  = None,
            coNameKor   = None,
            coNameEng   = None,
            foundedDate = None,
            corpDiv     = None,
            coStatus    = None,
            coAddr      = None,
            coEmail     = None,
            coWeb       = None,
            coLogo      = None,
            coTel       = None,
            ):
        self.hSerial     = hSerial    ,
        self.regEMailID  = regEMailID ,
        self.regTel      = regTel     ,
        self.regContPwd  = regContPwd ,
        self.coNameKor   = coNameKor  ,
        self.coNameEng   = coNameEng  ,
        self.foundedDate = foundedDate,
        self.corpDiv     = corpDiv    ,
        self.coStatus    = coStatus   ,
        self.coAddr      = coAddr     ,
        self.coEmail     = coEmail    ,
        self.coWeb       = coWeb      ,
        self.coLogo      = coLogo     ,
        self.coTel       = coTel      ,


class HumanDiv(db.Model):
    __tablename__ = 'humanDiv'
    hSerial       = db.Column(db.String(15), ForeignKey(HumanBasic.hSerial), primary_key=True)
    coDiv         = db.Column(db.String(2), nullable=False, default='', primary_key=True)
    
    def __init__(
            self,
            hSerial  = None,
            coDiv    = None
            ):
        self.hSerial  = hSerial,
        self.coDiv    = coDiv
        
class HumanHead(db.Model):
    __tablename__ = 'humanHead'
    hHDSerial                 = db.Column(db.String(15), ForeignKey(HumanBasic.hSerial), primary_key=True)
    representativeNameKor     = db.Column(db.String(25), nullable=False, default='')
    representativeNameEng     = db.Column(db.String(25), nullable=False, default='')
    representativeTel         = db.Column(db.String(15), nullable=False, default='')
    representativeNationality = db.Column(db.String(2), nullable=False, default='')
    representativeGender      = db.Column(db.String(2), nullable=False, default='')
    representativeFounderSame = db.Column(db.String(2), nullable=False, default='')
    founderNameKor            = db.Column(db.String(25), nullable=False, default='')
    coRepresentative          = db.Column(db.String(2), nullable=False, default='')
    coRepresentativeNameKor   = db.Column(db.String(25), nullable=False, default='')
    
    def __init__ (
            self,
            hHDSerial                 = None,
            representativeNameKor     = None,
            representativeNameEng     = None,
            representativeTel         = None,
            representativeNationality = None,
            representativeGender      = None,
            representativeFounderSame = None,
            founderNameKor            = None,
            coRepresentative          = None,
            coRepresentativeNameKor   = None
            ):
        self.hHDSerial                 = hHDSerial                ,
        self.representativeNameKor     = representativeNameKor    ,
        self.representativeNameEng     = representativeNameEng    ,
        self.representativeTel         = representativeTel        ,
        self.representativeNationality = representativeNationality,
        self.representativeGender      = representativeGender     ,
        self.representativeFounderSame = representativeFounderSame,
        self.founderNameKor            = founderNameKor           ,
        self.coRepresentative          = coRepresentative         ,
        self.coRepresentativeNameKor   = coRepresentativeNameKor  
        
class HumanItem(db.Model):
    __tablename__ = 'humanItem'    
    hITMSerial     = db.Column(db.String(15), ForeignKey(HumanBasic.hSerial), primary_key=True)
    serviceNameKor = db.Column(db.String(200), nullable=False, default='')
    serviceNameEng = db.Column(db.String(200), nullable=False, default='')
    serviceSummary = db.Column(db.String(500), nullable=False, default='')
    patent         = db.Column(db.String(500), nullable=False, default='')
    tech           = db.Column(db.String(2), nullable=False, default='')
    largeField     = db.Column(db.String(2), nullable=False, default='')
    smallField     = db.Column(db.String(200), nullable=False, default='')
    o2o            = db.Column(db.String(2), nullable=False, default='')
    businessType   = db.Column(db.String(2), nullable=False, default='')
    serviceType    = db.Column(db.String(2), nullable=False, default='')
    serviceStatus  = db.Column(db.String(2), nullable=False, default='')
    serviceURL     = db.Column(db.String(800), nullable=False, default='')
    similarService = db.Column(db.String(400), nullable=False, default='')
    serviceLogo    = db.Column(db.String(800), nullable=False, default='')
    
    def __init__ (
            self,
            hITMSerial     = None,
            serviceNameKor = None,
            serviceNameEng = None,
            serviceSummary = None,
            patent         = None,
            tech           = None,
            largeField     = None,
            smallField     = None,
            o2o            = None,
            businessType   = None,
            serviceType    = None,
            serviceStatus  = None,
            serviceURL     = None,
            similarService = None,
            serviceLogo    = None
            ):
        self.hITMSerial     = hITMSerial    ,
        self.serviceNameKor = serviceNameKor,
        self.serviceNameEng = serviceNameEng,
        self.serviceSummary = serviceSummary,
        self.patent         = patent        ,
        self.tech           = tech          ,
        self.largeField     = largeField    ,
        self.smallField     = smallField    ,
        self.o2o            = o2o           ,
        self.businessType   = businessType  ,
        self.serviceType    = serviceType   ,
        self.serviceStatus  = serviceStatus ,
        self.serviceURL     = serviceURL    ,
        self.similarService = similarService,
        self.serviceLogo    = serviceLogo   
    
class HumanStatus(db.Model):
    __tablename__ = 'humanStatus'
    hSTSerial           = db.Column(db.String(15), ForeignKey(HumanBasic.hSerial), primary_key=True)
    invStage            = db.Column(db.String(2), nullable=False, default='')
    prevYearSaleVolume  = db.Column(db.String(2), nullable=False, default='')
    invAttrTargetAmount = db.Column(db.Integer, nullable=False, default='')
    problemsToSolve     = db.Column(db.String(600), nullable=False, default='')
    ourSolution         = db.Column(db.String(600), nullable=False, default='')
    aboutTeam           = db.Column(db.String(600), nullable=False, default='')
    capital             = db.Column(db.String(400), nullable=False, default='')
    totalAssets         = db.Column(db.String(400), nullable=False, default='')
    totalLiabilities    = db.Column(db.String(400), nullable=False, default='')
    numberOfEmp         = db.Column(db.Integer, nullable=False, default='')
    invInfo             = db.Column(db.String(2), nullable=False, default='')
    invInfoAddIntention = db.Column(db.Boolean, nullable=False, default=False)
    
    def __init__ (
            self,
            hSTSerial           = None,
            invStage            = None,
            prevYearSaleVolume  = None,
            invAttrTargetAmount = None,
            problemsToSolve     = None,
            ourSolution         = None,
            aboutTeam           = None,
            capital             = None,
            totalAssets         = None,
            totalLiabilities    = None,
            numberOfEmp         = None,
            invInfo             = None,
            invInfoAddIntention = None
            ):
        self.hSTSerial           = hSTSerial          ,
        self.invStage            = invStage           ,
        self.prevYearSaleVolume  = prevYearSaleVolume ,
        self.invAttrTargetAmount = invAttrTargetAmount,
        self.problemsToSolve     = problemsToSolve    ,
        self.ourSolution         = ourSolution        ,
        self.aboutTeam           = aboutTeam          ,
        self.capital             = capital            ,
        self.totalAssets         = totalAssets        ,
        self.totalLiabilities    = totalLiabilities   ,
        self.numberOfEmp         = numberOfEmp        ,
        self.invInfo             = invInfo            ,
        self.invInfoAddIntention = invInfoAddIntention 
    
class HumanInvPps(db.Model):
    __tablename__ = 'humanInvPps'
    hVPSerial       = db.Column(db.String(15), ForeignKey(HumanBasic.hSerial), primary_key=True)
    invFundPurpose  = db.Column(db.String(2), nullable=False, default='', primary_key=True)
    
    def __init__(
            self,
            hVPSerial      = None,
            invFundPurpose = None
            ):
        self.hVPSerial      = hVPSerial,
        self.invFundPurpose = invFundPurpose    
    
class HumanInv(db.Model):
    __tablename__ = 'humanInv'
    hVSerial            = db.Column(db.String(15), ForeignKey(HumanBasic.hSerial), primary_key=True)
    preInvTime          = db.Column(db.Integer, nullable=False, default='', primary_key=True)
    preInvDate          = db.Column(db.Date, nullable=True)
    preInvStage         = db.Column(db.String(2), nullable=True, default='')
    preInvAmount        = db.Column(db.Integer, nullable=True, default='')
    preInvestor         = db.Column(db.String(400), nullable=True, default='')
    
    def __init__ (
            self,
            hVSerial            = None,
            preInvTime          = None,
            preInvDate          = None,
            preInvStage         = None,
            preInvAmount        = None,
            preInvestor         = None
            ):
       self.hVSerial            = hVSerial           ,
       self.preInvTime          = preInvTime         ,
       self.preInvDate          = preInvDate         ,
       self.preInvStage         = preInvStage        ,
       self.preInvAmount        = preInvAmount       ,
       self.preInvestor         = preInvestor                
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        