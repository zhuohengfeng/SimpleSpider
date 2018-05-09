#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/9 下午8:41
# @Author  : zhuo_hf@foxmail.com
# @File    : spider_bs4_requests.py

import requests
from bs4 import BeautifulSoup


def main():
    # 需要伪装成浏览器访问
    # 注意除了伪装外，服务器有可能通过ajaxc技术动态获取信息，所以我们单独发送一次请求是不够的。
    # 这个时候可以通过chrame--开发者工具---network--XHR 来看所有的请求
    headers = {
        "User - Agent": "Mozilla / 5.0(Linux;Android6.0;Nexus5Build / MRA58N) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 66.0.3359.139MobileSafari / 537.36",
        "Host": "kstj.baidu.com",
        "Referer": "https: // jingyan.baidu.com / album / a3761b2b8458321576f9aaf8.html?picindex = 1"
    }
    result = requests.get("http://www.baidu.com", headers=headers)
    print(result.content)
    pass


if __name__ == '__main__':
    main()