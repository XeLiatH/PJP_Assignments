"""
Generátor Fibonacciho posloupnosti
klasický příklad generátoru 
"""

def fib(max):
    """
    Generátor Fibonacciho posloupnosti
    """
    a, b = 0, 1          
    while a < max:
        yield a          
        a, b = b, a + b  

def demo_stop(max):
    """
    raises StopIteration
    """
    gen = fib(max)
    while True:
        try:
            print(next(gen))
        except StopIteration:
            print("generator skoncil")
            break


if __name__ == '__main__':
    print(fib(1000))
    print(list(fib(1000)))
    print(len(list(fib(1000))))         
    demo_stop(1000)
    [print(x) for x in fib(1000)]