class Dog:
    def __init__(self,name) :
        self.name = name  #attribute
    def sound(self): #method
        print(f'{self.name} barks')


Pupi = Dog('Pupi')
print('Dog\'s name is ',Pupi.name)
Pupi.sound()

Alice = Dog('Alice')
Alice.sound()