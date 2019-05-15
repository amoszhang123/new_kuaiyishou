#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2019/5/10 5:54 PM 
# @name: user
# @author：Zhangbohui

from sqlalchemy import Column, Integer, VARCHAR, TIMESTAMP
from sqlalchemy.orm.exc import NoResultFound
from src.po import Base, session
import time


class User(Base):
    __tablename__ = 'user'

    ID = Column(Integer, primary_key=True)
    OPEN_ID = Column(VARCHAR)
    CREATE_AT = Column(TIMESTAMP)


def get_wechat_id(open_id):
    try:
        return session.query(User.ID).filter(User.OPEN_ID==open_id).one().ID
    except NoResultFound:
        return False
    finally:
        session.close()

def add_id(open_id):
    user = User(OPEN_ID=open_id, CREATE_AT=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    try:
        session.add(user)
        session.commit()
    except Exception as e:
        print(e.args)
        print("注册失败")
        session.rollback()
    finally:
        session.close()
# def get_info(open_id):





if __name__ == "__main__":
    tt = "Herschel Supply Little America 春夏新色双肩包男背包书包潮牌】https://m.tb.cn/h.eXvxpyN?sm=683046 点击链接，再选择浏览器咑閞；或復·制这段描述￥VPIxYcah41A￥后到👉淘♂寳♀👈"
    url = "https" + tt.split("https")[1].split('点击链接')[0]
    print(url)