#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ ='huliang'
'''检查器用于检查条码的信息是否正确
用户设置的参数为:   FixRule:4,cs22;DateRule:4,yymm;Flow:6,base|16,exculde|io,
模块之间用分好";"隔开,冒号":"分割规则和参数(参数用逗号","分割)
FixRule 接受参数 字符串 del|-  replace|5-4 删除字符 ,替换字符(以-分割右替换左)
FlowRule 接受参数 base|16 exculde|io 进制,排除字符
DateRule 接受参数 年yy y Y 月mm M 日 dd 周期 ww
 '''

from abc import ABCMeta , abstractmethod
from utils import Config ,Log

class RuleAnallysisError(Exception):
    """规则解析错误"""
    pass

class RuleBase(metaclass=ABCMeta):
    def __init__(self,txt:str):
        '''把客户设置的参数转换对应的校验条件'''
        # print("RuleBase 初始化")
        self.original_args =txt
        '''解析字符串''' 
        args = [i for i in txt.split(",") if len(i) >0]
        self.length =args[0] 
        self.args = []
        self.kwargs = {}
        #确认长度信息是否为正整数
        if self.length.isdecimal() and "." not in self.length:
            self.length =abs(int(self.length))
        else:
            raise RuleAnallysisError("参数无长度信息")
        #如有有其他字典参数加入
        for arg in args[1:] :
            if "|" in  arg:
                k,v = arg.split("|")
                self.kwargs[k] = v
            self.args.append(arg)
 
    @abstractmethod
    def check(self, txt:str) -> (bool,str):
        """条码规则校验"""
        pass

class FixRule(RuleBase):
    ''' 识别固定字符 '''
    def check(self, input:str ) -> (bool,str) :
        if "?" in  self.args:
            self.__input__ = input          
            return self.reCheck #返回可调用的函数
        if len(self.args[0]) != self.length:
            # print(self.args, self.length)
            raise RuleAnallysisError("固定字符长度不对")

        if self.args[0] == input:
            return True,""
        else:
            return False,"固定字符不匹配"
    
    def reCheck(self,fixed:str) -> (bool,str):
        """用于没有提前输入的固定字符的验证"""
        if "del" in self.kwargs:
            fixed = fixed.replace(self.kwargs["del"],"")
        if "replace" in self.kwargs:
            fixed = fixed.replace(self.kwargs["replace"].split("-"))
        # print("fixed txt:",fixed,self.__input__)
        if fixed == self.__input__:
            return True,""
        else:
            return False,"无法匹配条码"
            
class RegRule(RuleBase):
    '''高级用户使用,规则错误会导致永远返回错误'''
    def check(self,txt:str):
        import re
        #re规则中除长度相关的信息外,全部都是匹配规则
        result =re.search(self.original_args[self.length:],txt)
        if result is None:
            return False,"正则无法匹配"
        return True,""
        
class DateRule(RuleBase):
    def check(self,txt:str) -> (bool,str):
        if self.length != len(self.args[0]):
            raise RuleAnallysisError("时间参数的长度不对")
        if len(txt) != self.length:
            raise ValueError("校验字符长度错误")
        import time 
        now = time.localtime(time.time())
        year =now.tm_year
        month = now.tm_mon
        weakday = now.tm_yday//7
        tmp = txt
        setup ={}
        for i in self.args[0]:
            if i not in "Yymdw":
                raise RuleAnallysisError("时间参数的类别不对")
            setup[i] = setup.setdefault(i,0) +1
        # print(setup)
        if  "y" in setup and setup["y"] > 0:
            n = setup["y"]
            if tmp[:n].isnumeric():
                result = int(tmp[:n] ) - year%(10**n)
            else:
                raise ValueError("年份参数错误")
            # print(result)
            if abs(result) > 1 and abs(10 - result)>1:
                return False,"年份错误"
            tmp =tmp[ setup["y"]:]
        if "Y" in setup and setup["Y"] == 1:
            if tmp[0].isnumeric():
                result = int(tmp[0]) - year%1000
            else:
                result = ord(tmp[0].lower()) -87 - year%100
            if abs(result) > 1:
                return False,"年份错误"
            tmp = tmp[1:]
        if "w" in setup and setup['w'] ==2 :
            result = week - int(tmp[:2])
            if result > 3 or  result < -3:
                return False,"周期超过3周"
        if "m" in setup and setup["m"] >0:
            n = setup["m"]
            result = int(tmp[:n] ) - year%(10**n)
            if result > 1 or  result < -1:
                return False,"月份错误"
            tmp =tmp[ setup["m"]:]
        if  "M" in setup and setup["M"] == 1:
            if tmp[0].isnumeric():
                result = int(tmp[0]) - year%1000
            else:
                result = ord(tmp[0].lower()) -87 - year%100
            if result > 1 or  result < -1:
                return False,"月份错误"
            tmp = tmp[1:]
        if "d" in setup and setup["d"] == 3 :
            result = now.tm_yday - int(tmp[:3])
            if result > 30 or  result < -30:
                return False,"天数错误"
        if "d" in setup and setup["d"] ==2:
            result = now.tm_mday -int(tmp[:2])
            if result > 30 or  result < -30:
                return False,"天数错误"
        if "d" in setup and setup["d"] == 1:
            if tmp[0].isnumeric():
                result = int(tmp[0]) - now.tm_mday
            else:
                result = ord(tmp[0].lower()) -87 - now.tm_mday
            if result > 30 or  result < -30:
                return False,"天数错误"
        return True,""

class FlowRule(RuleBase):
    ascii_lowercase = "abcdefghijklmnopqrstuvwxyz"
    ascii_uppercase ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number ="0123456789"

    def check(self, txt:str) ->(bool,str):
        self.rule =""

        if "base" not in self.kwargs:
            self.rule =self.number + self.ascii_uppercase
        else:
            tmp =self.kwargs["base"]
            if tmp.isdecimal() and "." not in tmp:
                tmp = int(tmp)
            if tmp <0:
                tmp = -tmp

            if self.kwargs["base"] > 10 and self.kwargs["base"] < 37:               
                self.rule =self.number + self.ascii_uppercase[:tmp-10] 
        #移除需要筛选的字符
        if "exculde"  in self.kwargs:
            for i in self.kwargs["exculde"]:
                self.rule = self.replace(i,"")

        for  x in txt:
            if  x not in self.rule:
                return False,"流水号错误"  
        return True,""
            

class Policy:
    def __init__(self,name:str,policy_src:str):
        self.name = name 
        self.rules =[]
        self._rules =("FixRule","RegRule","DateRule","FlowRule")
        self.repeatFlag = True
        self.fixed_txt = None
        self.log = None
        for item in policy_src.split(";"): 
            if item == "norepeat" or item.strip() == "":
                self.repeatFlag =False
                continue
            if len(item.split(":")) < 2 :
                raise RuleAnallysisError("没有足够的参数,必须用:分割规则和参数")
            if item.split(":")[0] not in self._rules:
                raise RuleAnallysisError("找不到相应的规则")
            rule ,args = item.split(":")
            if len(args) == 0:
                raise RuleAnallysisError("没有足够的参数")
            #在全局对象中找到对应的类,然后传入参数创建对象加入列表
            self.rules.append(globals()[rule](args))
        # print("rules:",self.rules)
    
    def check(self,txt:str) -> (bool,str):
        # print(self.rules[0])
        # print("rules:",self.rules[1].length)
        self.length = sum( i.length for i in self.rules)
        # print("length:",self.length)
        if len(txt) != self.length:
            # print(txt,self.length)
            return False,"条码长度不相符"
        tmp = txt #临时变量

        for rule in self.rules:
            result = rule.check(tmp[:rule.length])           
            # print("检查字段:",rule.__class__.__name__ ,tmp)
            if callable(result):
                #此次加载固定的条目以便深入校验
                # print("fixed_txt:",self.fixed_txt)
                result = result(self.fixed_txt)
            if result[0] is False:
                return result

            tmp = tmp[ rule.length: ]
        if self.repeatFlag:
            return True ,""
        else:
            if self.log is None:
                self.log = Log()
            return self.log.repeat_check(txt)
        #需要增加对重复的判定,在外部设置

    def add_fix_txt(self,fix:str):
        #把pn加入未加载FixRule未输入的内容中
        self.fixed_txt = fix


    def test(self):
        pass

class Checker:
    """参数model设置时按要求匹配验证,否则扫描全部"""
    def __init__(self,config):
        self.policys =[]
        self.model = None
        self.sucess = None
        if self.model and "customer" not in model  and "pn" not in model :
            raise Exception("字典参数model必须有custom和pn key的")       
        #从配置类中获取相应的
        if config:
            self.cfg = config 
        else :
            from utils import Config
            slef.cfg = Config()

        # print("checker confg",self.cfg)
        for name,policy_src in self.cfg.policy_cfg.items():
            self.policys.append(Policy(name,policy_src))

    def setMode(self,model:dict):
        """"""
        self.model = model

    def check(self,txt:str) -> (bool,str):
        '''校验输入的内容 '''
        # print("policys:",self.policys)
        for policy in self.policys:
            if self.model:
                if policy.name == self.model["customer"]:
                    return self.checkOne(txt, policy , self.model)
            # print(self.cfg.code_data)
            if not self.cfg.code_data.get(policy.name):
                raise Exception(f"条码规则config资源不存在{policy.name} key")
            for module, tmp  in self.cfg.code_data[policy.name].items():
                for name , pns in tmp.items():          
                    for pn in pns:    
                        # print("customer module name pn:",policy.name ,module ,name ,pn)         
                        return self.checkOne(txt,policy,{"customer":policy.name,"module":module,"name":name,"pn":pn })

        return False,"没有匹配的规则"

    def checkOne(self, txt:str, policy, model:dict ) -> (bool,str):
        # print("policy ,model",policy,model)
        policy.add_fix_txt(model["pn"])
        result = policy.check(txt)
        #只有在规则定义无重复且之前条码验证ok时才验证重复性
        if result[0]:
            self.sucess = model
        if not policy.repeatFlag and result[0]:
            return self.checkRepeat(txt)
        return result       
    
    def checkRepeat(self,code:str) ->(bool,str):
        '''获取资料中所有已存在的条码,检查此条码是否有重复'''
        return True,""
        return False,"条码重复"


if __name__ == '__main__':
    b ={"customer":"ECS","pn":"123-456-78"}
    c = Checker(b)
    print(c.check("12345678"))
    # f =FixRule("4,ssss")
    # print(f.length)
    # d = DateRule("3,ydd")
    # print(d.check("92"))


