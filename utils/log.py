#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ ='huliang'
'''帐号管理类 '''
import os
import hashlib
import json
import csv
from typing import Iterable
from .base import path_fixed ,pre_read
import settings as cf

class Log():
    """记录校验记录的类"""
    def __init__(self):
        filename =os.path.join( cf.PROJECT_DIR ,cf.CHECK_SAVE_FILE) 
        flag = path_fixed(filename)
        self.csvf = open(filename,"a+",encoding="utf-8",newline='\n')
        self.writer = csv.writer(self.csvf, delimiter=',')
        #在文件的开头写入列名称
        if not flag or os.path.getsize(filename) < 11:
            self.writer.writerow(["时间","结果判定","序列号","操作员"])

    def make(self, x:Iterable):
        self.writer.writerow(x)
        self.csvf.flush()
        # print("日志正在写入:",x)
    
    def repeat_check(self,x:str) ->(bool,str):
        current = self.csvf.tell()
        self.csvf.seek(0)
        for rows in csv.reader(self.csvf,delimiter=','):
            if self.csvf.tell() > current:
                return True,""
            if row[2] == x:
                return False,"条码重复"
        return True,""

if __name__ == '__main__':
    l =Log()
    l.make("sfsf")
    del l