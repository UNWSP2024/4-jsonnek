# Jonathan Sonnek
# Sept 21 2025
# Budget Calculator

# Program #5: Bank Balance
# Write a program that asks the user to enter the amount that he or she has budgeted for a month.
# A loop should then prompt the user to enter each of his or her expenses for the 
# month and keep a running total. (Enter 0 to exit the loop)  
# When the loop finishes, the program should display the amount that the 
# user is over or under budget.

def main():
    budget = 0.0
    difference = 0.0
    spent = 1.0         #initialize for while loop
    total = 0.0

    ######################
    # Setting initial expenses to 0 and finding the budget
    total_expenses = 0.0
    budget = float(input("Enter your budget: "))


    while True:
        expense = float(input("Enter your expense (Enter 0 if no more expenses): "))
        if expense == 0:
            break
        else:
            total_expenses += expense
            budget -= expense
    if budget > 0:
        print("You saved $", budget, "this month!")
    elif budget == 0:
        print("You budgeted well, you have $",budget, "left." )
    else:
        print("You went over your budget by $", abs(budget),"!")
    ######################


if __name__ == '__main__':
    main()