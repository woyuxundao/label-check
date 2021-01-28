#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ ='huliang'
'''帐号管理类 '''
import os
import hashlib
import json
from typing import Iterable, Tuple ,List
from .base import path_fixed ,pre_read
import settings as cf

class AccountManager():
    """建立帐号管理的模块"""   
    def __init__(self,*args, **kwargs):
        self.ACCOUNT = {}
        self.filename =os.path.join( cf.PROJECT_DIR ,cf.ACCOUNT_CFG) 
        if path_fixed(self.filename):
            self.ACCOUNT = pre_read(self.filename)

    def add_account(self,arg:Tuple[str]) -> bool:
        #如果添加成功则返回True
        # print("arg",arg)
        account , passwd, department,job,email= arg
        if account in self.ACCOUNT:
            return
        else:
            m = hashlib.sha256()
            m.update(passwd.encode())
            new_passwd = m.hexdigest()
            self.update_flie()
            return True

    def del_account(self,account:str):
        """从帐号字典中删除数据"""
        pop_account = self.ACCOUNT.pop(account)  
        self.update_flie()
        return pop_account

    def update_flie(self):
        with open(self.filename,"w",encoding="utf-8") as f:
            json.dump(self.ACCOUNT,f,ensure_ascii=False,indent=2)

    def validate(self,user:str ,password:str,autoflag=False,remflag=False) ->bool:
        # print(user,password)
        if user in self.ACCOUNT:
            m = hashlib.sha256()
            m.update(password.encode())
            new_passwd = m.hexdigest()
            # print(new_passwd,self.ACCOUNT[user])
            return new_passwd == self.ACCOUNT[user][0]
        return False


if __name__ == "__main__":
    pass
    # a = AccountManager()
    # a.add_account(("huliang","1233","","",""))
    # policy_cfg ={
    #     "ECS":"FixRule:2,cs;FixRule:8,?,del|-",
    #     "WST":"FixRule:4,4444",
    #     }
    # code_data = {
    #     "ECS":{
    #         "11":{
    #             "面板":["33-44-55-66",],
    #             "jike":["55-55-55-55",]
    #         },
    #         "22":{
    #             "面板2":["2333-4555-5",],
    #         },
    #     },
    #     "WST":{
    #         "33":{
    #             "面板3":["93333-4555-5",],
    #         },
    #         "44":{
    #             "面板4":["84333-4555-5",],
    #         },
    #     },
    # }