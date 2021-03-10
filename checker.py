#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ ='huliang'
'''检查器用于检查条码的信息是否正确
用户设置的参数为:   4 FixRule cs22;4 DateRule yymm; Flow:6,base|16,exculde|io,
模块之间用分好";"隔开,冒号":"分割规则和参数(参数用逗号","分割模块内的规则)。
FixRule 接受参数 字符串 del|- 删除字符 , replace|5*4 替换字符(以*分割右替换左)
FlowRule 接受参数,过滤器 base|16 ，base|37 ,exculde|io 进制，排除字符
DateRule 接受参数 年yy y ,月mm M,日 dd ,周期 WW，用逗号分隔，第一位为参数长度
 '''

from abc import ABCMeta , abstractmethod
from utils import config ,Log

class RuleAnallysisError(Exception):
    """规则解析错误"""
    def __str__(self):
        return "规则解析错误"

class RuleBase(metaclass=ABCMeta):
    def __init__(self,txt:str):
        '''把客户设置的参数转换对应的校验条件，用逗号拆分各规则条件保存在args列表中，
        如有过滤器则放入kwargs字典中。        
        '''
        self.original_args =txt
        args = [i for i in txt.split(",") if len(i) >0] #按逗号拆分
        self.length =args[0] 
        self.args = []
        self.kwargs = {}
        self.fixcode=""  #为了使固定条码匹配留下方便的存储位置
        #确认长度信息是否为正整数
        if self.length.isdecimal() and "." not in self.length:
            self.length =abs(int(self.length))
        else:
            raise RuleAnallysisError("参数无长度信息")
        #如有有其他字典参数加入
        for arg in args[1:] : 
            if "|" in  arg:   #按|拆分，生成过滤器
                k , v = arg.split("|")
                self.kwargs[k] = v
            else:    
                self.args.append(arg) #把剩余的参数存入
 
    @abstractmethod
    def check(self, txt:str) -> (bool,str):
        """条码规则校验"""
        pass

    def set_fixcode(self,txt:str):
        self.fixcode = txt

class FixRule(RuleBase):
    ''' 识别固定字符，过滤器del删除字符，过滤器replace替换字符用*隔开 '''
    def check(self, input:str ) -> (bool,str) :
        # print(f"fixrule检查字段：{input} ")
        if "?" in  self.args:
            self.__input = input   

            return self.fixcode_check() #返回可调用的函数
        # print(f"input:{input} args :{self.args} ")    
        if len(self.args) != 0 and len(self.args[0]) != self.length:
            # print(self.args, self.length)
            raise RuleAnallysisError("固定字符长度不对")
        if self.args[0] == input:
            return True,""
        else:
            return False,"固定字符不匹配"
    
    def fixcode_check(self) -> (bool,str):
        """用于没有提前输入的固定字符的验证"""
        if "del" in self.kwargs:
            self.fixcode = self.fixcode.replace(self.kwargs["del"],"")
        if "replace" in self.kwargs:
            self.fixcode = self.fixcode.replace(self.kwargs["replace"].split("*"))
        #print(f"fixed txt:{self.fixcode},原始字符串：{self.__input}")
        if self.fixcode == self.__input:
            return True,""
        else:
            return False,"无法匹配条码"
            
class RegRule(RuleBase):
    '''高级用户使用,规则错误会导致永远返回错误'''
    def check(self,txt:str):
        # print(f"regrule检查字段：{txt} ")
        import re
        #re规则中除长度相关的信息外(+1避开逗号),全部都是匹配规则
        # print(self.original_args,txt)
        result =re.search(r""+self.original_args[self.length+1:],txt)
        if result is None:
            return False,"正则无法匹配"
        return True,""
        
class DateRule(RuleBase):
    def check(self,txt:str) -> (bool,str):
        if self.length != len("".join(self.args)):
            raise RuleAnallysisError("时间参数的长度不对")
        if len(txt) != self.length:
            raise ValueError("校验字符长度错误")
        #print(f"datarule检查字段：{txt} ")
        import datetime
        now =datetime.datetime.now()
        self.year = now.year
        self.month =now.month
        self.weeks = now.isocalendar().week #一年的第几周
        self.day = now.day                  #一月的第几天
        self.day365=now.timetuple().tm_yday #一年的第几天
        tmp = txt
        #print(f"时间参数{self.args}")
        args_cate = ("y","Y","mm","M","dd","ddd","WW")
        #判定参数是否超出限定范围
        if len(set(args_cate) | set(self.args) )> len(args_cate):
            raise RuleAnallysisError("时间参数的类别不对")         
        for arg in self.args:
            n = len(arg) #参数的长度
            func = getattr(self,arg)
            ok,message = func(tmp[:n])
            if not ok:
                return ok,message
            tmp = tmp[n:]  

        return True,""

    def y(self,txt:str) ->(bool,str):
        if txt.isnumeric():
            result = int(txt) - self.year%10
        else:
            return False,"年份参数错误"
        # print(result)
        if abs(result) > 1 and abs(10 - result)>1:
            return False,"年份错误"
        return True,""

    def Y(self,txt:str) ->(bool,str):
        if txt.isnumeric():
                result = int(txt) - self.year%10
        else:
            result = ord(txt.lower()) -88 - self.year%100  #如果是字母则转换成两位数的年份，再比较
            # print(f"result:{result} {txt} {self.year}")
        if abs(result) > 1:
            return False,"年份错误" 
        return True,""

    def mm(self,txt:str) ->(bool,str):
        result = int(txt) - self.month
        if result > 1 or  result < -1:
            return False,"月份错误"
        return True,""

    def M(self,txt:str) ->(bool,str):
        if txt.isnumeric():
            result = int(txt) - self.month
        else:
            result = ord(txt.lower()) -87 - self.month
        if result > 1 or  result < -1:
            return False,"月份错误"
        return True,""
        
    def d(self,txt:str) ->(bool,str):
        if txt.isnumeric():
            result = int(txt) - self.day
        else:
            result = ord(txt.lower()) -87 - self.day
        if result > 30 or  result < -30:
            return False,"天数错误"
        return True,""
        
    def dd(self,txt:str) ->(bool,str):
        if not txt.isnumeric():
            return False,"dd格式必须为两位数字"
        result = self.day -int(txt)
        if result > 30 or  result < -30:
            return False,"天数错误"
        return True,""
        
    def ddd(self,txt:str) ->(bool,str):
        if not txt.isnumeric():
            return False,"ddd格式必须为三位位数字"  
        result = self.day365 - int(txt)
        if result > 30 or  result < -30:
            return False,"条码超过30天"
        return True,""
        
    def WW(self,txt:str) ->(bool,str):
        if not txt.isnumeric():
            return False,"年份参数错误"
        result = self.weeks - int(txt)
        if abs(result) > 3 :
            return False,"条码超过3周"
        return True,""
        

class FlowRule(RuleBase):
    ascii_lowercase = "abcdefghijklmnopqrstuvwxyz"
    ascii_uppercase ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number ="0123456789"

    def check(self, txt:str) ->(bool,str):
        # print(f"flowrule检查字段：{txt} ")
        self.rule =""
        if "base" not in self.kwargs:
            self.rule =self.number + self.ascii_uppercase
        else:
            tmp =self.kwargs["base"]
            if tmp.isdecimal() and "." not in tmp:
                tmp = int(tmp)
            if tmp <0:
                tmp = -tmp
            if tmp > 10 and tmp < 37:               
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
        self._rules =tuple(rule for rule in globals().keys() if "Rule" in rule)
        self.repeatFlag = True
        self.fixcode = ""
        self.log = None
        for item in policy_src.split(";"): 
            if item == "norepeat" or item.strip() == "":
                self.repeatFlag =False
                continue
            if len(item.split(":")) < 2 :
                raise RuleAnallysisError("没有足够的参数,必须用:分割规则和参数")
            if item.split(":")[0] not in self._rules:
                print(f"规则列表{self._rules}")
                raise RuleAnallysisError("找不到相应的规则")
            rule ,args = item.split(":")
            #print("rule args:",rule,args)
            if len(args) == 0:
                raise RuleAnallysisError("没有足够的参数")
            #在全局对象中找到对应的类,然后传入参数创建对象加入列表
            #print(f"rule:{rule} ;args:{args}")
            self.rules.append(globals()[rule](args))
        #print(f"现在的规格{self.rules}")
    
    def check(self,txt:str) -> (bool,str):
        # result_list=[] #存储结果列表
        self.length = sum( i.length for i in self.rules)
        #print("length:",self.length,self.rules)
        if len(txt) != self.length:
            #print(f"条码:{txt},长度:{self.length}")
            return False,"条码长度不相符"
        tmp = txt #临时变量        
        for rule in self.rules:
            # print(f"当前校验的rule：{rule.__class__.__name__}")
            rule.set_fixcode(self.fixcode)
            result = rule.check(tmp[:rule.length])    
            tmp= tmp[rule.length:]
            if result[0] is False:
                return result 
        return True,""

    def set_fixcode(self,txt:str):
        #把pn加入未加载FixRule未输入的内容中
        self.fixcode = txt

class Checker:
    """参数model设置时按要求匹配验证,否则扫描全部"""
    def __init__(self):
        self.policys =[]
        self.model = None
        self.cfg = config       #从配置类中获取相应的数据
        #条码暂存容器验证重码
        self.codes=set()
        #print("checker confg",self.cfg)
        for name,policy_srcs in self.cfg.policy_cfg.items():
            # print(f"policy:{name} src:{policy_src}")
            for policy_src in policy_srcs:
                if len(policy_src.strip()) ==0 :
                    continue
                self.policys.append(Policy(name,policy_src))

    def setMode(self,model:dict):
        """设置或清除机型信息"""
        self.model = None       
        if model:
            if "customer"  in model  and "pn"  in model :
                self.model = model
            else:
                print("字典参数model必须有custom和pn key的，否则设为None") 
  
        
    def check(self,txt:str) -> (bool,str):
        '''校验输入的内容,如果未设置具体的model就遍历检查 '''
        #print("检查器的model",self.model)
        if self.model:
            result = None
            for policy in self.policys:
                if self.model["customer"] == policy.name :
                    result = self.check_one(txt, policy,self.model)
                    if result[0]:
                        return result
            else:
                return result

        for policy in self.policys:
            print(f"正在匹配的规则{policy.name}")
            if not self.cfg.code_data.get(policy.name):
                #print("此规则为没有对应的机型，进行下一个规则检查")
                result = self.check_one(txt,policy,{})     
                if result[0]:
                    return reuslt           
                continue
            for module, tmp  in self.cfg.code_data[policy.name].items():
                # print("module,tmp",module,tmp)
                for name , pns in tmp.items():    
                    for pn in pns: 
                        result = self.check_one(txt,policy,{"customer":policy.name,"module":module,"name":name,"pn":pn})  
                        if result[0]:return result
        return False,"没有匹配的规则"

    def check_one(self,txt,policy,model:dict) -> (bool,str):
        #按照给定的具体信息匹配验证
        if not len(model) == 0:
            policy.set_fixcode(model["pn"])
        result = policy.check(txt)
        # print(f"规则{policy.name} 结果如下:{result}")
        # print("rules:",[rule.__class__.__name__ for rule in policy.rules])
        if result[0]:
            self.model = model
            if not policy.repeatFlag :
                #只有在规则定义无重复且之前条码验证ok时才验证重复性
                return self.checkRepeat(txt)
        return result
    
    def checkRepeat(self,code:str) ->(bool,str):
        '''获取资料中所有已存在的条码,检查此条码是否有重复'''
        if code in self.codes:
            return False,"条码重复"
        else:
            self.codes.add(code)
            return True,""

if __name__ == '__main__':
    b ={"customer":"ECS","pn":"123-456-78"}
    c = Checker()
    c.setMode(b)
    print(c.check("12345678"))
    # f =FixRule("4,ssss")
    # print(f.length)
    # d = DateRule("3,ydd")
    # print(d.check("92"))


