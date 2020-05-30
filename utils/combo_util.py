#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ ='huliang'
'''工具模块 '''

def changeComboBox(self,combo,txt):
    """改变combobox的信号处理方式"""  
    if combo not in self.combo_list:
        return
    index = self.combo_list.index(combo)
    for cb in self.combo_list[index+1:]:
        cb.blockSignals(True)
        cb.clear()
        cb.blockSignals(True)
    tmp = self.cfg.code_data
    if index > 0:
        for cb in self.combo_list[index]:
            tmp = tmp[cb.currentText()]
    self.combo_list[index+1].addItems(tmp[txt])   
