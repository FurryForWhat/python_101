def min_store(item,amount):
    store_item = ['candy', 3,'liquior',350, 'ciggarte',40, 'apple',80,'pear',95,'rice',10,'fried egg', 5]
    store_dict = {store_item[i] : store_item[i+1] for i in range (0,len(store_item),2)}
    
    purchase_item = []
    spend_money = 0
    
    for product,price in store_dict.items():
        if product in item:
            purchase_item.append(product)
            spend_money += price
            item = item.replace(product, '', 1)
            
    if spend_money > amount:
        return "Insufficient Amount",None
    else:
        cash_back = amount-spend_money
        return purchase_item , cash_back
            
x, y = min_store('fried',1000)

if y is None:
    print(x)
else:
    print(x,y)