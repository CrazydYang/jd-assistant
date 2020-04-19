#!/usr/bin/env python
# -*- coding:utf-8 -*-
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

from jd_assistant import Assistant
from messenger import Messenger
from config import global_config

if __name__ == '__main__':
    """
    重要提示：此处为示例代码之一，请移步下面的链接查看使用教程👇
    https://github.com/tychxn/jd-assistant/wiki/1.-%E4%BA%AC%E4%B8%9C%E6%8A%A2%E8%B4%AD%E5%8A%A9%E6%89%8B%E7%94%A8%E6%B3%95
    """

#     sku_ids = '100006836850'  # 商品id
#     area = '1_2800_55823'  # 区域id
#     asst = Assistant()  # 初始化
#     asst.login_by_QRcode()  # 扫码登陆
#     .buy_item_in_stock(sku_ids=sku_ids, area=area, wait_all=False, stock_interval=5)  # 根据商品是否有货自动下单
#     # 6个参数：
#     # sku_ids: 商品id。可以设置多个商品，也可以带数量，如：'1234' 或 '1234,5678' 或 '1234:2' 或 '1234:2,5678:3'
#     # area: 地区id
#     # wait_all: 是否等所有商品都有货才一起下单，可选参数，默认False
#     # stock_interval: 查询库存时间间隔，可选参数，默认3秒
#     # submit_retry: 提交订单失败后重试次数，可选参数，默认3次
#     # submit_interval: 提交订单失败后重试时间间隔，可选参数，默认5秒

    asst = Assistant()      # 初始化
    asst.login_by_QRcode()  # 扫码登陆
#     asst.clear_cart()       # 清空购物车（可选）2020-03-16 20:00:00
    job_defaults = { 'max_instances': 3 }
    scheduler = BlockingScheduler(job_defaults=job_defaults)
#     scheduler.add_job(asst.exec_seckill_by_time, 'date', run_date=datetime.datetime(2020, 3, 18, 21, 8, 30, 900), args=['100011551632,100006394713',50,0.1,1])
#     scheduler.add_job(asst.make_reserve,'cron',hour='15',minute='17',second='0', args=['100011551632'])
#     scheduler.add_job(asst.make_reserve,'cron',hour='15',minute='17',second='0', args=['100006394713'])
#     scheduler.add_job(asst.exec_seckill_by_time, 'cron', hour='19',minute='59',second='59', args=['100011551632,100006394713',5,0.1,1])
    #############茅台################
    scheduler.add_job(asst.make_reserve,'cron',hour='10',minute='40',second='0', args=['100012043978'])
    scheduler.add_job(asst.exec_seckill_by_time, 'cron', hour='9',minute='59',second='58', args=['100012043978',5,0.1,1])
    scheduler.start()
 
