from stack import *

class myQueue:
    push_stack = Stack()
    pop_stack = Stack()

    def push(self, value):
        self.push_stack.push(value)

    def pop(self):
        if self.pop_stack.top == None:
            self.shift_stacks()
            while self.push_stack.top != None:
                self.pop_stack(self.push_stack.pop())
        return self.pop_stack.pop()
    
    def shift_stacks(self):
        while self.push_stack.top != None:
            self.pop_stack.push(self.push_stack.pop())

    def print_queue(self):
        pop_arr = []
        push_arr = []

        current = self.push_stack.top
        while current != None:
            push_arr.append(current.value)
            current = current.next

        current = self.pop_stack.top
        while current != None:
            pop_arr.append(current.value)
            current = current.next

        print(f"\n \n \npush_arr: {push_arr} \npop_arr: {pop_arr}")
