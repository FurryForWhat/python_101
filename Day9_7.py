def min_store(item,amount):
    store_item = ['candy', 3,'liquior',350, 'ciggarte',40, 'apple',80,'pear',95]
    item_list =[]
    price_list = []
    item_count = 0
    price_count = 0
    for i in range(len(store_item)):
        if i % 2 == 0:
            item_list.append(store_item[i])
            item_count += 1
        else:
            price_list.append(store_item[i])
            price_count += 1
        
    for j in range(len(item_list)):
        if item == item_list[j]:
            if amount >= price_list[j]:
                cash_back = amount - price_list[j]
                return item, cash_back
            else:
                print('Insufficent amount!')
                exit(1)
        elif item_count > j and item in item_list:
            pass
        else:
            print('You cannot buy it')
            exit(0)
x, y = min_store('orange',50)
print(x,y)