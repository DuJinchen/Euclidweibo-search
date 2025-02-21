# -*- coding: utf-8 -*-
# @Time    : 2023/3/21 21:35
# @Author  : Euclid-Jie
# @File    : Utils.py
import json
import time

import requests
from bs4 import BeautifulSoup


def Get_json_data(URL, header, max_try_times=100):
    try_times = 0
    data_json = None
    while try_times < max_try_times:
        data_json = Get_json_data_sub(URL, header)
        if data_json:
            break
        else:
            time.sleep(1)
            try_times += 1
    if data_json:
        return data_json
    else:
        raise TimeoutError("重试{}后仍无效".format(max_try_times))


def Get_json_data_sub(URL, header):
    response = requests.get(URL, headers=header, timeout=5)  # 使用request获取网页
    if response.status_code == 200:
        html = response.content.decode('utf-8', 'ignore')  # 将网页源码转换格式为html
        data_json = json.loads(html)
        return data_json
    else:
        return None

def Get_soup_data(URl, header):
    response = requests.get(URl, headers=header, timeout=60)  # 使用request获取网页
    html = response.content.decode('utf-8', 'ignore')  # 将网页源码转换格式为html
    soup = BeautifulSoup(html, 'lxml')
    return soup


def remove_upPrintable_chars(s):
    """移除所有不可见字符"""
    return ''.join(x for x in s if x.isprintable())
