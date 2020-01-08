# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 13:22:51 2019

@author: Raghav Chitkara
"""

def check_sorted(arr):
    if len(arr)==1:
        return True
    
    return arr[0]<arr[1] and check_sorted(arr[1:])
               
        
        
check_sorted([1,2,3,4,5,6]) 