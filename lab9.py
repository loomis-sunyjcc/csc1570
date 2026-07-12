"""
    lab9.py
    Lab #9
    CSC 1570

    This program is used to reserve seats for
    customers in a movie theater or concert.
    Occupied seats contain an X and empty seats
    are marked with an O.
"""
__author__ = "Your Name"

ROWS = 5
COLS = 10
MENU = { "X": "E(x)it",
         "M": "Display (M)enu",
         "S": "Display (S)eats",
         "R": "(R)eserve Seat" }

def main ( ):
    # Initialize a 2D grid of 'O's
    seats = [['O' for _ in range(COLS)] for _ in range(ROWS)]

    # Small test loop
    print("Welcome to the Ticket Manager!")

    for option, label in MENU.items():
        print ( f"{option}: {label}" )
    print ()
    selection =  input ( "Make a selection: " ).upper()[0]
    while selection != "X":
        if selection == "M":
            for option, label in MENU.items():
                print ( f"{option}: {label}" )
        elif selection == "S":
            display_seats(seats)
        elif selection == "R":
            seat = tuple( input ( "Enter seat# (row col): " ).split() )
            r, c = int( seat[0]), int(seat[1])
            if book_seat ( seats, r, c ):
                print ( "Seat booked" )
            else:
                print ( "Invalid seat option" )
        print()
        selection =  input ( "Make a selection: " ).upper()[0]

def display_seats(seats):
    """ Displays the seats in a 2D grid. """
    print ( f"There are {count_empty_seats(seats)} seats available." )
    # Print col header row
    header = [str (x) for x in range(0, COLS) ]
    print( "   " + " ".join(header) )
    for index, row in enumerate(seats):
        # Print row header followed by the seats
        print(f"{index}: " + " ".join(row))

def book_seat(seats, row, col):
    """ Reserves a seat for the given row and col in the grid. """
    # TODO: Step 1: Check if the row and col are valid (0 to ROWS/COLS)
    # TODO: Step 2: Check if seat is 'O' or 'X'
    # TODO: Step 3: Update the seat if available
    return False

def count_empty_seats(grid):
    """ Produces the count of the number of empty seats. """
    # TODO: Use nested loops to count 'O's
    pass

if __name__ == "__main__":
    main ()
