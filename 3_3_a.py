from stack import *

class StackOfPlates:
    """using a linked list of a stack to store other linked list
    stacks"""

    top = None
    size = 0

    def __init__(self, max_size):
        self.my_plate_stacks = Stack() #holds the stacks of plates
        self.max_size = max_size

    def push(self, value):
        if self.top == None or self.top.size == self.max_size:
            #create a new empty stack and push it on stack of plates
            new_stack = Stack()
            new_stack.push(value)
            new_stack.size = 1
            self.size += 1
            new_stack.next = self.top
            self.top = new_stack
            self.my_plate_stacks.push(new_stack)

        else:
            #push value to existing stack
            self.top.size += 1
            self.top.push(value)

    def pop(self):   
        if self.top.size == 0:
            self.top = self.top.next

        if self.top == None:
            raise StackEmptyError(f"can't pop an empty stack")    

        self.top.size -= 1
        return self.top.pop()
    
    def pop_at_index(self, index):
        current_node = self.top

        while index <= self.size:
            if self.size - 1 == index:
                current_node.size -= 1
                return current_node.pop()
            else:
                index += 1
                current_node = current_node.next

    def re_organise_plates(self):
        #rearranges plates into stacks of max_size, leaving the total plates % max_size
        #at the bottom of the stack

        self.remove_empty_stacks()    
        self.print_plates()

        current_node = self.top
        while current_node.next != None:
            current_plate = current_node.top
            while current_plate.next != None:
                current_plate = current_plate.next

            current_plate.next = current_node.next.top

            mem_next = current_node.next.next
            current_node = self._split_stack(current_node)
            current_node.next = mem_next
        self._split_stack(current_node)
        
        self.size = 0
        while current_node != None:
            self.size += 1
            current_node = current_node.next

    def remove_empty_stacks(self):

        while self.top.top == None: #remove leading empty stacks
            self.top = self.top.next

        #have a non-empty stack at the start so delete all subsequent empty stacks

        previous = self.top
        current = previous.next

        while current.next != None:
            current.print_stack()
            if current.top != None:
                previous.next = current
                previous = current
            current = current.next
        
        #check if last slot is empty
        if current.top == None:
            previous.next = None



    def _split_stack(self, stack):
        #split this stack, if there is excess create a new stack and return the excess as a new
        #stack, if the same size, return the next node and if it is too small return the stack

        current_plate = stack.top
        count = 1

        while count < self.max_size and current_plate.next != None:
            current_plate = current_plate.next
            count += 1 


        if current_plate.next == None:
            if count < self.max_size: #stack smaller than max_size
                stack.size = count
                return stack
            else:
                stack.size = count
                return stack #stack equal to max_size
        else:
            #stack greater than max_size
            excess_stack_top = current_plate.next
            current_plate.next = None
            excess_stack = Stack()
            excess_stack.top = excess_stack_top
            stack.next = excess_stack
            stack.size = self.max_size
            return excess_stack        
                    
            
    def print_plates(self):
        current_node = self.top
        while current_node != None:
            current_node.print_stack()
            current_node = current_node.next

        print('\n')

my_plates = StackOfPlates(5)

for i in range(40):
    my_plates.push(i+1)

for i in range(3):
    my_plates.pop_at_index(0)
    my_plates.pop_at_index(2)
    my_plates.pop_at_index(7)

for i in range(5):
    my_plates.pop_at_index(3)
    my_plates.pop_at_index(4)

my_plates.re_organise_plates()


my_plates.print_plates()

my_plates.pop()

my_plates.print_plates()
my_plates.pop_at_index(1)





class StackError(Exception):
    """stack operation error"""


class StackEmptyError(StackError):
    """the stack is empty"""
