def Destol(customer_id):
    charges = 10000
    def selling_petrol():
        nonlocal charges
        charges -= 2000
        print(f"{customer_id} filled patrol: cost 2000, left charges {charges}")
    return selling_petrol

Jimmy = Destol("Jimmy")
Cathy = Destol("Cathy")
Denith = Destol("Denith")

Jimmy()
Jimmy()
Jimmy()
Cathy()
Denith()
Cathy()