from new_lab9 import book_seat

seats = [['O' for _ in range(3)] for _ in range(3)]

try:
    book_seat( seats, 0, 0)
    print ( "Seat booked" )
except Exception as e:
    print ( e )

try:
    print ( book_seat( seats, 0, 0) ) # False
    print ( "Seat booked" )
except Exception as e:
    print ( e )

try:
    print ( book_seat( seats, 1, "1") ) # Exception
except Exception as e:
    print ( e )

try:
    print ( book_seat( seats, -1, -1) ) # Exception
except Exception as e:
    print ( e )

try:
    print ( book_seat( seats, 5, 5) ) # Exception
except Exception as e:
    print ( e )
