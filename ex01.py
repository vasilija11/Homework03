#Modify the recursive Fibonacci program given in the chapter so that it prints tracing information.
#Specifically, have the function print a message when it is called and when it returns.
def fib(n):

    if n<3:
        return 1

    else:
        return fib(n-1) + fib(n-2)

print("fib(6)")
print(fib(6))