#!/usr/bin/env python
# -*-coding:utf-8 -*-
__author__ = 'whisky'
__date__ = '2019/3/17 15:17'


# !/usr/bin/python
# -*- coding: UTF-8 -*-


class Employee:
    '所有员工的基类asdasd'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print(        "Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print(        "Name : ", self.name, ", Salary: ", self.salary)


# print("Employee.__doc__:", Employee.__doc__)
# print("Employee.__name__:", Employee.__name__)
# print("Employee.__module__:", Employee.__module__)
# print("Employee.__bases__:", Employee.__bases__)
print("Employee.__dict__:", Employee.__dict__)
obj = Employee('ad', '1111111')
print("obj.__dict__:", obj.__dict__)
