# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 17:00:57 2019

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


def infix_to_postfix(expression):
    
    prec={}
    prec["*"]=3
    prec["/"]=3
    prec["+"]=2
    prec["-"]=2
    prec["("]=1
    
    stack1= stack()
    postfix_exp=""
    for element in expression:
        if element in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
            postfix_exp=postfix_exp +element
            print("postfix_exp",postfix_exp)
            
        elif element in "()":
            if element=="(":
                stack1.push(element)
                stack1.print_stack()
                
            elif element==")":
                while stack1.top_element() !="(":
                    postfix_exp=postfix_exp +stack1.top_element()
                    print("postfix_exp",postfix_exp)
                    stack1.pop()
                    stack1.print_stack() 
                stack1.pop()
                stack1.print_stack() 
        elif element in "+*-/":
            if stack1.length()==0:
                stack1.push(element)
                stack1.print_stack()
            
            else :
                if prec[element]> prec[stack1.top_element()]:
                    stack1.push(element)
                    stack1.print_stack()
                    
                else:
                    postfix_exp=postfix_exp + stack1.top_element()
                    print("postfix_exp",postfix_exp)
                    stack1.pop()
                    stack1.push(element)
                    stack1.print_stack()
                        
    
    while stack1.length()!=0:
        postfix_exp=postfix_exp + stack1.top_element()
        print("postfix_exp",postfix_exp)
        stack1.pop()
    print(postfix_exp)  
    return postfix_exp
        

if __name__=="__main__":
    infix_exp="A*B-(C+D)+E"
    infix_to_postfix(infix_exp)
    
                        
                
    
    
    
    
    
    
    
    
    
    