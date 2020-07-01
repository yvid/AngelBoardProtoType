# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 14:46:37 2020

@author: ACMD-YYB
"""

from sqlalchemy import ForeignKey
from . import db
from .models_angel import db, Angel
from .models_human import db, HumanBasic as Human

class Inv(db.Model):
    __tablename__ = 'investment'
    iSerial    = db.Column(db.String(15), nullable=False, primary_key=True, unique=True)
    invASerial = db.Column(db.String(15), ForeignKey(Angel.aSerial))
    invHSerial = db.Column(db.String(15), ForeignKey(Human.hSerial))
    invType    = db.Column(db.String(4), nullable=False, default='')
    reqDate    = db.Column(db.DateTime, nullable=False, default='')
    invStep    = db.Column(db.String(5), nullable=False, default='')
    chngDate   = db.Column(db.DateTime, nullable=True, default='')
    
    def __init__(
            self,
            iSerial    = None,
            invASerial = None,
            invHSerial = None,
            invType    = None,
            reqDate    = None,
            invStep    = None,
            chngDate   = None
            ):
        self.iSerial    = iSerial   ,
        self.invASerial = invASerial,
        self.invHSerial = invHSerial,
        self.invType    = invType   ,
        self.reqDate    = reqDate   ,
        self.invStep    = invStep   ,
        self.chngDate   = chngDate  
