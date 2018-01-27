#!/usr/bin/python3

import random
import re

INF = 1000000.0


class Unit_Template:
    def __init__(self, lower_bound, upper_bound=-INF, type='uniform', *args):
        self.lower_bound = lower_bound
        if (upper_bound == -INF):
            self.upper_bound = lower_bound
        else:
            self.upper_bound = upper_bound
        if (self.upper_bound < self.lower_bound):
            self.able = False
        else:
            self.able = True
        if isinstance(self.upper_bound, float) & isinstance(self.lower_bound, float):
            self.able = True
        else:
            self.able = False
        self.type = type
        self.mu = (lower_bound + upper_bound) / 2
        self.args = args

    def gauss(self):
        return random.gauss(self.mu, self.args[0])

    def uniform(self):
        return random.uniform(self.lower_bound, self.upper_bound)

    def distribute(self):
        if (self.able == False):
            return -INF
        func = getattr(self, self.type)
        a = func()
        while ((a > self.upper_bound) or (a < self.lower_bound)):
            a = func()
        return a

class Series_Template:
    def __init__(self,ptn):
        class RangeExcept(Exception):
            def __init__(self, args):
                self.args = args
        rule1 = r'(\d+)'
        rule2 = r'(\[(\d+)\,(\d+)\]([A-Z])\((\d+)\))'
        rule3 = r'(\[(\d+)\,(\d+)\])'
        result = []
        curBound = -INF
        try:
            while ptn:
                ptrn = re.match(r'(' + rule1 + r'|' + rule2 + r'|' + rule3 + r')', ptn).group(0)
                ptn = ptn[len(ptrn) + 1:]
                if re.match(rule1, ptrn):
                    lower_bound = float(re.search(rule1, ptrn).group(0))
                    if curBound > lower_bound:
                        raise RangeExcept("重叠！")
                    else:
                        curBound = lower_bound
                    a = Unit_Template(lower_bound)
                    result.append(a)
                elif re.match(rule2, ptrn):
                    lower_bound = float(re.search(rule2, ptrn).group(2))
                    upper_bound = float(re.search(rule2, ptrn).group(3))
                    if (curBound > lower_bound) | (lower_bound > upper_bound):
                        raise RangeExcept("重叠！")
                    else:
                        curBound = lower_bound
                    typ = re.search(rule2, ptrn).group(4)
                    arg = float(re.search(rule2, ptrn).group(5))
                    a = Unit_Template(lower_bound, upper_bound, "gauss", arg)
                    result.append(a)
                elif re.match(rule3, ptrn):
                    lower_bound = float(re.search(rule3, ptrn).group(2))
                    upper_bound = float(re.search(rule3, ptrn).group(3))
                    if (curBound > lower_bound) | (lower_bound > upper_bound):
                        raise RangeExcept("重叠！")
                    else:
                        curBound = lower_bound
                    a = Unit_Template(lower_bound, upper_bound)
                    result.append(a)
        except RangeExcept:
            result = []
            print("范围重叠！")
            self.seires=None
        self.series=result
    def distribute(self):
        result=[]
        for a in self.series:
            result.append(a.distribute())
        return result


if __name__ == '__main__':
    ptn = input("Please enter a pattern: ")
    a = Series_Template(ptn)
    print(a.distribute())
    print(a.distribute())
    print(a.distribute())
    print(a.distribute())
