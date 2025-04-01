class Calculator:
    def __init__(self):
        pass
    def addition(self, a, b):
        result = a+b
        print(f"{a} + {b} = {result}")
    def sub(self, a, b):
        result = a-b
        print(f"{a} - {b} = {result}")
    def mul(self, a, b):
        result = a*b
        print(f"{a} * {b} = {result}")
    def div(self, a, b):
        result = a/b
        print(f"{a} / {b} = {result}")
        


cal = Calculator()



def op():
    try:
        num1 = int(input("Please enter 1st number : "))
        num2 = int(input("Enter the 2nd number : "))

        operation = input("Operation : ")
        if "+" in operation:
            cal.addition(num1,num2)
        elif "*" in operation:
            cal.mul(num1,num2)
        elif "-" in operation:
            cal.sub(num1,num2)
        elif "/" in operation:
            cal.div(num1,num2)
        else:
            print("please enter valid Operation like (*, +, -).")
            op()
    except(ValueError):
        print("please enter valid numbers.")
        op()
    except KeyboardInterrupt:
        print("\nOperation canceled by user. Exiting...")  
        exit(0)


op()






