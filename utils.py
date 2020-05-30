#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ ='huliang'
'''工具模块 '''
import os
import csv
import hashlib
import json
import sqlite3
from typing import Iterable, Tuple ,List
import config as cf

def path_fixed(filename:str) ->bool:
    #处理文件路径的问题
    if os.path.exists(filename):
        return True
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename)) 
            return True
        except FileNotFoundError:
            print(f"{filename}路径无法找到")
        except Error:
            print("未知错误")
    return False

def pre_read(filename):
    if path_fixed(filename):
        with open(filename,"r+",encoding="utf-8") as f:
            if os.path.getsize(filename) > 0 :
                return json.loads(f.read())
    return {}        

class Log():
    """记录校验记录的类"""
    def __init__(self):
        filename =os.path.join( os.path.dirname(__file__) ,cf.CHECK_SAVE_FILE) 
        flag = path_fixed(filename)
        self.csvf = open(filename,"a+",encoding="utf-8",newline='\n')
        self.writer = csv.writer(self.csvf, delimiter=',')
        #在文件的开头写入列名称
        if not flag or self.csvf.tell() < 11:
            self.writer.writerow(["时间","结果判定","序列号","操作员"])

    def make(self, x:Iterable):
        self.writer.writerow(x)
        self.csvf.flush()
        # print("日志正在写入:",x)
    
    def repeat_check(self,x:str) ->(bool,str):
        # current = self.csvf.tell()
        self.csvf.seek(0)
        for rows in csv.reader(self.csvf,delimiter=','):
            if row[2] == x:
                return False,"条码 "
        return True,""


class AccountManager():
    """建立帐号管理的模块"""
    ACCOUNT = {}
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance    

    def __init__(self,*args, **kwargs):
        filename =os.path.join( os.path.dirname(__file__) ,cf.ACCOUNT_CFG) 
        flag = path_fixed(filename)
        if flag:
            #读取json文件中的内容
            with open(filename,"r+",encoding="utf-8") as f:
                if os.path.getsize(filename) > 0 :
                    self.__class__.ACCOUNT = json.loads(f.read())

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
            self.__class__.ACCOUNT[account] = (new_passwd,department,job,email)
            with open(filename,"w",encoding="utf-8") as f:
                json.dump(self.__class__.ACCOUNT,f,ensure_ascii=False,indent=2)
            return True

    def validate(self,user:str ,password:str,autoflag=False,remflag=False) ->bool:
        # print(user,password)
        if user in self.ACCOUNT:
            m = hashlib.sha256()
            m.update(password.encode())
            new_passwd = m.hexdigest()
            # print(new_passwd,self.ACCOUNT[user])
            return new_passwd == self.ACCOUNT[user][0]
        return False

    def del_account(self,account:str):
        return self.__class__.ACCOUNT.pop(account)    
        
class Config:

    policy_cfg ={}
    code_data = {}
    policy_cate=("FixRule","RegRule","DateRule","FlowRule")  
    def __init__(self):   
        self.plicy_cfg_f = os.path.join( os.path.dirname(__file__) ,cf.POLICY_CFG) 
        self.fixcode_cfg_f =os.path.join( os.path.dirname(__file__) ,cf.FIXCODE_CFG) 
        self.__class__.policy_cfg = pre_read(self.plicy_cfg_f) #预读数据到类变量
        self.__class__.code_data = pre_read(self.fixcode_cfg_f)

    def remove_policy(self, name:str) -> bool:
        if name in self.policy_cfg:
            del  self.__class__.policy_cfg[name]
            #把配置信息policy_cfg写上文件中                     
            return True
        self.update_policy() 
        return False

    def edit_policy(self,policy_name ,content, model:bool=True) -> bool:
        '''model 为True是修改否则新增'''
        if not model and  policy_name in self.policy_cfg:
                return False
        self.policy_cfg[policy_name] = content
        self.update_policy()        
        return True

    def remove_item(self,tmp:Tuple[str]) -> bool:
        cls = self.__class__
        # print("rm",tmp)
        if len(tmp) == 2 :
            cls.code_data[tmp[0]].pop(tmp[1])
        if len(tmp) == 3:
            cls.code_data[tmp[0]][tmp[1]].pop(tmp[2])
        if len(tmp) == 4 and tmp[3] in  cls.code_data[tmp[0]][tmp[1]][tmp[2]]:
            cls.code_data[tmp[0]][tmp[1]][tmp[2]].remove(tmp[3])    
        self.update_fixcode()

    def add_item(self,ll:List[str]):
        cls = self.__class__
        '''tmp为 规则/机型/品名/料号组成的字符串列表'''
        # print("ll列表内容:",ll)
        policy,module,name,pn = ll
        # print("xxx",ll)
        tmp = cls.code_data.setdefault(policy,{}) #避免in操作报错
        # print("tmp",tmp)
        if module not in tmp:
            tmp.update({module:{name:[pn]}})
        if name not in tmp[module]:
            tmp[module].update({name:[pn]})
        if pn not in tmp[module][name]:
            tmp[module][name].append(pn)
        self.update_fixcode()
        # print(cls.code_data)

    def update_policy(self): 
        with open(self.plicy_cfg_f,"w",encoding="utf-8") as f:
            json.dump(self.policy_cfg, f,ensure_ascii=False, indent=2)
    
    def update_fixcode(self):
        with open(self.fixcode_cfg_f,"w",encoding="utf-8") as f:
            json.dump(self.code_data, f,ensure_ascii=False, indent=2)


        
if __name__ == '__main__':
    l =Log()
    l.make("sfsf")
    del l
    # os.remove(os.path.join(os.getcwd(),"log/log.csv"))
    # os.removedirs(os.path.join(os.getcwd(),"log"))
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