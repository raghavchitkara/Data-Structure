# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 14:53:09 2019

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
        
if __name__=="__main__":
    output_stack= stack()

    string_unbal= input("enter string : > ")
    #string_unbal="(A+B)"
    for element in string_unbal:
        
        if element in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+-*/":
            pass
        else:
            if element in "{[(":
                output_stack.push(element)
                
            elif element in ")}]":
                output_stack.print_stack()
                top_symbol=output_stack.top_element()
                print(top_symbol)
                print("element ",element)
                if (top_symbol=="(" and element==")") or (top_symbol=="{" and element=="}") or (top_symbol=="[" and element=="]"):
                    output_stack.pop()
                    print("popped")
                else:
                    
                    print("expression is unbalanced")
                    break
                    
    if output_stack.length()==0:
        print("expression is balanced")
        
    else:
        print("expression is unbalanced")