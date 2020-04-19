#!/usr/bin/env python
# -*- coding:utf-8 -*-
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

from jd_assistant import Assistant

if __name__ == '__main__':
    """
    重要提示：此处为示例代码之一，请移步下面的链接查看使用教程👇
    https://github.com/tychxn/jd-assistant/wiki/1.-%E4%BA%AC%E4%B8%9C%E6%8A%A2%E8%B4%AD%E5%8A%A9%E6%89%8B%E7%94%A8%E6%B3%95
    """


    asst = Assistant()      # 初始化
    asst.login_by_QRcode()  # 扫码登陆
    asst.buy_item_in_stock(sku_ids='5921142,1306182,2582352,65959086672,65708238590',area='1_2800_55823',stock_interval=60)# 根据商品是否有货自动下单
# asst.buy_item_in_stock(sku_ids='100006836850',area='1_2800_55823',stock_interval=60)# 根据商品是否有货自动下单
