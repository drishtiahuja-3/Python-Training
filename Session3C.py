# promo code: ZOMATO
# CONDITION 1 : More then 249
# CONDITION 2 : 50 % off upto 150 
amount = float(input("Enter the amount: "))
promo_code = input("enter promo code: ")

#nested if else
if promo_code == "ZOMATO":
    print("Promo code valid")

    if amount > 249:
        print("promo code applied")

        discount = 0.50 * amount
        if discount >= 150:
            discount= 150  
        amount -= discount
        print("discount is:", discount)
        print("Please pay is:", amount)

    else:
        print("amount is low...")
else:
    print("promo code invalid")
