class Car:
    def __init__(self,owner,brand,model,unique_ability,four_wheel = True) -> None:
        self.name = owner
        self.brand = brand
        self.model = model
        self.ability = unique_ability
        self.wheel = four_wheel
        
U_Kyaw_Kyaw= Car('KyawKyaw','Toyota','2019','Crown')
print(f'user {U_Kyaw_Kyaw.name} own a {U_Kyaw_Kyaw.model} {U_Kyaw_Kyaw.brand} {U_Kyaw_Kyaw.ability}')
print(f'user {U_Kyaw_Kyaw.name} car has four wheel :{U_Kyaw_Kyaw.wheel}')

U_Mya = Car('Mya','Mitsubishi','1996','Landcruser')
print(f'user {U_Mya.name} own a {U_Mya.model} {U_Mya.brand} {U_Mya.ability}')

U_Aung= Car('Aung','Honda','2023','TriCyle',False)
print(f'user {U_Aung.name} car has four wheel :{U_Aung.wheel}')
