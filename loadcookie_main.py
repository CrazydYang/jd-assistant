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
    asst.login_by_QRcode()  # 扫码登陆
#     asst._check_cookies() #检查cookie目录的cookie是否生效
    job_defaults = { 'max_instances': 3 }
    scheduler = BlockingScheduler(job_defaults=job_defaults)
    scheduler.add_job(asst.make_reserve,'cron',hour='19',minute='24',second='0', args=['100012043978'])
    scheduler.start()
