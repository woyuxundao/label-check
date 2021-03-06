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

class RuleAnallysisError(Exception):pass #规则解析错误
class RuleTypeError(TypeError):pass #规则参数类型错误

SUCESS = 3
PARTIY_SUCESS = 1
FAIL = 0
class RuleBase(metaclass=ABCMeta):
    def __init__(self,txt:str):
        '''把客户设置的参数转换对应的校验条件，用逗号拆分各规则条件保存在args列表中，
        如有过滤器则放入kwargs字典中。        
        '''
        self.original_args =txt
        if len(txt) == 0:
            raise RuleTypeError("参数不可为空") 
        args = [i for i in txt.split(",") if len(i) >0] #按逗号拆分
        self.length =args[0] 
        self.args = []
        self.kwargs = {}
        self.fixcode=""  #为了使固定条码匹配留下方便的存储位置
        #确认长度信息是否为正整数
        if self.length.isdecimal():
            self.length =abs(int(self.length))
        else:
            raise RuleTypeError("参数无长度信息")
        #如有有其他字典参数加入
        tmp_args = [] #临时列表方便后续替换
        for arg in args[1:] : 
            if "|" in  arg:   #按|拆分，生成过滤器
                k , v = arg.split("|")
                self.kwargs[k] = v
            else:    
                tmp_args.append(arg) #把剩余的参数存入
        self.args =tmp_args

    @abstractmethod
    def check(self, txt:str) -> (bool,str):
        """条码规则校验"""
        pass

    def set_fixcode(self,txt:str):
        self.fixcode = txt

class FixRule(RuleBase):
    ''' 识别固定字符，过滤器del删除字符，过滤器replace替换字符用*隔开 '''
    def check(self, input:str ) -> (bool,str) :
        print(f"fixrule检查字段：{input} ")
        if "?" in  self.args or "？" in  self.args:
            self.__input = input   
            return self.fixcode_check() #返回可调用的函数
        print(f"input:{input} args :{self.args} ")    
        if len(self.args) != 0 and sum(len(i) for i in self.args) != self.length:
            print(self.args, self.length)
            raise RuleAnallysisError("固定字符长度不对"+self.args[0])
        if self.args[0] == input:
            return SUCESS,""
        else:
            return FAIL,"固定字符不匹配"
    
    def fixcode_check(self) -> (bool,str):
        """用于没有提前输入的固定字符的验证"""
        if "del" in self.kwargs:
            self.fixcode = self.fixcode.replace(self.kwargs["del"],"")
        if "replace" in self.kwargs:
            self.fixcode = self.fixcode.replace(self.kwargs["replace"].split("*"))
        print(f"fixed txt:{self.fixcode},原始字符串：{self.__input}")
        if self.fixcode == self.__input:
            return SUCESS,""
        else:
            return FAIL,"无法匹配条码"
            
class RegRule(RuleBase):
    '''高级用户使用,规则错误会导致永远返回错误'''
    def check(self,txt:str):
        # print(f"regrule检查字段：{txt} ")
        import re
        #re规则中除长度相关的信息外(+1避开逗号),全部都是匹配规则
        # print(self.original_args,txt)
        result =re.search(r""+self.original_args[self.length+1:],txt)
        if result is None:
            return FAIL,"正则无法匹配"
        return SUCESS,""
        
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
        self.weeks = now.isocalendar()[1] #一年的第几周
        self.day = now.day                  #一月的第几天
        self.day365=now.timetuple().tm_yday #一年的第几天
        tmp = txt
        #print(f"时间参数{self.args}")
        args_cate = ("y","yy","yyyy","Y","mm","M","d","dd","ddd","WW")
        #判定参数是否超出限定范围
        if len(set(args_cate) | set(self.args) )> len(args_cate):
            raise RuleAnallysisError("时间参数的类别不对") 
        res_content =[]#用于放置校验的结果,只放非错误的结果        
        for arg in self.args:
            n = len(arg) #参数的长度
            func = getattr(self,arg)
            result =func(tmp[:n])
            if result[0] == FAIL:
                return result
            if result[0] == PARTIY_SUCESS:
                res_content.append(result)
            tmp = tmp[n:]  
        if len(res_content) == 0:
            return SUCESS,""
        else:
            return res_content[0]

    def y(self,txt:str) ->(bool,str):
        if txt.isnumeric():
            result = int(txt) - self.year%10
        else:
            return FAIL,"年份参数错误"
        # print(result)
        if abs(result) > 1 and abs(10 - result)>1:
            return PARTIY_SUCESS,"条码年份超过一年" 
        return SUCESS,""

    def yy(self,txt:str) ->(bool,str):
        if txt.isnumeric():
            result = int(txt) - self.year%100
        else:
            return FAIL,"年份参数错误"
        # print(result)
        if abs(result) > 1 and abs(10 - result)>1:
            return PARTIY_SUCESS,"条码年份超过一年" 
        return SUCESS,""

    def yyyy(self,txt:str) ->(bool,str):
        if txt.isnumeric():
            result = int(txt) - self.year
        else:
            return FAIL,"年份参数错误"
        # print(result)
        if abs(result) > 1 and abs(10 - result)>1:
            return PARTIY_SUCESS,"条码年份超过一年" 
        return SUCESS,""

    def Y(self,txt:str) ->(bool,str):
        if txt.isnumeric():
                result = int(txt) - self.year%10
        else:
            result = ord(txt.lower()) -88 - self.year%100  #如果是字母则转换成两位数的年份，再比较
            # print(f"result:{result} {txt} {self.year}")
        if abs(result) > 1:
            return PARTIY_SUCESS,"条码年份超过一年" 
        return SUCESS,""

    def mm(self,txt:str) ->(bool,str):
        result = int(txt) - self.month
        if result > 1 or  result < -1:
            return PARTIY_SUCESS,"条码月份超过一个月" 
        return SUCESS,""

    def M(self,txt:str) ->(bool,str):
        if txt.isnumeric():
            result = int(txt) - self.month
        else:
            result = ord(txt.lower()) -87 - self.month
        if result > 1 or  result < -1:
            return PARTIY_SUCESS,"条码月份超过一个月" 
        return SUCESS,""
        
    def d(self,txt:str) ->(bool,str):
        if txt.isnumeric():
            result = int(txt) - self.day
        else:
            result = ord(txt.lower()) -87 - self.day
        if result > 30 or  result < -30:
            return PARTIY_SUCESS,"条码天数超过一个月" 
        return SUCESS,""
        
    def dd(self,txt:str) ->(bool,str):
        if not txt.isnumeric():
            return FAIL,"dd格式必须为两位数字"
        result = self.day -int(txt)
        if result > 30 or  result < -30:
            return PARTIY_SUCESS,"条码天数超过一个月" 
        return SUCESS,""
        
    def ddd(self,txt:str) ->(bool,str):
        if not txt.isnumeric():
            return FAIL,"ddd格式必须为三位位数字"  
        result = self.day365 - int(txt)
        if result > 30 or  result < -30:
            return PARTIY_SUCESS,"条码超过30天"
        return SUCESS,""
        
    def WW(self,txt:str) ->(bool,str):
        if not txt.isnumeric():
            return FAIL,"年份参数错误"
        result = self.weeks - int(txt)
        if abs(result) > 3 :
            return PARTIY_SUCESS,"条码超过3周"
        return SUCESS,""
        
class FlowRule(RuleBase):
    # ascii_lowercase = "abcdefghijklmnopqrstuvwxyz"
    ascii_uppercase ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number ="0123456789"

    def check(self, txt:str) ->(bool,str):
        # print(f"flowrule检查字段：{txt} ")
        self.rule = self.number + self.ascii_uppercase
        if "base" not in self.kwargs:
            self.rule = self.rule[:10]
        else:
            tmp =self.kwargs["base"]
            print(f"tmp:{tmp}",type(tmp))
            if tmp.isdecimal():
                tmp = int(tmp)
                if 10< tmp < 37:               
                    self.rule =self.rule[:tmp] 
                else:
                    raise RuleTypeError("进制最多为36进制，实际为{tmp}")
        #移除需要筛选的字符
        if "exculde"  in self.kwargs:
            for i in self.kwargs["exculde"]:
                self.rule = self.rule.replace(i,"")

        for  x in txt:
            if  x not in self.rule:
                print(f"....---x:{x},self.rule:{self.rule}")
                return FAIL,"流水号错误"  
        return SUCESS,""
            
class Policy:
    def __init__(self,name:str,policy_src:str):
        self.name = name 
        self.rules =[]
        self._rules =tuple(rule for rule in globals().keys() if "Rule" in rule)
        self.repeatFlag = True #True标识可以重复
        self.fixcode = ""
        self.log = None
        for item in policy_src.split(";"): 
            if "FlowRule" in item: #如果规则中有流水号则说明条码不可重复
                self.repeatFlag =False
                
            if len(item.split(":")) < 2 :
                raise RuleAnallysisError("没有足够的参数,必须用:分割规则和参数")
            if item.split(":")[0] not in self._rules:
                #print(f"规则列表{self._rules}")
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
        self.length = sum( i.length for i in self.rules)
        # print("length:", [i.length for i in self.rules])
        if len(txt) != self.length:
            # print(f"条码:{txt},长度:{self.length}")
            return FAIL,"条码长度不相符"
        tmp = txt #临时变量  
        res_content =[] #存放非错的内容      
        for rule in self.rules:
            print(f"当前校验的rule：{rule.__class__.__name__}")
            rule.set_fixcode(self.fixcode)
            result = rule.check(tmp[:rule.length])    
            #print(f"result:{result}")
            tmp= tmp[rule.length:]
            if result[0] == FAIL:
                return result
            if result[0] == PARTIY_SUCESS:
                res_content.append(result)
        if len(res_content) >0:
            return res_content[0]    
        else:
            return SUCESS,""

    def set_fixcode(self,txt:str):
        #把pn加入未加载FixRule未输入的内容中
        self.fixcode = txt

class Checker:
    """参数model设置时按要求匹配验证,否则扫描全部"""
    def __init__(self):
        self.policys =[]
        self.model = None
        self.cfg = config       #从配置类中获取相应的数据
        self.repeat_model = "memory"
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
            if "customer" in model  and "pn"  in model:
                self.model = model
            else:
                #print("字典参数model必须有custom和pn key的，否则设为None") 
                pass
        
    def check(self,txt:str) -> (bool,str):
        '''校验输入的内容,如果未设置具体的model就遍历检查 '''
        ##print("检查器的model",self.model)
        if self.model:
            result = None
            for policy in self.policys:
                if self.model["customer"] == policy.name :
                    result = self.check_one(txt, policy,self.model)
                    if result[0] == SUCESS:
                        if not policy.repeatFlag :
                            #只有在规则定义无重复且之前条码验证ok时才验证重复性
                            #print("重复检查工作有进行")
                            return self.checkRepeat(txt)
                        return result
            else:
                return result

        for policy in self.policys:
            #print(f"正在匹配的规则{policy.name}")
            if not self.cfg.code_data.get(policy.name):
                ##print("此规则为没有对应的机型，进行下一个规则检查")
                result = self.check_one(txt,policy,{})     
                if result[0] == FAIL:
                    continue
                else:
                    return reuslt           
                
            res_content = [] #存储一半正确的结果
            for module, tmp  in self.cfg.code_data[policy.name].items():
                # #print("module,tmp",module,tmp)
                for name , pns in tmp.items():    
                    for pn in pns: 
                        model = {"customer":policy.name,"module":module,"name":name,"pn":pn}
                        result = self.check_one(txt,policy,model)  
                        if result[0] == SUCESS:
                            self.model = model
                            if not policy.repeatFlag :
                            #只有在规则定义无重复且之前条码验证ok时才验证重复性
                                #print("重复检查工作有进行")
                                return self.checkRepeat(txt)
                            return result
                        if result[0] == PARTIY_SUCESS:
                            res_content.append(result)
            if len(res_content)>0:
                #print("result_content:",res_content)
                return res_content[0]
        return FAIL,"没有匹配的规则"

    def check_one(self,txt,policy,model:dict) -> (bool,str):
        #按照给定的具体信息匹配验证
        if not len(model) == 0:
            policy.set_fixcode(model["pn"])
        return  policy.check(txt)


    def checkRepeat(self,code:str) ->(bool,str):
        '''获取资料中所有已存在的条码,检查此条码是否有重复'''
        if self.repeat_model == "memory":
            if not hasattr(self,"codes"):
                self.codes=set()#条码暂存容器验证重码
            if code in self.codes:
                return FAIL,"条码重复"
            else:
                self.codes.add(code)
                return SUCESS,""
        else :
            return FAIL,"暂未实现条码重复检查"

if __name__ == '__main__':
    b ={"customer":"ECS","pn":"123-456-78"}
    c = Checker()
    c.setMode(b)
    print(c.check("12345678"))
    # f =FixRule("4,ssss")
    # print(f.length)
    # d = DateRule("3,ydd")
    # print(d.check("92"))


