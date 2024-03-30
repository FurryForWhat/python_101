my_dict= {}
a = "Jan Winter\n"
my_data = a.split()
formation = my_data[1].replace('\n','')
my_dict.update({my_data[0] : formation})

print(my_dict)