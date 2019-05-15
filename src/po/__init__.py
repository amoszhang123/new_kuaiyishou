#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2019/5/8 4:29 PM 
# @name: __init__.py
# @author：Zhangbohui

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import String
from sqlalchemy import update

Base = declarative_base()

class VARCHAR2(String):
    pass

engine = create_engine('mysql+pymysql://root:root@94.191.13.226:3306/kuaiyipai')
Session = sessionmaker(bind=engine)
session = Session()

