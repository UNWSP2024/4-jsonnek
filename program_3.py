# Program #3: Average Rainfall
# Write a program that uses nested loops to collect data and calculate the average 
# rainfall over a period of years.  
# The program should first ask for the number of years.  
# The outer loop will iterate once for each year. 
# The inner loop will iterate twelve times, once for each month.  
# Each iteration of the inner loop will ask the user for inches of rainfall for each month.  
# After all iterations, the program should display the number of months, 
# the total inches of rainfall, and the average rainfall per month for the entire period.

def main():
    ######################
    # Determining how many times to run the program.
    years = int(input("Enter Years: "))

    # Defining variables
    total_rain_fall = 0
    months = 0

    # Collect Data
    for year in range(years):
        for month in range(12):
            months += 1
            print('Month', months)
            monthly_rain_fall = float(input("How many inches of rain",))
            total_rain_fall += monthly_rain_fall
            if (months) == 12:
                months = 0

    # Calculate average rainfall
    average_monthly_rain_fall = total_rain_fall / (12*years)

    # Display totals
    print("The average monthly rain fall is", average_monthly_rain_fall)
    print("Total Rain Fall:", total_rain_fall)


    ######################


if __name__ == '__main__':
    main()