import os

class Config:
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://Elder_admin:rE6dvA)rb?Ok9(6ROT?@meudatabase.czo26icy2f3k.us-east-2.rds.amazonaws.com:3306/FORMELD_TCC_BANCO_DE_DADOS'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
