fib = lambda x: 1-x if x < 2 else  fib(x-1)+fib(x-2)
print(fib(4))

#from functools import reduce
#fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1])
#print(fib(35)) 