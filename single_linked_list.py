

#implementing linked list in pythton

class Node() :

    def __init__(self):
        self.data=None
        self.next=None

    def set_data(self, data):
        self.data=data

    def get_data(self):
        print(self.data)
        return self.data

    def set_next( self, next):
        self.next=next

    def get_next( self):
        print("next: ",self.next)
        return self.next

    def has_next(self):
        return self.next!=None


class LinkedList() :

    def __init__(self,head=None):
        self.head= head
        self.length=0

    def insert_begin(self, data):
        new_node=Node()
        new_node.set_data(data)
        new_node.get_data()
        new_node.set_next(self.head)
        #new_node.get_next()
        self.head=new_node
        print("head: ",self.head)
        self.length+=1
        print("length : ", self.length)
    def insert_end( self, data):
        new_node=Node()
        new_node.set_data(data)
        new_node.get_data()
        current=self.head
        print("current_head:",current)
        while current.get_next()!=None:
            current=current.get_next()
        print("current : ", current)
        current.set_next(new_node)
        print("current_new : ", current.get_next())
        self.length+=1
        print("length : ", self.length)
        print(new_node.get_next())
     
    def insert_in_mid(self,data,pos):
        new_node=Node()
        new_node.set_data(data)
        new_node.get_data()
        current=self.head
        print("current_head:",current)
        pos_temp=1
        while pos_temp<pos-1 :
            current=current.get_next()
            pos_temp+=1
        print("current : ", current)

       
        new_node.set_next(current.get_next())
        print("new_node : " ,new_node.get_next())
        current.set_next(new_node)
        print("current_new : ", current)

        self.length+=1
        print("length : ", self.length)
        
    def print_list(self):
        temp=self.head
        while temp!=None:
            print(temp.data)
            temp=temp.next
    
    def delete_from_beg(self):
        if self.length==0:
            print("The list is empty")
        else:
            
            self.head=self.head.get_next()
            self.length-=1
            
    def delete_from_end(self):
        prev=self.head
        current=self.head
         
        while current.get_next()!=None:
            prev=current
            current=current.get_next()
        prev.set_next(None)
        self.length-=1
        
    def delete_from_mid(self,number):
        if number>self.length:
            raise ValueError("number not in list")
        if self.length==0:
            raise ValueError("length is zero")
        
        prev=self.head
        current=self.head
        temp_num=1
        print("delete_from_mid: ")
        #print("prev")
        
        while temp_num<=number-1:
            
            prev=current
            current=current.get_next()
            temp_num+=1
        prev.set_next(current.get_next())
        self.length-=1
    
    def delete_value(self,value):
         
        found=False
        previous=self.head
        current=self.head
        while current.get_next()!=None :
            if current.get_data()==value:
                found=True
                break
            else:
                previous=current
                current=current.get_next()
        previous.set_next(current.get_next())
        self.length-=1
        if not found:
            print("{} not in list".format(value))
        
if __name__=="__main__":

    llist=LinkedList()
    llist.insert_begin(10)
    llist.insert_begin(11)
    llist.insert_end(12)
    llist.insert_end(13)
    llist.insert_end(14)
    llist.insert_in_mid(15,3)
    llist.insert_in_mid(18,5)
    #llist.delete_from_beg()
    #llist.delete_from_end()
    #llist.insert_begin(20)
    #llist.insert_end(21)
    #llist.insert_in_mid(22,5)
    #llist.delete_from_end()
    #llist.delete_from_mid(2)
    #llist.delete_value(25)
    
    llist.print_list()
        
        


