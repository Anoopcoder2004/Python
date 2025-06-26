b=0
try:
    a=10/b
    print(a)
except ZeroDivisionError:
    print("cannot divide by zero")