# This was the second part of the challenge.
# Refactor four print statements into three.
# There's a certain irony here as it was much easier to 
# refactor my original code into needing one print statement.

for i in range(1, 101):
    value = ''
    
    if ( (i % 3) == 0 ):
        value = 'Fizz'
        print(value, end='')

    if ( (i % 5) == 0 ):
        value = 'Buzz'
        print(value, end='') 
        
    if (value):
        value = ''
        
    if not ( ((i % 3) == 0) or ((i % 5) == 0) ):
        value = i
        
    print(value)