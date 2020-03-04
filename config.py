#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ ='huliang'
''' 软件的配置信息'''
import sys
from typing import List ,Tuple
import json
import os

POLICY_CFG = r"policy_cfg.json"

class Config:
    policy_cfg ={
        "ECS":"FixRule:2,cs;FixRule:8,?,del|-",
        "WST":"FixRule:4,4444",
        }
    code_data = {
        "ECS":{
            "11":{
                "面板":["33-44-55-66",],
                "jike":["55-55-55-55",]
            },
            "22":{
                "面板2":["2333-4555-5",],
            },
        },
        "WST":{
            "33":{
                "面板3":["93333-4555-5",],
            },
            "44":{
                "面板4":["84333-4555-5",],
            },
        },
    }
    policy_cate=("FixRule","RegRule","DateRule","FlowRule")

    def __init__(self):        
        if not os.path.exists(POLICY_CFG):
            self.f =open(POLICY_CFG,"w+",encoding="utf-8")
        else:
            self.f =open(POLICY_CFG,"r+",encoding="utf-8")
            tmp = json.load(self.f)
            self.__class__.policy_cfg , self.__class__.code_data = tmp

    def __del__(self):
        #把配置信息policy_cfg写上文件中
        self.f.seek(0,0)#从文件开头进行
        self.f.truncate()
        json.dump([self.policy_cfg, self.code_data], self.f,ensure_ascii=False)
        self.f.close()
        # print("__del__,")

    def remove_policy(self, name:str) -> bool:
        if name in self.policy_cfg:
            del  self.__class__.policy_cfg[name]
            return True
        return False

    def edit_policy(self,policy_name ,content, model:bool=True) -> bool:
        '''model 为True是新增否则修改'''
        if not model and k in self.policy_cfg[policy_name]:
                return False
        self.policy_cfg[policy_name] = content
        return True

    @classmethod
    def remove_item(cls,tmp:Tuple[str]) -> bool:
        if len(tmp) == 2 :
            cls.code_data[tmp[0]].pop(tmp[1])
        if len(tmp) == 3:
            cls.code_data[tmp[0]][tmp[1]].pop(tmp[2])
        if len(tmp) == 4 and tmp[3] in  cls.code_data[tmp[0]][tmp[1]][tmp[2]]:
            cls.code_data[tmp[0]][tmp[1]][tmp[2]].remove(tmp[3])    

    @classmethod
    def add_item(cls,ll:List[str]):
        '''tmp为 规则/机型/品名/料号组成的字符串列表'''
        # print("ll列表内容:",ll)
        policy,module,name,pn = ll
        tmp = cls.code_data[policy]
        if module not in tmp:
            tmp.update({module:{name:[pn]}})
        if name not in tmp[module]:
            tmp[module].update({name:[pn]})
        if pn not in tmp[module][name]:
            tmp[module][name].append(pn)
        # print(cls.code_data)

if __name__ == '__main__':
    c = Config() 
