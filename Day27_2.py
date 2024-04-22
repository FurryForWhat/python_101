

def num_generator(num):
    counter = 0
    while counter < num:
        yield counter
        counter += 1

for i in num_generator(3):
    print(i)
    print(id(i))

# def my_generator(n):
#     value = 0
#     while value < n:
#         yield value
#         value += 1
        
# for value in my_generator(3):
#     print(value)