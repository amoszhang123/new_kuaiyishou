#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2019/5/15 3:01 PM 
# @name: wood
# @author：Zhangbohui

from sqlalchemy import Column, Integer, VARCHAR, TIMESTAMP
from src.po import Base,session
import time

class Wood(Base):
    __tablename__ = 'woods'

    ID = Column(Integer, primary_key=True)
    NAME = Column(VARCHAR)
    CREATE_AT = Column(TIMESTAMP)
    DETAIL = Column(VARCHAR)
    COUNT = Column(Integer)
    USER_ID = Column(Integer)
    SPU = Column(VARCHAR)

def add_good(name, detail, spu):
    wood = Wood(NAME=name, DETAIL=detail, SPU=spu, COUNT=1, CREATE_AT=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    try:
        session.add(wood)
        session.commit()
    except Exception as e:
        print(e.args)
        print("新建商品错误")
        session.rollback()
    finally:
        session.close()
