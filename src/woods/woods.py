#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @date: 2019/5/9 3:50 PM 
# @name: woods
# @author：Zhangbohui
from src.resolve import *
from src.po.wood import *


def get_wood_info(msg):
    l_url, good_name = get_info_from_tao(msg)
    url,spu = url_to_lone(l_url)
    detail = get_detail(url)
    add_good(detail=detail, spu=spu, name=good_name)
    order_url = "http://94.191.13.226/wood?spu=%s"%spu
    return order_url
