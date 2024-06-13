import pytest


class MultiStack:
    """Creates three seperate stacks on the array and includes
    methods for manipulating them. Does this by holding an array
    which keeps track of the index of the top item of each stack."""

    def __init__(self, default_size, number_of_stacks):
        self.default_size = default_size
        self.number_of_stacks = number_of_stacks
        self.last_indices = [None] * number_of_stacks
        self.values = [None]    *   (default_size*number_of_stacks)

    def push(self, stack_num, value):
        if not self.is_valid_stack(stack_num):
            raise StackDoesNotExistError(f"stack {stack_num} does not exists")

        if self.is_full(stack_num):
            raise StackEmptyError(f"can't push to full stack # {stack_num}")
        
        if self.is_empty(stack_num):
            self.last_indices[stack_num] = self.default_size*stack_num
            self.values[self.last_indices[stack_num]] = value
        else:
            self.values[self.last_indices[stack_num] + 1] = value
            self.last_indices[stack_num] += 1

    def peek(self, stack_num):
        if self.is_empty(stack_num):
            raise StackEmptyError(f"can't peek on empty stack #{stack_num}")
        
        return self.values[self.last_indices[stack_num]]
    
    def pop(self, stack_num):
        if self.is_empty(stack_num):
            raise StackEmptyError(f"can't peek on empty stack #{stack_num}")
        
        ret = self.values[self.last_indices[stack_num]] #store value

        self.values[self.last_indices[stack_num]] = None #free space

        if self.last_indices[stack_num] == self.default_size*stack_num:
            self.last_indices[stack_num] = None #remove last element index if no such element exists
        else: 
            self.last_indices[stack_num] -= 1 

        return ret

    def is_full(self, stack_num):
        return self.last_indices[stack_num] == ( (self.default_size * (stack_num+1)) - 1)
    
    def is_empty(self, stack_num):
        return self.last_indices[stack_num] == None
    
    def is_valid_stack(self, stack_num):
        if isinstance(stack_num, int) and 0 <= stack_num < self.number_of_stacks:
            return True
        return False

class MultiStackError(Exception):
    """multistack operation error"""


class StackFullError(MultiStackError):
    """the stack is full"""


class StackEmptyError(MultiStackError):
    """the stack is empty"""


class StackDoesNotExistError(ValueError):
    """stack does not exist"""

my_stack = MultiStack(3,3)