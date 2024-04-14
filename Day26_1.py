def outer_function():
    def inner_function():
        x = 1
        print(x)
        
    return inner_function


inner_obj = outer_function()
print(inner_obj())