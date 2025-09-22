# Jonathan Sonnek
# Sept 21 2025
# Movie Tickets

# Program #2: Movie Tix
# Write a program that has the user input various movie names and how many 
# tickets are desired for each movie.  
# At the end of the program it prints out the total number of tickets desired by the user.  
# Use either a "for loop" or "while loop" to accomplish this.

def main():
    ######################
    # Setting the add_movie variable to True to begin the program
    add_movie = True

    # Setting the initial ticket count to 0
    total_tickets = 0
    # Movie title collector
    while add_movie == True:
        title = input("Enter Movie Title (Type x if no more movie titles): ")
        if(title == "x"):
            add_movie = False
        else:
            tickets = int(input("Enter the number of tickets: "))
            total_tickets += tickets
    print("Total tickets: ", total_tickets)
    ######################


if __name__ == '__main__':
    main()