#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2019/5/15 11:33 AM 
# @name: resolve
# @author：Zhangbohui

import requests
import urllib.parse
import json

def get_info_from_tao(tao):
    """
    :param tao: 淘口令
    :return: 短链,商品名称
    """
    return "https" + tao.split("https")[1].split('点击链接')[0], tao.split("【")[1].split('】')[0]

def url_to_lone(s_url):
    """
    :param s_url: 短链
    :return: 商品H5链接
    """
    http_headers = {'Accept': '*/*', 'Connection': 'keep-alive',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'}
    resp_data = requests.get(s_url, http_headers)
    test = resp_data.text
    spu = test.split("https://a.m.taobao.com/i")[1].split('.htm?')[0]

    url_data = "{\"ft\":\"t\",\"id\":\"%s\",\"itemNumId\":\"%s\",\"exParams\":\"{\\\"ft\\\":\\\"t\\\",\\\"id\\\":\\\"%s\\\"}\",\"detail_v\":\"8.0.0\",\"utdid\":\"1\"}" % (
        spu, spu, spu)
    data = urllib.parse.quote(url_data)
    url = "https://h5api.m.taobao.com/h5/mtop.taobao.detail.getdetail/6.0/?jsv=2.5.1&appKey=12574478&t=1514774430&api=mtop.taobao.detail" + \
          ".getdetail&v=6.0&isSec=0&ecode=0&AntiFlood=true&AntiCreep=true&H5Request=true&ttid=2018@taobao_h5_9.9.9&type=jsonp&dataType=jsonp&callback=&data=" + data
    return url,spu

def get_detail(good_url):
    response = requests.get(good_url).json()
    detail = ""
    try:
        props = response['data']['skuBase']['props']
        new_props = []
        for detail in props:

            values = detail['values']

            new_values = []
            for value in values:
                new_value = {'vid': value['vid'], 'name': value['name']}
                new_values.append(new_value)
            order_detail = {'pid': detail['pid'], 'name': detail['name'], 'values': new_values}
            new_props.append(order_detail)
        skus = response['data']['skuBase']['skus']
        new_detail = {'props':new_props, 'skus':skus}
        return json.dumps(new_detail, ensure_ascii=False)
    except KeyError:
        return detail

if __name__ == "__main__":
    import time
    s = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    print(type(time.localtime(time.time())))
    print(time.localtime(time.time()))