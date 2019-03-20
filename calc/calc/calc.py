# -*- coding: utf-8 -*-
from functools import reduce
class Calc:
    def add(self, *args):
        return sum(args)
    def sub(self, a, b):
        return a - b
    def mult(self, *args):
        # def mult2(a, b):
            # return a * b
        # return reduce(mult2, args)
        if not all(args):
            raise ValueError
        return reduce(lambda x, y: x*y, args)
    def div(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "inf"

    def avg(self, it, ut=None, lt=None):

        if ut is not None:
            it = [x for x in it if x <= ut]
        if lt is not None:
            it = [x for x in it if lt <= x]
        if not len(it):
            return 0
        return sum(it) / len(it)