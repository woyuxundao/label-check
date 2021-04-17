#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ ='huliang'
'''工具模块 '''
import os
import json
from typing import Iterable, Tuple ,List

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
        
class Const:
    def __init__(self,x:int):
        self.__value = x

    def __setattr__(self,key,value) -> bool:
        raise ValueError("const can not change")
    
    def __eq__(self,value):
        return value == self.__value

    def __and__(self,value):
        return value & self.__value
    
    def __rand__(self,value):
        return value & self.__value

    def __or__(self,value):
        return value | self.__value
    
    def __ror__(self,value):
        return value | self.__value
        
if __name__ == '__main__':
    l =Log()
    l.make("sfsf")
    del l
    # os.remove(os.path.join(os.getcwd(),"log/log.csv"))
    # os.removedirs(os.path.join(os.getcwd(),"log"))
