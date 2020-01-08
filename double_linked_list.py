# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 20:45:00 2019

@author: Raghav Chitkara
"""

class Node():
    
    def __init__(self, data=None,prev=None,next=None):
        self.data=data
        self.prev=prev
        self.next=next
    
    def set_data(self,data):
        self.data=data
    
    def get_data(self):
        print("data : ",self.data)
        return self.data
    
    def set_next(self,next):
        self.next=next
        
    def get_next(self):
        print("next : ",next)
        return self.next
    
    def has_next(self):
        return self.next!=None
    
    def set_prev(self,prev):
        self.prev=prev
        
    def get_prev(self):
        print("prev : ", prev)
        return self.prev
    
    def has_prev(self):
        return self.prev!=None
    
    
class LinkedList():
    def __init__(self,head=None):
        self.head=head
        self.length=0
        
    def insert_begin(self,data):
       if self.length==0:
            new_node=Node()
            new_node.set_data(data)
            new_node.get_data()
            new_node.set_prev(None)
            new_node.set_next(None)
            self.head=new_node
            self.length+=1
            
       else:
           
           new_node=Node()
           new_node.set_data(data)
           new_node.get_data()
           new_node.set_prev(None)
           print("head : ",self.head)
           new_node.set_next(self.head)
           self.head.set_prev(new_node)
           self.head=new_node
           print("head : ",self.head)
           self.length+=1
    
    def insert_end(self,data):
        new_node=Node()
        new_node.set_data(data)
        new_node.get_data()
        current=self.head
        print("current_head:",current)
        while current.get_next()!=None:
            current=current.get_next()
        print("current : ", current)
        new_node.set_prev(current)
        new_node.set_next(None)
        current.set_next(new_node)
        print("current_new : ", current.get_next())
        self.length+=1
         
    def insert_mid(self,data,pos):
        new_node=Node()
        new_node.set_data(data)
        new_node.get_data()
        current=self.head
        temp_pos=1
        while temp_pos<pos-1:
            current=current.get_next()
            temp_pos+=1
            
        new_node.set_next(current.get_next())
        new_node.set_prev(current)
        current.set_next(new_node)
        self.length+=1
        
        
    def print_list(self):
        temp=self.head
        while temp!=None:
            print(temp.data)
            temp=temp.next

if __name__=="__main__":
    llist=LinkedList()
    llist.insert_begin(10)
    llist.insert_begin(12)
    llist.insert_end(13)
    llist.insert_end(14)
    llist.insert_mid(20,3)
    llist.print_list()
    
     
    