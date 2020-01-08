# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 19:05:05 2019

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

def postfix_eval(postfix_expr):
    stack1=stack()
    for element in postfix_expr:
        if element in "0123456789":
            element=int(element)
            stack1.push(element)
            stack1.print_stack()
        else:
            if element=="+":
                a=stack1.top_element()
                stack1.pop()
                b=stack1.top_element()
                stack1.pop()
                stack1.push(b+a)
                stack1.print_stack()
            if element=="-":
                a=stack1.top_element()
                stack1.pop()
                b=stack1.top_element()
                stack1.pop()
                stack1.push(b-a)
                stack1.print_stack()
            if element=="*":
                a=stack1.top_element()
                print(a)
                stack1.pop()
                b=stack1.top_element()
                print(b)
                stack1.pop()
                stack1.push(b*a)
                stack1.print_stack()
            if element=="/":
                a=stack1.top_element()
                stack1.pop()
                b=stack1.top_element()
                stack1.pop()
                stack1.push(b/a)
                stack1.print_stack()
    print("stack final", stack1.print_stack())
                
if __name__=="__main__":
    postfix_expr=input("enter expression")
    postfix_eval(postfix_expr)
    