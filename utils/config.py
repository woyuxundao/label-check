#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ ='huliang'
'''帐号管理类 '''
import os
import json
import copy
from typing import Iterable, Tuple ,List
from .base import pre_read
import settings  as cf

class ConfigProperty:
    '''属性数据描述符'''
    def __init__(self,filename:str,):
        self.filename = filename
        self.content= pre_read(self.filename)

    def __get__(self,instance,cls):
        '''返回数据的拷贝，避免底层数据被错误修改'''
        if not instance.flag:
            return self.content
        return copy.deepcopy(self.content)

    def __set__(self,instance,value:dict):
        if self.content is value:
            self.save()
            return
        self.content=value
        self.save()
    
    def save(self):
        with open(self.filename,"w",encoding="utf-8") as f:
            json.dump(self.content, f,ensure_ascii=False, indent=2)        


plicy_cfg_f = os.path.join( cf.PROJECT_DIR ,cf.POLICY_CFG) 
fixcode_cfg_f =os.path.join( cf.PROJECT_DIR,cf.FIXCODE_CFG)

class Config:
    """用于管理规则和料号的类"""
    policy_cfg =ConfigProperty(plicy_cfg_f)
    code_data = ConfigProperty(fixcode_cfg_f)
    policy_cate=("FixRule","RegRule","DateRule","FlowRule")  

    def __init__(self):
        self.flag = False #用于改变数据描述符的处理状态
 
    def remove_item(self,tmp:Tuple[str]) -> bool:
        self.flag = True
        content = self.code_data
        self.flag =False
        if len(tmp) == 2 :
            content[tmp[0]].pop(tmp[1])
        if len(tmp) == 3:
            content[tmp[0]][tmp[1]].pop(tmp[2])
        if len(tmp) == 4 and tmp[3] in  content[tmp[0]][tmp[1]][tmp[2]]:
            content[tmp[0]][tmp[1]][tmp[2]].remove(tmp[3])    
        self.code_data = content #启用附着用进行自动把数据写入硬盘
        return True

    def add_item(self,ll:List[str]) ->bool:
        '''tmp为 规则/机型/品名/料号组成的字符串列表'''
        policy,module,name,pn = ll
        self.flag = True
        content = self.code_data
        self.flag =False
        tmp = content.setdefault(policy,{}) #避免in操作报错
        # print(f"tmp:{tmp}")
        if module not in tmp:
            tmp.update({module:{name:[pn]}})
        if name not in tmp[module]:
            tmp[module].update({name:[pn]})
        if pn not in tmp[module][name]:
            tmp[module][name].append(pn)
        self.code_data = content #启用附着用进行自动把数据写入硬盘
        return True


import sys
sys.modules[__name__] = Config()

if __name__ == "__main__":
    pass