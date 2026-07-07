"""
Buggy Solution to Project 3
project3.py
CSC 1570

This program that consumes the homework grades for an unknown
number of homework assignments and produces the resulting homework
grade as a percentage and a letter grade. The letter grade is
based on the letter grading rubric found in the course syllabus.

"""
__author__ = "Your Name"

# These are constants used to denote the maximum and minimum allowed value. Not
#   exactly needed for a correct solution, but useful.
MAX_SCORE = 10
MIN_SCORE = 0

# Input Instructions
print ( "Enter the homework scores one at a time. Type \"done\" when finished." )
hwCount = 1
strScore = input ( "Enter HW#" + str ( hwCount ) + " score: " )
while ( not strScore.isdigit ( ) and strScore != "done" ) or \
      ( strScore.isdigit ( ) and \
      ( int(strScore) < MIN_SCORE or int(strScore) > MAX_SCORE ) ):
    if ( strScore.isdigit ( ) ):
        print ( "Please enter a number between %0d and %0d." \
                % ( MIN_SCORE, MAX_SCORE), end=' ' )
    else:
        print ( "Please enter only whole numbers.", end=' ' )
    strScore = input ( "Enter HW#" + str ( hwCount ) + " score: " )
#end loop
totalScore = 0
while ( strScore != "done" ):
    totalScore += int ( strScore )
    hwCount += 1
    strScore = input ( "Enter HW#" + str ( hwCount ) + " score: " )
    while ( not strScore.isdigit ( ) and strScore != "done" ) or \
          ( strScore.isdigit ( ) and \
          ( int(strScore) < MIN_SCORE or int(strScore) > MAX_SCORE ) ):
        if ( strScore.isdigit ( ) ):
            print ( "Please enter a number between %0d and %0d." \
                % ( MIN_SCORE, MAX_SCORE), end=' ' )
        else:
            print ( "Please enter only whole numbers.", end=' ' )
        strScore = input ( "Enter HW#" + str ( hwCount ) + " score: " )
    #end loop
#end loop

# Calculation Instructions    
if ( hwCount > 1 ):
    pctScore = ( totalScore / ( MAX_SCORE * ( hwCount - 1 ) ) ) * 100
else:
    pctScore = 0
    
if ( pctScore < 60 ):
    letterGrade = "F"
if ( pctScore < 70 ):
    letterGrade = "D"
if ( pctScore < 77 ):
    letterGrade = "C"
if ( pctScore < 80 ):
    letterGrade = "C+"
if ( pctScore < 87 ):
    letterGrade = "B"
if ( pctScore < 90 ):
    letterGrade = "B+"
else:
    letterGrade = "A"

# Output Instructions
print ( "Your percentage score is %.2f%% and your letter grade for the course is a %0s." \
        % ( pctScore, letterGrade ) )

#end

