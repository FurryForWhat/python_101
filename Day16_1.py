def one():  
     return print('Hi')

def one(a):
     return a

def two(something ): #parameter
    return print(something)

def three(something):
     return print('Hello')


def a(b:int):
    if b < 0:
         return print('can\'t calculate')
    elif b == 0:
         return 1
    else:
        result = 1
        for i in range(2,b+1):
              result *= i
        return result
         
finalData = a(8) 
print(finalData)

# a = 12
# a = 13 #data overwriting
# print(a)