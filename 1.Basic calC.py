#To make a calculator which performs basic operations:

a=float(input("Enter first number(a):"))
b=float(input("Enter second number(b):"))
print("Use '+' for addition")
print("Use '-' for subtraction")
print("Use '*' for multipication")
print("Use '/' for division")
print("Use '**' for exponents where a raised to b ")
c=input("Select the operator:")
match c:
    case '+':  print(a+b)
    case '-':  print(a-b)
    case '*':  print(a*b)
    case '/':  print(float(a/b))
    case '**': print(a**b)
    case _:    print("Invalid Case")
