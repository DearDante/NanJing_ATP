#!/usr/bin/python3

import random
import re

INF = 1000000.0


class Unit_Template:
    def __init__(self, lower_bound=-INF, upper_bound=-INF, type='uniform', *args):
        self.lower_bound = lower_bound
        self.able=True
        if(lower_bound == -INF):
            self.able=False
            return
        if (upper_bound == -INF):
            self.upper_bound = lower_bound
        else:
            self.upper_bound = upper_bound
        if (self.upper_bound < self.lower_bound):
            self.error = "上界小于下界"
            self.able=False
        self.type = type
        self.mu = (lower_bound + upper_bound) / 2
        self.args = args

    def gauss(self):
        return random.gauss(self.mu, self.args[0])

    def uniform(self):
        return random.uniform(self.lower_bound, self.upper_bound)

    def distribute(self):
        if (self.able == False):
            return None
        func = getattr(self, self.type)
        a = func()
        while ((a > self.upper_bound) or (a < self.lower_bound)):
            a = func()
        return a

class Series_Template:
    def __init__(self,ptn=""):
        class MyException(Exception):
            def __init__(self, args):
                self.args = args
        rule1 = r'(\d+)'
        rule2 = r'(\[(\d+)\,(\d+)\]([A-Z])\((\d+)\))'
        rule3 = r'(\[(\d+)\,(\d+)\])'
        result = []
        curBound = -INF
        try:
            while ptn:
                temp = re.match(r'(' + rule1 + r'|' + rule2 + r'|' + rule3 + r')', ptn)
                a=Unit_Template
                if(temp):
                    ptrn=temp.group(0)
                else:
                    raise MyException("语法错误")
                ptn = ptn[len(ptrn):]
                if re.match(rule1, ptrn):
                    lower_bound = float(re.search(rule1, ptrn).group(0))
                    if curBound > lower_bound:
                        raise MyException("区间重叠")
                    else:
                        curBound = lower_bound
                    a = Unit_Template(lower_bound)
                    result.append(a)
                elif re.match(rule2, ptrn):
                    lower_bound = float(re.search(rule2, ptrn).group(2))
                    upper_bound = float(re.search(rule2, ptrn).group(3))
                    if (curBound > lower_bound) or (curBound > upper_bound):
                        raise MyException("区间重叠")
                    else:
                        curBound = upper_bound
                    typ = re.search(rule2, ptrn).group(4)
                    arg = float(re.search(rule2, ptrn).group(5))
                    a = Unit_Template(lower_bound, upper_bound, "gauss", arg)
                    result.append(a)
                elif re.match(rule3, ptrn):
                    lower_bound = float(re.search(rule3, ptrn).group(2))
                    upper_bound = float(re.search(rule3, ptrn).group(3))
                    if (curBound > lower_bound) or (curBound > upper_bound):
                        raise MyException("区间重叠")
                    else:
                        curBound = upper_bound
                    a = Unit_Template(lower_bound, upper_bound)
                    result.append(a)
                if(ptn)and(ptn[0]==','):
                    ptn = ptn[1:]
                if(hasattr(a, "error")):
                    raise MyException(a.error)
        except MyException as e:
            self.error= e.args
            result=[]
        self.series=result
    def distribute(self):
        result=[]
        for a in self.series:
            result.append(a.distribute())
        return result
    def ATP_dis(self):
        result=[]
        flag=True
        ta=0
        for a in self.series:
            flag = not flag
            if(flag):
                result.append([ta,a.distribute()])
            else:
                ta=a.distribute()
        if(len(self.series)%2):
            result.append(ta)
        return result


if __name__ == '__main__':
    ptn = input("Please enter a pattern: ")
    a = Series_Template(ptn)
    if (hasattr(a, "error")):
        print(a.error)
    print(a.distribute())
    print(a.distribute())
    print(a.ATP_dis())
    print(a.ATP_dis())
