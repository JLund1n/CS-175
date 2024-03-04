#----------------------------------------------------
# Stack implementation #2 
# (Top of stack corresponds to back of list)
# 
# Author: CMPUT 175 team
# Updated by:
#----------------------------------------------------

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    
    def pop(self):       
        if len(self.items) == 0: #Checks to see if the stack is empty
            raise Exception('Stack Empty') #If the stack is empty raise an exception
        return self.items.pop() #Pop an item from the stack
    
    
    def peek(self):      
        if len(self.items) == 0: #Checks to see if the stack is empty
            raise Exception('Stack Empty') #If the stack is empty raise an exception
        return self.items[len(self.items) - 1] #Returns the last item added to the stack
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
    def show(self):
        print(self.items)
    
    def __str__(self):
        stackAsString = ''
        for item in self.items:
            stackAsString += item + ' '
        return stackAsString
    
    def clear(self):
        self.items.clear() #Clears the stack