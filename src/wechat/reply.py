#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2019/5/8 5:20 PM 
# @name: reply
# @author：Zhangbohui

from src.user.users import *
from src.woods.woods import *
from src.tb_users.tb_user import *
from src.po.order import *



def reply_msg(open_id, msg):
    #查看
    if len(msg) == 1:
        if msg == "0":
            login_msg = check_user_login(open_id)
            if login_msg is True:
                return "您暂未登录账号，请发送1登录"
            else:
                return login_msg
        #登录
        elif msg == "1":
            return login_tb()
        elif msg == "2":
            return "woods"
        elif msg == "3":
            return "woods"
        return "您发送的命令我不明白哦，请您按照说明操作--0:查看账号状态；1：登录淘宝账号；2：查看购物车；"
    if "http" in msg:
        # print(msg)
        return get_wood_info(msg)
        # if check_user_login(open_id):
        #     return "您暂未登录账号，请发送1登录"
        # else:
        #     return get_wood_info(msg)

def get_info(open_id):
    info = get_account(get_wechat_id(open_id))
    # print(info)
    accounts = []

    for msg in info:
        msg_info = {'账户': msg.NAME, '登录时间': msg.LOGIN_AT.strftime("%Y-%m-%d %H:%M:%S")}
        accounts.append(msg_info)
    return accounts

def get_orders(open_id):
    info = get_orders_with_id(get_wechat_id(open_id))
    orders = []

    for msg in info:
        msg_info = {'账户': msg.CUSTOMER_NAME, '品名': msg.NAME, '规格': msg.DETAIL, '数量': msg.QTY,
                    '下单时间': msg.CREATE_AT.strftime("%Y-%m-%d %H:%M:%S"),
                    '购买时间': msg.EXCUTE_AT.strftime("%Y-%m-%d %H:%M:%S"), '状态': msg.STATUS}
        orders.append(msg_info)
    return orders

def do_event(open_id, event):
    if event == "subscribe":
        register(open_id)
        return "欢迎使用快一拍！"
    else:
        return "ok"

if __name__ == "__main__":
    pass
