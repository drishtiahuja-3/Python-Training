## coupon code avail 

# Condition 1: promo code can be applied iff min amount is greater than 500 
# Condition 2:  

promo_code = "GET200" 
amount = float(input("Enter the amount: "))
min_amount = 500 

#CONDITIONAL CONSTRUCT 
if amount > min_amount:
    print("you can apply promo code: ", promo_code)
    amount -= 200 
    print("promo code applied successfully. Please pay :", amount)
else:
    print("you cannot apply promo code: ", promo_code)
    print("add items worth :", min_amount - amount, "more... ")