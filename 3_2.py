import pytest
import random

class MinStack:
    class StackNode:
        nextNode = None
        min = float('inf')

        def __init__(self, value):
            self.value = value
        
    top = None
    
    def push(self, value):
        t = self.StackNode(value)
        t.next = self.top

        #check to see if this value is smaller than previous min
        if t.next == None:
            t.min = t.value
        else:
            if t.value < t.next.min:
                t.min = t.value
            else:
                t.min = t.next.min

        self.top = t

    def pop(self):
        if (self.top == None):
            raise StackEmptyError(f"can't pop an empty stack")     
        ret = self.top.value
        self.top = self.top.next
        return ret
    
    def peek(self):
        if(self.top == None):
            raise StackEmptyError(f"can't peek on an empty stack")   
        return self.top.value
    
    def print_stack(self):
        my_arr = []
        current_node = self.top
        while current_node != None:
            my_arr.append(current_node.value)
            current_node = current_node.next
        print(my_arr)

    def peek_min(self):
        if(self.top == None):
            raise StackEmptyError(f"can't get min of an empty stack")   
        return self.top.min

    
class StackError(Exception):
    """stack operation error"""


class StackEmptyError(StackError):
    """the stack is empty"""

