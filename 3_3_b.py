class SetOfStack:
    stacks = []

    def __init__(self, capacity):
        self.capacity = capacity

    def get_last_stack(self):
        if len(self.stacks) == 0:
            return None
        return self.stacks[len(self.stacks) - 1]
    
    def push(self, value):
        last = self.get_last_stack()
        if (last != None and last.is_full() == False):
            last.push(value)
        else:
            stack = Stack(self.capacity)
            stack.push(value)
            self.stacks.append(stack)
    
    def pop_at(self, index):
        return self.left_shift(index, True)
    
    def left_shift(self, index, remove_top):
        stack = self.stacks[index]
        removed_item = None

        if remove_top:
            removed_item = stack.pop()
        else:
            removed_item = stack.removeBottom()

        if stack.isEmpty():
            self.stacks.remove(stack)
        elif len(self.stacks) > index + 1:
            print(f"len stacks: ({len(self.stacks)} current index: {index})")
            value = self.left_shift(index + 1, False)
            stack.push(value)

        return removed_item

    def print_stacks(self):
        for i in self.stacks:
            i.print_stack()


class Stack:
    size = 0
    top = None
    bottom = None
    
    def __init__(self, capacity):
        self.capacity = capacity

    def is_full(self):
        return self.capacity == self.size
    
    def join(self, above, below):
        if below != None:
            below.above = above
        if above != None:
            above.below = below

    def push(self, value):
        if self.size >= self.capacity:
            return False
        self.size += 1
        n = self.Node(value)
        if self.size == 1:
            self.bottom = n
        self.join(n ,self.top)
        self.top = n

        return True
    
    def pop(self):
        t = self.top
        self.top = self.top.below
        self.size -= 1
        return t.value
    
    def isEmpty(self):
        return self.size == 0
    
    def removeBottom(self):
        b = self.bottom
        self.bottom = self.bottom.above
        if self.bottom != None:
            self.bottom.below = None
        self.size -= 1
        return b.value
    
    def print_stack(self):
        current = self.top
        arr = []
        while current != None:
            arr.append(current.value)
            current = current.below

        print(arr)
            

    
    class Node:
        above = None
        below = None

        def __init__(self, value):
            self.value = value        


class StackError(Exception):
    """stack operation error"""


class StackEmptyError(StackError):
    """the stack is empty"""
