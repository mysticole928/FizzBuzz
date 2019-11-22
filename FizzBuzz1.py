for i in range(1, 101):
    # If a mulitple of 3 and a multiple of 5 
    # I chose the modulo of 3 *and* the modulo of 5
    # for readability.  (i mod 15) would probably have been 
    # simpler.  However, I opted to mirror the requirement.
    if ( ( (i % 3) == 0 ) and ( (i % 5) == 0) ):
        print("FizzBuzz")
    # Check for multiple of 3.
    elif( (i % 3) == 0 ):
        print("Fizz")
    # Check for a multiple of 5.
    elif( (i % 5) == 0 ):
        print("Buzz")
    # For everything else, print the number.
    else:
        print(i)