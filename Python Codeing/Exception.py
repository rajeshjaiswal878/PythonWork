try:
    a=10
    b=0
    print(a+b)
except ZeroDivisionError:
    print("Change B value")
finally:
    print("fuck you")