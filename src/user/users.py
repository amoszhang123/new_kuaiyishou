#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2019/5/9 3:47 PM 
# @name: users
# @author：Zhangbohui
from src.po.user import *
from src.po.tb_user import *

def check_user_login(open_id):
    msg = "您已登录的淘宝账号：\n" \
          "ID:淘宝账户名\n"
    wechat_id = get_wechat_id(open_id)
    if not wechat_id:
        print("asa")
    tb_id = get_tb_id(wechat_id)
    if len(tb_id) > 0:
        for ids in tb_id:
            msg = msg + str(ids.PRIMARY_ID) + " :" + ids.NAME + "\n"
        return msg
    else:
        return True

def register(open_id):
    add_id(open_id)

if __name__ == "__main__":
    r = get_wechat_id("adwdwd")
    if not r:
        print("meiyouzhuce")
    else:
        print("1")
    # print(r)
