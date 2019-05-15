#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2019/5/13 9:56 AM 
# @name: wood
# @author：Zhangbohui

from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, VARCHAR, TIMESTAMP
from src.po import VARCHAR2,Base,session

class Order(Base):
    __tablename__ = 'orders'

    ID = Column(Integer, primary_key=True)
    NAME = Column(VARCHAR)
    CUSTOMER_NAME = Column(VARCHAR)
    DETAIL = Column(VARCHAR)
    QTY = Column(VARCHAR)
    CREATE_AT = Column(TIMESTAMP)
    EXCUTE_AT = Column(TIMESTAMP)
    STATUS = Column(VARCHAR)


def get_orders_with_id(id):
    """
    :return:
    """
    msg = """SELECT * FROM orders WHERE CUSTOMER_NAME IN (SELECT NAME FROM tb_user WHERE USER_ID=%s)"""%id
    return session.execute(msg).fetchall()