import pytest

class Stack:
    class StackNode:
        value = None
        nextNode = None

        def __init__(self, value):
            self.value = value
        
    top = None
    
    def push(self, value):
        t = self.StackNode(value)
        t.next = self.top
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
    
class StackError(Exception):
    """stack operation error"""


class StackEmptyError(StackError):
    """the stack is empty"""


my_stack = Stack()

