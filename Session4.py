"""
ZOMATO : 20% off 
        :MIN value :300
BINGO : 50 % off 
        :min value: 500 
        :max discount: 100
"""
promo_code = input("enter promo code: ")
amount = float(input("enter the amount: "))
#Nested if else
if promo_code == "ZOMATO":
    print("ZOMATO can be applied... ")

    if amount > 300:
        discount = 0.20 * amount  
        print("ZOMATO applied successfully. You got a discount of :", discount)
        amount -= discount
        amount = amount + 0.18*amount # gst tax 
        amount += 16.5 # delivery charges 
        print("You can pay:" , amount)
    else: 
        print("amount is less. You can add items worth", 300 - amount , "more...")

# indentation : PEP (python enhancement proposal)

elif promo_code == "BINGO":
    print("BINGO can be applied... ")

    if amount > 500:
        discount = 0.50 * amount

        if discount > 100:
            discount = 100
            print("BINGO applied successfully. you got a discount of: ", discount) 
            amount -= discount
            amount = amount + 0.18*amount # gst tax 
            amount += 16.5 # delivery charges  
            print("You can pay: \u20b9", amount) 
        else:
            print("amount is less. You can add more items worth", 500 - amount ,"more..")

else: 
    print("Invalid promo code ... ")


# write your name in hindi/ punjabi / any language using unicodes 
