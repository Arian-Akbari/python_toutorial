food_amount = int(input("food price ?"))
tip_amount = int(input("tip percent ? "))
print('food amount : ${}'.format(food_amount))
print("To pay : ", (food_amount + (tip_amount / 100) * food_amount))
