my_num_list= []
my_num_odd= []
total_prime_number = 0

for i in range(100):
    my_num_list[i]= i+1

for j in range(100):
    if my_num_list[j] % 2 != 0:
        my_num_odd.append(my_num_list[j])

print(my_num_odd)
print(len(my_num_odd))