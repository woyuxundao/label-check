#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ ='huliang'
''' 软件的配置信息'''

#条码规则设置文件
POLICY_CFG =  "etc/policy_cfg.json"
#帐号配置文件
ACCOUNT_CFG = "etc/account.json"
#条码校验记录文件
CHECK_SAVE_FILE = "log/log.csv"

#update条码校验记录
LOG_SETTING ={
    "type":"sqlite", #sqlite/csv
    "path_name":"log/log.db",
}
#帐号配置文件
ACCOUNT_SETTING={
    "type":"sqlite", #sqlite/csv
    "path_name":"etc/acount.db",
}


    
