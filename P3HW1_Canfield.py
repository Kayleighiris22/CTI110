"""
P3HW1- Debugging
Canfield
"""
def main():

    # defining minimum score to get grade A, B, C and D
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60

    # asking user to input score 
    score = float(input("Please enter score: "))
    
    # using if-else statements to output the grade letter corresponding to the score
    if score >= A_score:
        print("Your grade is: A")
    else:
        if score >= B_score:
            print("Your grade is: B")
        else:
            if score >= C_score:
                print("Your grade is: C")
            else:
                if score >= D_score:
                    print("Your grade is: D")
                else:
                    print("Your grade is: F")


# calling main function
main()
