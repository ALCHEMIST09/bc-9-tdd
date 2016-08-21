def fizz_buzz(n):
    if n == None:
        raise TypeError('Function expects an integer argument. No argument given')
    elif type(n) == str:
        raise TypeError('Function expects an integer argument. String given')
    elif type(n) == list:
        raise TypeError("Functions expects numerical argument. List given")
    
    if n % 3 == 0 and n % 5 != 0:
        return 'Fizz'
    elif n % 5 == 0 and n % 3 != 0:
        return 'Buzz'
    elif n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    else:
        return n
    
#print(fizz_buzz(9))
#print(fizz_buzz(15))
#print(fizz_buzz(18))
#print(fizz_buzz(21))
#print(fizz_buzz(25))
#print(fizz_buzz(41))