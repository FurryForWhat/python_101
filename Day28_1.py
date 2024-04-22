class Human:  #blueprint
   def __init__(self,name= None,age= None,gender= None,job= None) :
    self.name= name #attribute
    self.age = age
    self.gender = gender
    self.job = job

John = Human('John',12,'Male','staff')
print('My name is',John.name)
print('I\'m',John.age)
print('I\'m a',John.gender)
print("I am a",John.job)
print()
Mary = Human('Mary',21,'Female','doctor')
print('My name is',Mary.name)
print('I\'m',Mary.age)
print('I\'m a',Mary.gender)
print("I am a",Mary.job)
print()
Daisy = Human()
print('My name is',Daisy.name)
print('I\'m',Daisy.age)
print('I\'m a',Daisy.gender)
print("I am a",Daisy.job)