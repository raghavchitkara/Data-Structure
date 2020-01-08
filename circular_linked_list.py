# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 08:50:18 2019

@author: Raghav Chitkara
"""

class Node():
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
    
    def set_data(self,data):
        self.data=data
        
    def get_data(self):
        print("data", self.data)
        return self.data
    
    def set_next(self,next):
        self.next=next
        
    def get_next(self):
        #print("next : ", self.next)
        return self.next
    def has_next(self):
        return self.next!=None
    
class LinkedList():
    def __init__(self,head=None):
        self.head=head
        self.length=0
        
    def insert_begin(self,data):
        new_node=Node()
        new_node.set_data(data)
        new_node.get_data()
        if self.length==0:
            self.head=new_node
            new_node.set_next(self.head)
            self.length+=1
            print("new_node", new_node)
        else:
            current=self.head
            print("current_head:",current)
            while current.get_next()!=self.head:
                current=current.get_next()
            current.set_next(new_node)
            new_node.set_next(self.head)
            self.head=new_node
            print("current_get_next ",current.get_next())
            print("new_node ", self.head)
            print("next_node:",self.head.get_next())
            self.length+=1
            
    def insert_end(self,data):
        new_node=Node()
        new_node.set_data(data)
        new_node.get_data()
        current=self.head
        print("current_head:",current)
        while current.get_next()!=self.head:
            current=current.get_next()
            
        current.set_next(new_node)
        print("current_get_next ",current.get_next())
        new_node.set_next(self.head)
        print("head :", self.head)
        print("head :", new_node.get_next())
        self.length+=1
        
    def print_list(self):
        current=self.head
        current.get_data()
        while current.get_next()!=self.head:
            
            current=current.get_next()
            current.get_data()
            
    def delete_from_beg(self):
        current=self.head
        #current.get_data()
        while current.get_next()!=self.head:
            
            current=current.get_next()
            #current.get_data()
        current.set_next(self.head.get_next())
        self.head=self.head.get_next()
        self.length-=1
    
    def delete_from_end(self):
        previous=self.head
        current=self.head
        #current.get_data()
        while current.get_next()!=self.head:
            
            previous=current
            current=current.get_next()
            #current.get_data()
        previous.set_next(self.head)
        self.length-=1
        
    
if __name__=="__main__":
    llist=LinkedList()
    llist.insert_begin(10)
    llist.insert_begin(11)     
    llist.insert_end(12)
    llist.insert_end(13)
    llist.insert_end(14)
    llist.insert_end(15)
    llist.print_list()
    llist.delete_from_beg()
    llist.delete_from_end()
    llist.print_list()