from stack import *

class myQueue:
    push_stack = Stack()
    pop_stack = Stack()

    def push(self, value):
        #transfer everything to the push stack an push next item
        while self.pop_stack.top != None:  
            self.push_stack.push(self.pop_stack.pop())
        self.push_stack.push(value) 


    def pop(self):
        while self.push_stack.top != None:
            self.pop_stack.push(self.push_stack.pop())

        return self.pop_stack.pop()
    
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



my_queue = myQueue()
 
for i in range(5):
    my_queue.push(i+1)

my_queue.print_queue()

print(my_queue.pop())
print(my_queue.pop())

my_queue.print_queue()

my_queue.push(6)
my_queue.push(7)
my_queue.print_queue()

my_queue.pop()
my_queue.pop()

my_queue.print_queue()