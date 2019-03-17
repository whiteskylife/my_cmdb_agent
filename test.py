#!/usr/bin/env python
# -*-coding:utf-8 -*-
__author__ = 'whisky'
__date__ = '2019/3/17 15:07'



class Foo(object):
    def __init__(self, hostname):
        self.hostname1 = hostname

class Foo2(object):
    def __init__(self, hostname):
        self.hostname = hostname + '2222222222222222'


class Middle(Foo,Foo2):
    def hi(self):
        print('hi')


class Whi(Foo,Foo2):
    def test(self):
        print('test---------')


obj = Whi('whisky home')
print(obj.hostname)
print(obj.__dict__)


