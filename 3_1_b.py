import pytest


class MultiStack:
    
    #stack info is a simple stack that holds a set of data about each stack. It does
    #not hold the actual items in the stack. We could have done this wiht just a bunch
    #of individual variables, but that's messy and doesn't gain us much.
    
    class StackInfo:    
        size = 0 

        def __init__(self, start, capacity):
            self.start = start
            self.capacity = capacity

        def is_within_stack_capacity(self, index):

            ####do stuff here
            return True
        
        def is_full(self):
            return self.capacity == self.size
        
        def is_empty(self):
            return self.size == 0
        
        def last_element_index(self):
            return self.start + self.size - 1
        
        
    info = []
    values = []

    def __init__(self, number_of_stacks, default_size):
        for i in range(number_of_stacks):
            self.info.append(self.StackInfo(default_size*i, default_size))
        self.values = [None]*(number_of_stacks*default_size)
    
    def push(self, stack_num, value):

        if not self.is_valid_stack(stack_num):
            raise StackDoesNotExistError(f"{stack_num} is not a valid stack")
        
        stack_info = self.info[stack_num]


        if self.all_stacks_full():
            raise StackFullError(f"Push failed: all stacks are full")
        
        if stack_info.is_full():
            self.shift_stack(  (stack_num + 1) %  len(self.info))
            stack_info.capacity += 1

        stack_info.size += 1
        self.values[self.index_of_top(stack_info)] = value

    def index_of_top(self, stack_info):
        return self.wrap_index(stack_info.last_element_index());

    def peek(self, stack_num):
        if not self.is_valid_stack(stack_num):
            raise StackDoesNotExistError(f"{stack_num} is not a valid stack")
        
        stack_info = self.info[stack_num]
        if stack_info.is_empty():
            raise StackEmptyError(f"stack #{stack_num}")
        return self.values[stack_info.last_element_index()]
    
    def pop(self, stack_num):
        if not self.is_valid_stack(stack_num):
            raise StackDoesNotExistError(f"{stack_num} is not a valid stack")
        
        stack_info = self.info[stack_num]
        if stack_info.is_empty():
            raise StackEmptyError(f"cannot peek at empty stack #{stack_num}.")
        
        ret = self.values[self.wrap_index(stack_info.last_element_index())]
        self.values[self.wrap_index(stack_info.last_element_index())] = None
        stack_info.size -= 1        

        return ret
    
    def all_stacks_full(self):
        for stack_info in self.info:
            if stack_info.is_full() == False:
                return False
        return True
    
    def wrap_index(self, index):
        return ( (index + len(self.values)) % len(self.values)) 
    
    def shift_stack(self, stack_num):
        stack_info = self.info[stack_num]

        if stack_info.is_full():
            self.shift_stack( (stack_num + 1) % len(self.info))
            stack_info.capacity += 1
        
        index = stack_info.last_element_index()
        for i in range(stack_info.size):
            self.values[self.wrap_index(index + 1)] = self.values[self.wrap_index(index)]
            index -= 1

        stack_info.start = self.wrap_index(stack_info.start + 1)
        stack_info.capacity -= 1

    def is_valid_stack(self, stack_num):
        if not isinstance(stack_num, int):
            return False
        if stack_num < 0 or stack_num >= len(self.info):
            return False
        return True
            
        


class MultiStackError(Exception):
    """multistack operation error"""


class StackFullError(MultiStackError):
    """the stack is full"""


class StackEmptyError(MultiStackError):
    """the stack is empty"""


class StackDoesNotExistError(ValueError):
    """stack does not exist"""
