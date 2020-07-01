# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 17:21:42 2020

@author: ACMD-YYB
"""


from os import environ

mysql_config = {
	'host': environ.get('MYSQL_HOST', '115.71.232.20'),
	'user': environ.get('MYSQL_USER', 'yb'),
	'pass': environ.get('MYSQL_PASS', 'Qwer!2345'),
	'db':   environ.get('MYSQL_DB', 'yb'),
}

def alchemy_uri():
	return 'mysql://%s:%s@%s/%s?charset=utf8' % (
		mysql_config['user'], mysql_config['pass'], mysql_config['host'], mysql_config['db']
	)

class Config:
    """Set Flask configuration vars from .env file.
    
    # General
    TESTING = environ.get('TESTING')
    FLASK_DEBUG = environ.get('FLASK_DEBUG')
    SECRET_KEY = environ.get('SECRET_KEY')
    
    # Database
    SQLALCHEMY_DATABASE_URI = environ.get('mysql://yb:Qwer!2345@115.71.232.20:3306/yb')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    """