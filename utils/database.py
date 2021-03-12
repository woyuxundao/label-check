#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ ='huliang'
'''数据库模块，用于日志存储 '''
import os
from  os.path import abspath ,dirname
import sqlite3
from typing import Iterable

DIRNAME = dirname(abspath(__file__))
F_DIRNAME = dirname(DIRNAME)

class DB_Manage:
    CUSTOMER= {}

    def __init__(self):
        '''数据库初始化工作，未发现文件则创建数据库'''
        pass

    def db_init(self,custom:str):
        '''检查数据库是否存在，否则创建进行初始化'''
        if custom not in self.CUSTOMER:
            db_name = F_DIRNAME+"/"+custom+".db"
            db = sqlite3.connect(db_name)
        pass

    def create_table(self,custom:str,PN:str):
        """创建表，并初始化"""
        table_name= "tb"+PN
        create_sql=f'create table {table_name} values(,,);'
        self.CUSTOMER[custom].execute(create_sql)
        self.CUSTOMER[custom].commit()
        pass
    
    def insert(self,row:Iterable):
        """把记录写入对应的表中"""
        pass

    def select(self,col:str) ->bool:
        """查询记录，如果存在则返回False"""
        select_sql = f"select * from {table_name} where xx = {col}"
        self.CUSTOMER[custom].execute(create_sql)
        self.CUSTOMER[custom].commit()        
        pass

