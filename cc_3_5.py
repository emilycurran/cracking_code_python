from stack import *

def sort_stack(jumbled_stack):
    sorted_stack = Stack()
    sorted_stack.push(jumbled_stack.pop())

    while jumbled_stack.top != None:

        #item we're positioning on sorted stack
        temp = jumbled_stack.pop()

        if sorted_stack.top == None or temp <= sorted_stack.top.value:
            #if the item is less than everythin on sorted stack
            sorted_stack.push(temp)
        else:
            #our item does not fit on this index in the sorted stack,
            #push all items larger than our item onto jumbled stack
            #and then place our item

            current = sorted_stack.top
            while current.value != None and temp > current.value: 
                jumbled_stack.push(current.value)
                current = current.next
                sorted_stack.pop()
            
            sorted_stack.push(temp) #place temp in it's ordered place            
            
    return sorted_stack