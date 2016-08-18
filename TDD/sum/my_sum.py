def my_sum(x, y):
    if x == None or y == None:
        raise TypeError('Function expects two positional arguments. One missing')
    if x == None and y == None:
        raise TypeError('Function expects two positional arguments. None given')
    elif type(x) != int or type(y) != int:
        raise ValueError("Non-integer types passed as arguments")
    else:
        return x + y

#my_sum(5, 20)

#def testFunc(a, b):
#    return a + b
#
#testFunc()


