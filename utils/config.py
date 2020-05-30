#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ ='huliang'
'''帐号管理类 '''
import os
import json
from typing import Iterable, Tuple ,List
from .base import path_fixed ,pre_read
import settings  as cf

class Config:
    policy_cfg ={}
    code_data = {}
    policy_cate=("FixRule","RegRule","DateRule","FlowRule")  
    def __init__(self):   
        self.plicy_cfg_f = os.path.join( cf.PROJECT_DIR ,cf.POLICY_CFG) 
        self.fixcode_cfg_f =os.path.join( cf.PROJECT_DIR,cf.FIXCODE_CFG) 
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

if __name__ == "__main__":
    pass