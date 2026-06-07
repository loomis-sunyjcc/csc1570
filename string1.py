"""
    This program illustrates the immuteable nature
    of a string variable in Python. It prints out the
    identifying number for a variable in Python in
    hexadecimal form. This is the equivalent of printing
    the memory address of a variable in other languages.
"""
__author__ = "Ken Loomis"

str1 = "Hello"
print ( "The memory address of str1 =", hex( id ( str1 ) ) )
str2 = "class"
#Reassign a new string for str1
str1 = str1 + " " + str2
print ( "The new memory address of str1 =", hex( id ( str1 ) ) )
