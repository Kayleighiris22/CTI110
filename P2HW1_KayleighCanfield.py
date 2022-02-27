f= open("P2HW1_KayleighCanfield.py")
 
# Total Purchases
# 02/26/2022
# CTI-110 P2HW1 - Total Purchases
# Kayleigh Canfield
#

# parse input as float
price1 = float(input("Enter the price of item #1:  "))

#parse input as float
price2 = float(input("Enter the price of item #2:  "))

#parse input as float
price3 = float(input("Enter the price of item #3:  "))

#parse input as float
price4 = float(input("Enter the price of item #4:  "))

#parse input as float
price5 = float(input("Enter the price of item #5:  "))

#obtain subtotal = price1 + price2 +price3 +price4 +price5
subtotal = price1 + price2 +price3 +price4 +price5;

#obtain sales tax = subtotal * 0.07
salestax = subtotal * 0.07;

#obtain overall total = subtotal + sales tax
total = subtotal + salestax;

#print results
print("-------Results-------")

#print subtotal after converting to string
print("Subtotal:  " + str(round(subtotal, 2)))

#print sales tax after converting to string
print("Sales Tax:  " + str(round(subtotal * 0.07, 2)))

#print overall total after converting to string
print("Total:  " + str(round(subtotal + salestax, 2)))

#call function P2HW1_KayleighCanfield.py()
    
    
    
    
                  
    
