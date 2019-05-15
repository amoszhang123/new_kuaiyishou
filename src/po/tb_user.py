#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2019/5/13 10:00 AM 
# @name: tb_user
# @author：Zhangbohui

from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, VARCHAR, TIMESTAMP
from src.po import VARCHAR2,Base, session

class TbUser(Base):
    __tablename__ = 'tb_user'

    ID = Column(Integer, primary_key=True)
    NAME = Column(VARCHAR)
    USER_ID = Column(Integer)
    CREATE_AT = Column(TIMESTAMP)

def get_tb_id(id):
    """
    :param id: wechat_openId
    :return: tb_name[dict]
    """
    #获取登录时间为一天内的账号名
    msg = """select NAME,PRIMARY_ID from tb_user WHERE TIMESTAMPDIFF(MINUTE,now(),LOGIN_AT)<1440 AND USER_ID=%s"""%id
    return session.execute(msg).fetchall()

def get_account(id):
    """
    :param id: wechat_openId
    :return: account_list
    """
    msg = """select * from tb_user where USER_ID=%s""" % id
    return session.execute(msg).fetchall()

if __name__ == "__main__":
    print(get_tb_id("1"))