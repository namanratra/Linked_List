#Naman Ratra
#Linked List Assignment
from time import perf_counter

class Node: #class for each element of the linked list
    def __init__(self,data=None):
        self.data=data
        self.next=None
       
class Linked_list: #class for operations of a linked list
    
    def __init__(self):
        self.head = Node()
       
    def append(self,data): #append new values in the list
        new_node = Node(data)
        curr = self.head
        while curr.next!=None:
            curr = curr.next
        curr.next = new_node
       
    def length(self): #calculate the length of the linked list
        curr = self.head
        total = 0
        while curr.next!=None:
            total = total+1
            curr = curr.next
        return total
   
    def display(self): #display the result
        elems = []
        curr_node = self.head
        while curr_node.next!=None:
            curr_node = curr_node.next
            elems.append(curr_node.data)
        print(elems)
       
    def get(self,index): #get function to get the data at any given index
        if index>=self.length():
            print('Index is out of range')
            return None
        curr_index=0
        curr_node=self.head
        while True:
            curr_node=curr_node.next
            if curr_index==index:return curr_node.data
            curr_index = curr_index+1
           
    def insert_and_return_timetaken(self,index,data_): #Insert fuction which also returns the time taken in the insertion process
        list_length = self.length()
        if index >= list_length:
            print('Index out of Range')
            return None
        curr_index = 0
        curr_node = self.head
        new_node = Node(data=data_)
        while curr_index <= list_length:
            new_next_node = curr_node.next.next
            curr_node = curr_node.next
            if curr_index == index:
                time1 = perf_counter()
                curr_node.next = new_node
                new_node.next = new_next_node
                time2 = perf_counter()
            curr_index = curr_index+1
        return time2 - time1

#Time Complexity
import random
Result_Time = []
LL_len = [1000, 2000, 4000, 8000, 16000, 32000]
for j in range(0,6):
    Linked_Lst = []
    Linked_Lst = Linked_list()
    for i in range(0,LL_len[j]):
        n = random.randint(1,50000)
        Linked_Lst.append(n)
    p = Linked_Lst.insert_and_return_timetaken(random.randint(1,Linked_Lst.length()-1),1) #Insertion of number 1 at a random place in the list
    Result_Time.append(p)
print('Time taken for insertion for different lengths of lists', Result_Time)

import matplotlib.pyplot as plt #plot for time complexity of insertion

plt.plot(LL_len, Result_Time)
plt.xlabel('Number of Elements in List')
plt.ylabel('Time Taken for Insertion')
plt.title('Time Complexity for Insertion in a linked list')
plt.show()
#Time taken to insert a single element, is similar for all the lists of any given length, hence time complexity is constant for insertion in linked lists

