def calculate_calories(carbs,fats,proteins):
    total = (carbs*4) + (fats*9) + (proteins*4)
    print("total calories:",total)


carbs = float(input("enter carbs: "))
fats = float(input("enter fats: "))
proteins = float(input("enter proteins: "))

calculate_calories(carbs,fats,proteins)
