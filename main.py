def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def div(a,b):
    return a / b
def mul(a,b):
    return a * b
def exp(a,b):
    return a**b

def main():
    print("Welcome twin")
    num1 = float(input("what is your first number? "))
    num2 = float(input("What is your second number? "))
    func = input("What operation(/, +, -, *, ^)? ")

    if func == "/":
        print(div(num1, num2))
    if func == "*":
        print(mul(num1, num2))
    if func == "+":
        print(add(num1, num2))
    if func == "-":
        print(sub(num1, num2))
    if func == "^":
        print(exp(num1, num2))  

maybe = True
while maybe == True:
    main()
    y = str.capitalize(input("Done? Y/N: "))
    if y == "Y":
        maybe = False
    elif y == "N":
        maybe = True