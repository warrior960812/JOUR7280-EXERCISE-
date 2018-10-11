print("hello")
def fib(n):
    a,b=0,1
    while a<n:
        print(a,end='')
        a,b=b,a+b
    print()
    # Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
print((6>5)and(2<4))
print((8==8)or(6 !=6))
print(not(3 <=1))