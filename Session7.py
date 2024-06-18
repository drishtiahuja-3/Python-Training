""" 
I have HDFC bank Credit card 
Hdfc bank will charge 15% interest on outstanding amount 
Minimum, you should be able to pay 10 % of outstanding amount else your credit score will be compromised


april 2024 -> 50,000  ----> input by user 
    april 2024 min -> 5000
                pending ->45,000
                            +15% of 45,000 = 6750
I can only pay max of 8000 per month -----> input by user 

find in which month whole amount will become 0  
"""

print("\n\n\t\tWelcome To HDFC Bank Credit Card Services")
print("\n******************************************************************************")
print("\t\tCONDITIONS TO OWN A CREDIT CARD")
print("1. Minimum amount you should be able to pay is 10% of the outstanding amount so that your credit score is not affected.")
print("2. Total interest charged on the outstanding amount is 15% .\n\n")

n = int(input("Enter 1 if u want to have a credit card or 0 to exit:"))
if n == 1:
    amount = int(input("\nEnter the outstanding amount u would like to take credit card service on: "))
    min = 0.10 * amount
    print("Minimum amount that is to be paid every month will be:" , min)
    interest = 0.15 * amount 
    print("You have to pay the interest of:", interest)
    amount = amount + interest
    print("Total amount to be paid is:", amount)
    month = input("Enter the month in which u applied for credit card:")
    if month == "january":
        m = 1

    elif month == "february":
        m = 2

    elif month == "march":
        m = 3

    elif month == "april":
        m = 4
    elif month == "may":
        m = 5
       
    elif month == "june":
        m = 6
     
    elif month == "july":
        m = 7
  
    elif month == "august":
        m = 8
      
    elif month == "september":
        m = 9
       
    elif month == "october":
        m = 10
       
    elif month == "november":
        m = 11
   
    elif month == "december":
        m = 12
        
    else:
        print("not a valid month")
        

    while amount > 0:
        max= int(input("Enter the amount you can pay this month:"))
        if max >= min :
            amount = amount - max
            print("The amount left is :", amount)
            m +=1
            
        else:
            print("The amount to be paid this month is less than", min,".....")
            break
    print("EMI COMPLETED SUCCESSFULLY...")
    if m % 12 == 0:
        print("You will finish the EMI in December")
      
    elif m % 12 == 1:
        print("You will finish the EMI in January")
    
    elif m % 12 == 2:
        print("You will finish the EMI in February")
       
    elif m % 12 == 3:
        print("You will finish the EMI in March")
  
    elif m % 12 == 4:
        print("You will finish the EMI in April")
 
    elif m % 12 == 5:
        print("You will finish the EMI in May")
     
    elif m % 12 == 6:
        print("You will finish the EMI in June")
       
    elif m % 12 == 7:
        print("You will finish the EMI in July")
       
    elif m % 12 == 8:
        print("You will finish the EMI in August")
        
    elif m % 12 == 9:
        print("You will finish the EMI in September")
        
    elif m % 12 == 10:
        print("You will finish the EMI in October")
      
    else:
        print("You will finish the EMI in November")
     
else:
    print("EXIT")
