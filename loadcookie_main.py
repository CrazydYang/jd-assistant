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

# setSystemTime()

    asst = Assistant()      # 初始化
    asst._check_cookies() #检查cookie目录的cookie是否生效
#     asst.login_by_QRcode()  # 扫码登陆
# #     asst.clear_cart()       # 清空购物车（可选）2020-03-16 20:00:00
#     job_defaults = { 'max_instances': 2 }
#     scheduler = BlockingScheduler(job_defaults=job_defaults)
# #     scheduler.add_job(asst.exec_seckill_by_time, 'date', run_date=datetime.datetime(2020, 3, 18, 21, 8, 30, 900), args=['100011551632,100006394713',50,0.1,1])
#     scheduler.add_job(asst.make_reserve,'date', args=['100012043978'])
#     scheduler.add_job(asst.exec_seckill_by_time, 'cron', hour='9',minute='59',second='58', args=['100012043978',5,0.1,1])
#     scheduler.start()

    
