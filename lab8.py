"""
    lab8.py
    Lab #8
    CSC 1570

    This program perform two common conversions that are
    used in computer science.
        Converting from a binary number to an integer
        Converting from an integer to a binary number
    The user will be asked which task to perform.
"""
__author__ = "Your Name"

def main ( ):
    print ( "Menu options:",
            "\tSelect 1: Convert from Binary to Decimal.",
            "\tSelect 2: Convert from Decimal to Binary.",
            sep = "\n"  )
    choice = input ( "Select option: " )
    while choice not in ("1", "2" ):
        choice = input ( "Invalid selection. Select option: " )

    if choice == "1":
        number = input ( "Enter a binary number: " )
        print ( binary_to_decimal(number) )
    elif choice == "2":
        number = int ( input ( "Enter positive decimal number: " ) )
        print ( decimal_to_binary(number) )

def binary_to_decimal ( bit_string ):
    """ Converts a bit string to it's decimal equivalent. """
    decimal_num = 0
    # Write the conversion code here
    return decimal_num

def decimal_to_binary ( number ):
    """ Converts a whole positive integer to its binary equivalent. """
    bit_string = ""
    # Write the conversion code here
    return bit_string

if __name__ == "__main__":
    main ()


