#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2019/5/13 10:01 AM 
# @name: user_wood
# @author：Zhangbohui

from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, VARCHAR, TIMESTAMP
from src.po import VARCHAR2,Base

class UserWood(Base):
    __tablename__ = 'user_wood'

    ID = Column(Integer, primary_key=True)
    NAME = Column(VARCHAR)
    USER_ID = Column(Integer)
    CREATE_AT = Column(TIMESTAMP)