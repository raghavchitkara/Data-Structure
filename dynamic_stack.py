# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 08:48:06 2019

@author: Raghav Chitkara
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 08:29:45 2019

@author: Raghav Chitkara
"""

class stack :
    def __init__(self):
        self.stack=[]
        self.limit=2
        
    def push(self,data):
        if len(self.stack)<self.limit:
            self.stack.append(data)
            print("size ",self.size_stack())
        else:
            self.resize_stack()
            print("stack now expaned _now limit = ",self.limit)
            self.stack.append(data)
            print("size ",self.size_stack())
            
    def pop(self):
        if len(self.stack)>0:
            #del self.stack[len(self.stack)-1]
            self.stack.pop()
        else:
            print("stack is empty")    
    def top(self):
        if len(self.stack)>0:
            print(self.stack[len(self.stack)-1])
            return self.stack[len(self.stack)-1]
        else:
            print("stack is empty") 
            
    def print_stack(self):
        print("stack : ", self.stack)
           
    def size_stack(self):
        #print(len(self.stack))
        return len(self.stack)
    def resize_stack(self):
        #new_stack=self.stack
        self.limit=2*self.limit
        
if __name__=="__main__":
    stack1= stack()
    stack1.print_stack()
    stack1.push(5)
    stack1.push(6)
    stack1.push(7)
    stack1.push(8)
    stack1.push(9)
    stack1.push(11)
    stack1.print_stack()
    stack1.pop()
    stack1.pop()
    stack1.pop()
    stack1.pop()
    stack1.print_stack()
    stack1.pop()
    stack1.print_stack()
    stack1.pop()
    stack1.pop()
    stack2= stack()
    stack2.print_stack()
    stack2.push(5)
    stack2.push(6)
    stack2.push(7)
    stack2.push(8)
    stack2.push(9)
    stack2.print_stack()
    stack2.top()