# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 15:10:10 2019

@author: Raghav Chitkara
"""

def insert_in_beg(x,l):
    print("list",l)
    for element in l:
        element=x+element
    print("list",l)
    return l
def bit_strings(n):
    if n==0:
        return []
    if n==1:
        return ["0","1"]
    return insert_in_beg("0",bit_strings(n-1))+insert_in_beg("1",bit_strings(n-1))
bit_strings(2)
    