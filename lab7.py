from random import randint
"""
    lab7.py
    Lab #7
    CSC 1570

    This program will encrypt a message using the Caesar cipher
    with a random offset value. OR to decrypt a message when
    provided with the encryption key.
"""
__author__ = "Your Name"

def main ( ):
    choice = get_menu_choice( )
    while choice != 3:
        if choice == 1:
            message = input ( "Enter message: " )
            key = randint (1, 26)
            print ( f"Key = {key}" )
            print ( f"Encrypted = \"{encrypt(message, key)}\"")
        elif choice == 2:
            message = input ( "Enter message: " )
            key = int ( input ( "Enter key: " ) )
            print ( f"Decrypted = \"{encrypt(message, -key)}\"")
        choice = get_menu_choice( )

def get_menu_choice ():
    """ Displays a menu that asks what action to perform on a given
        message. Accepts and validates the users response before
        returning it. """
    print ( "Menu options:",
            "\tSelect 1: Encrypt a message.",
            "\tSelect 2: Decrypt a message.",
            "\tSelect 3: Exit program.",
            sep = "\n"  )
    choice = input ( "Select option: " )
    while choice not in ("1", "2", "3" ):
        choice = input ( "Invalid selection. Select option: " )
    return int ( choice )

def encrypt ( message, key ):
    """ Is used to either encrypt or decrypt a message using the provided key.
    For encrypting the key should be a possive number between 1 and 26. For
    decrpyting the key should be within the same range, but a negative number."""
    cipher = ""
    # Write the encyption code here
    return cipher

if __name__ == "__main__":
    main ()


