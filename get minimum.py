# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 19:39:12 2019

@author: Raghav Chitkara
"""

class stack:
    def __init__(self):
        self.stk=[]
        self.limit=10
        #self.top=0
        
        
    def push(self,data):
        if len(self.stk)<self.limit:
            
            self.stk.append(data)
        else:
            print("stack overflow")
        
    def pop(self):
        
        if len(self.stk)>0:
            self.stk.pop()
        else:
            print("stack is empty")
    
    def top_element(self):
        if len(self.stk) >0:
            return self.stk[len(self.stk)-1]
        else:
            return None
    def length(self):
        return len(self.stk)
    
    def print_stack(self):
        print("stack : ", self.stk)
        return self.stk

def get_minimum(input_list):
    stack1=stack()
    for number in input_list:
        number=int(number)
        if stack1.length()==0:
            stack1.push(number)
        else:
            if number>stack1.top_element():
                stack1.push(stack1.top_element())
                
            else:
                stack1.push(number)
    stack1.print_stack()
    return stack1.top_element()
            

if __name__=="__main__":
    input_list=input("enter list comma separated")
    print(get_minimum(input_list.split(",")))
    