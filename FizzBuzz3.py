for i in range(1, 101):
    value = ""
    if ( (i % 3) == 0 ):
        value += "Fizz"
    if ( (i % 5) == 0 ):
        value += "Buzz"
    if not ( ((i % 3) == 0) or ((i % 5) == 0) ): 
        value = str(i)
    print(value)