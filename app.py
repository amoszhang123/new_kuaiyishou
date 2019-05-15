#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2019/5/8 5:20 PM
# @name: reply
# @author：Zhangbohui
from flask import Flask, jsonify, render_template
from flask import request, Response
import hashlib
from lxml import etree
from src.wechat.reply import *

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/',methods=["GET","POST"])
def app_login():
    if request.method == "GET":
        signature = request.args.get("signature")
        timestamp = request.args.get("timestamp")
        nonce = request.args.get("nonce")
        echostr = request.args.get("echostr")
        # 自己的token
        token = "kuaiyipai1234"  # 这里改写你在微信公众平台里输入的token
        # 字典序排序
        list = [token, timestamp, nonce]
        list.sort()
        sing_str = ''.join(list)
        sha1 = hashlib.sha1()
        sha1.update(sing_str.encode('utf-8'))
        hashcode = sha1.hexdigest()
        print(hashcode)
        # sha1加密算法

        # 如果是来自微信的请求，则回复echostr
        if hashcode == signature:
            return echostr
    else:
        str_xml = request.data  # 获得post来的数据0
        xml = etree.fromstring(str_xml)  # 进行XML解析
        print(str_xml)
        fromUser = xml.find("FromUserName").text
        toUser = xml.find("ToUserName").text
        msgType = xml.find("MsgType").text
        return_msg = ""
        if msgType == "text":
            content = xml.find("Content").text  # 获得用户所输入的内容
            return_msg = reply_msg(fromUser, content)
        elif msgType == "event":
            event = xml.find("Event").text
            return_msg = do_event(fromUser, event)
        return jsonify(render_template("reply_text.xml", toUser=fromUser, fromUser=toUser, createTime=int(time.time()),
                                       content=return_msg))

@app.route('/account', methods=['GET'])
def get_accounts():
    id = request.args.get("ID")
    return Response(json.dumps(get_info(id)), content_type='application/json')

@app.route('/goods', methods=['GET'])
def get_orders_by_id():
    id = request.args.get("ID")
    return Response(json.dumps(get_orders(id)), content_type='application/json')


if __name__ == '__main__':
    app.run(
      host='0.0.0.0',
      port= 80,
      debug=True,
      threaded=True
    )
