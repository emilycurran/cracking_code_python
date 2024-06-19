class Queue:
    first = None
    last = None

    class Node:
        next = None

        def __init__(self, value):
            self.value = value

    def add(self,value):
        t = self.Node(value)

        if self.last != None:
            self.last.next = t 
            self.last = t
        
        if self.first == None:
            self.first = self.last

        self.last = t

    def remove(self):
        if self.last == None:
            raise EmptyQueueException(f"can't pop an empty queue!")
        
        ret = self.first.value
        
        self.first = self.first.next
        if self.first == None:
            self.last = None

        return ret
    
    def peek(self):
        if self.last == None:
            raise EmptyQueueException(f"can't pop an empty queue")
        return self.first.value
    
    def isEmpty(self):
        return self.first == None
    
    def print_queue(self):
        my_arr = []
        current = self.first
        while current != None:
            my_arr.append(current.value)
            current = current.next

        print(my_arr)
                
class QueueError(Exception):
    """Queue Error Exception"""

class EmptyQueueException(QueueError):
    """the queue is empty"""

