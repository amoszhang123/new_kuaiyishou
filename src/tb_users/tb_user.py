#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2019/5/13 2:17 PM 
# @name: tb_user
# @author：Zhangbohui

import requests
import threading
import time

def login_tb():
    data = requests.get(url="http://47.102.37.41:8080/new/qr/gen").json()
    url = data['url']
    print("1111")
    token = data['token']
    new_thread = threading.Thread(target=check_login_state(token))
    # new_thread.setDaemon(True)
    new_thread.start()
    print(url)
    return url


def check_login_state(token):
    tb_id = ""
    while len(tb_id) == 0:
        print("check")
        time.sleep(5)
        params = {
            "token": token
        }
        tb_id = requests.get(url="http://47.102.37.41:8080/new/qr/check",params=params).text
        if len(tb_id) > 0:
            return tb_id



if __name__ == "__main__":
    print(login_tb())