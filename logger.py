# -*- coding: utf-8 -*-
'''
Date: 2022-05-02 19:22:19
LastEditors: Zhong.donghong
LastEditTime: 2022-11-02 21:42:07
Description: 输出日志
'''
import re
import time
import logging
import os
from logging import handlers

import time
import logging
import os
from logging import handlers


def _logging(**kwargs):
    level = kwargs.pop('level', None)
    filename = kwargs.pop('filename', None)
    datefmt = kwargs.pop('datefmt', None)
    format = kwargs.pop('format', None)
    if level is None:
        level = logging.DEBUG
    if filename is None:
        filename = 'default.log'
    if datefmt is None:
        datefmt = '%Y-%m-%d %H:%M:%S'
    if format is None:
        format = '%(asctime)s [%(module)s] %(levelname)s [%(lineno)d] %(message)s'
    log = logging.getLogger(filename)
    format_str = logging.Formatter(format, datefmt)
    # backupCount 保存日志的数量，过期自动删除
    backupCount = 4
    # when 按什么日期格式切分(这里方便测试使用的秒)
    th = handlers.TimedRotatingFileHandler(
        filename=filename, when='D', backupCount=backupCount, encoding='utf-8')

    # def namer(filename):
    #     return filename.split('default.')
    # th.namer = namer
    # 设置为S，默认的suffix为 Y-%m-%d_%H-%M-%S
    th.suffix = "%Y-%m-%d.log"
    # th.extMatch = r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}.log$"
    # th.extMatch = re.compile(th.extMatch)
    th.setFormatter(format_str)
    log.addHandler(th)
    log.setLevel(level)
    return log


os.makedirs("./logs", exist_ok=True)
logger = _logging(filename='./logs/default.log')

if __name__ == '__main__':
    logger.debug('Hello World log debug Success')
    logger.info('Hello World log info Success')
    logger.error('Hello World log ERROR Success')
    logger.fatal('Hello World log fatal Success')
    # while True:
    #     time.sleep(0.1)
    #     logger.debug('Hello World log debug Success')
    #     logger.info('Hello World log info Success')
    #     logger.error('Hello World log ERROR Success')
    #     logger.fatal('Hello World log fatal Success')
