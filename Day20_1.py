def finding_weather():
    month : str = input('Enter month eg.Jan , Feb, Mar :')  #Mar
    monthly = {"jan":"Winter","feb":"Winter",
           "mar":"Summer","apr":"Summer","may":"Summer","jun":"Summer",
           "jul":"Rainy Season","aug":"Rainy Season","sep":"Rainy Season",
           "oct":"Rainy Season","nov":"Winter","dec":"Winter"}
    for i,j in monthly.items():
        if i == month.lower():
            return f"The weather is {j}"
    return 'Not Found'

def finding_weather_2():
    month : str = input('Enter month eg.Jan , Feb, Mar :')  #Mar
    monthly = ["jan","Winter","feb","Winter",
           "mar","Summer","apr","Summer","may","Summer","jun","Summer",
           "jul","Rainy Season","aug","Rainy Season","sep","Rainy Season",
           "oct","Rainy Season","nov","Winter","dec","Winter"]
    monthly.update
    for i in range(len(monthly)):
        if monthly[i] == month.lower():
             return f"The weather is {monthly[i+1]}"
    return 'Not Found'

print(finding_weather_2())