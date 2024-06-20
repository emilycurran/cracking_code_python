from queue import *

class Animal:
    __ord = 0

    def __init__(self, name, is_dog):
        self.name = name
        self.is_dog = is_dog

    def get_order(self):
        return self.__ord
    
    def set_order(self, value):
        self.__ord = value
    
class AnimalWrapper:
    dogs = Queue()
    cats = Queue()
    order = 0

    def enqueu(self, name, is_dog):
        new_animal = Animal(name, is_dog)
        self.set_order(new_animal)

        if is_dog:
            self.dogs.add(new_animal)
        else:
            self.cats.add(new_animal)
    
    def set_order(self, animal):
        animal.set_order(self.order)
        self.order += 1

    def dequeue_cat(self):
        return self.cats.remove()
    
    def dequeue_dog(self):
        return self.dogs.remove()
    
    def dequeue_any(self):
        if self.cats.is_empty():
            return self.dogs.remove()
        elif self.dogs.is_empty():
            return self.cats.remove()
        else:
            if self.cats.peek().get_order() < self.dogs.peek().get_order():
                return self.cats.remove()
            else:
                return self.dogs.remove()    

my_shelter = AnimalWrapper()