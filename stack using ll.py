# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 09:01:18 2019

@author: Raghav Chitkara
"""

class Node:
    def __init__(self):
        self.data=None
        self.next=None
        
    def set_data(self,data):
        self.data=data
        
    def get_data (self):
        print("get_data ",self.data)
        return self.data
    
    def set_next(self,next):
        self.next=next
        
    def get_next (self):
        print("get_next ",self.next)
        return self.next
    
class stack:
    
    