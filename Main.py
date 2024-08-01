
def add(num1,num2):
    result = num1 + num2 
    return result

def subtract(num1, num2):
    result = num1 - num2
    return result

def multiply(num1, num2):
    result = num1 * num2
    return result

def divide(num1,num2):
    result = num1 / num2
    return result

def remainder(num1,num2):
    result = num1 % num2
    return result

def getNum(prompt="Please enter your number. \n"):
    while True:
        user_input = input(prompt)
        try:
            user_num = float(user_input)
            return user_num
        except ValueError:
            print("This is not a number. Pleaes try again.")


def getOperator(prompt="enter your operator (+, -, *, /) \n"):

    operators = ["+", "-", "*", "/"]

    while True:
        user_input = input(prompt)
        if user_input in operators:
            return user_input
        else:
            print("this is an invalid operator. please enter one of the following: \n (+, -, *, /)")


def calculation(num1,num2, operation):
    if operation == "+":
        print("Result:", add(num1,num2), "\n")
    
    elif operation == "-":
        print("Result:", subtract(num1,num2), "\n")
    
    elif operation == "*":
        print("Result:", multiply(num1,num2), "\n")

    elif operation == "/":
        print("Result:", divide(num1,num2), "\n")
    
    else:
        print("this is invalid. try again.")

if __name__ == "__main__":

    calculate = True
    print("--------------------------------------------- \n")
    print("how this works: \n enter 2 numbers and the operation. \n")
    print("---------------------------------------------")

    while calculate == True:
        
        num1 = getNum()
        num2 = getNum()
        op = getOperator()

        calculation(num1,num2, op)

        continue_calc = input("continue Y/N \n")
        if ((continue_calc == "Y") or (continue_calc == "y")):
            continue
        elif ((continue_calc == "N") or (continue_calc =="n")):
            calculate = False
            print("goodbye!")
            SystemExit
        