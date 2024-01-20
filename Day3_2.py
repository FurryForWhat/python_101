data_one= 'He said that "this value wasn\'t true'

print(data_one)
print(type(data_one))
data_two= data_one.upper()
print(data_two)
data_three = data_one.lower()
print(data_three)
print(data_two.isupper())
print(data_three.islower())

print(data_one.count('\''))
print(data_one.find('h'))
print(data_one.replace('a','z'))