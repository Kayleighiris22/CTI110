"""
# CTI-110
# P3HW2 - Pizza Order
# Canfield
# 03/12/2022
"""
import math

# accept user input for number of students
students = int(input("How many students do you want to order pizza for? "))
# accept user input for number of people per pizza
people = float(input("Enter the number of people per pizza (1.5, 2 or 3): "))

# if people per pizza is valid then calculate the number of pizzas and price
if people == 1.5 or people == 2 or people == 3:
    whole_pizzas = math.ceil(students / people)
    price = whole_pizzas * 5; 
#obtain price = price + price * 0.06
    price = price + price * 0.06;
    print()
    print("----Pizza Order--------") 
    print("Number of Students :  ", students)
    print("Pizzas Needed: ", whole_pizzas)
    print("Price $  ", str(round(price, 2)))
    print("--------------------------------")
else:
    print("INVALID ENTRY!!!!")
    print("Should have entered 1.5, 2, or 3")
    print()
    print("Run Program again")
