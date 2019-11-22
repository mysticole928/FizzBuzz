# FizzBuzz

*TL;DR*

* `FizzBuzz1.py` - Python code with four print statements
* `FizzBuzz2.py` - Python code with three print statements
* `FizzBuzz3.py` - Python code with two print statements
* `FizzBuzz4.py` - Python code with one print statement

I was recently asked to do the "FizzBuzz Challege."  I did not do well.  The reasons are many but the essence of it is that, unless I code every day, I stop thinking like a programmer.

However, I have a hard time letting problems go.  So, I sat down and figured it out.

## The challenge

Write a program that prints the numbers from 1 to 100.

For multiples of three print `Fizz` instead of the number and for multiples of five print, `Buzz`.

For numbers that are multiples of both three and five, print `FizzBuzz`.

## My first attempt

I used python as it has become my *go to* language for prototypes and small projects.

I was _mostly_ successful with my first attempt.  It was done on a whiteboard.  In hindsight, I did miss some of the, um, precision in my syntax.  However, I got the overall flow correct.

```python
for i in range(1, 101):
    if ( ( (i % 3) == 0 ) & ( (i % 5) == 0) ):
        print("FizzBuzz")
    elif( (i % 3) == 0 ):
        print("Fizz")
    elif( (i % 5) == 0 ):
        print("Buzz")
    else:
        print(i)
```

## The refactor challenge

This was my failure.  (I should let go of it and move on.  However, I _need_ to know why things happen the way they do.)  I was asked to refactor this snippet to have three print statements instead of four.

After playing with it, this was my solution

```python
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
```

This was harder than I expected.  Part of it was that, once I saw how refactor down to a single print statement, it was hard to build soemthing that I _knew_ to be inefficient.

For this solution, I removed the newline character after printing either `Fizz` or `Buzz`.  However, I needed it back when I printed a number that was not multiple of 3 or 5.

## And then there were two

I started with four print statements, figured out how to do it with a single print statement, and then refactored it to have only three print statements.

Maybe I should try two print statements.

```python
for i in range(1, 101):
    value = ''
    
    if ( (i % 3) == 0 ):
        value = 'Fizz'
    if ( (i % 5) == 0 ):
        value += 'Buzz'
        
    print(value, end='') 
        
    if (value):
        value = ''
        
    if not ( ((i % 3) == 0) or ((i % 5) == 0) ):
        value = i
        
    print(value)
```

This made me happy from a readability standpoint.  

`Fizz` is assigned to the variable `value` because, if called, it will *always* be first.

`Buzz` is assigned using `+=` because it might be the only thing on the line *or* it might terminate the line. 

## Down to a single print statement

In the end, after spending some time on it, I got it down to a single print statement.  *_I actually figured this out before doing either three or two print statements._*  

```python
for i in range(1, 101):
    value = ""
    if ( (i % 3) == 0 ):
        value += "Fizz"
    if ( (i % 5) == 0 ):
        value += "Buzz"
    if not ( ((i % 3) == 0) or ((i % 5) == 0) ): 
        value = str(i)
    print(value)
```

No, this doesn't help me now.  It's a day late (+/-) and a dollar short.  

However, it does make me feel good about figuring out where I went wrong.
