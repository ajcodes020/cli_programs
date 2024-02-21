def add(n1, n2):
    """ Returns the sum of n1, n2 """
    return n1 + n2


def subtract(n1, n2):
    """ Returns the difference of n1, n2 """
    return n1 - n2


def multiply(n1, n2):
    """ Returns the product of n1, n2 """
    return n1 * n2


def divide(n1, n2):
    """ Returns the quotient of n1, n2 """
    return n1 / n2


operations_dict = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}


def calculator():
    """ Starts the calculator program """
    num1 = float(input("Enter a number: "))
    proceed = True

    while proceed:
        operation_symbol = input("What operation? (+, -, *, /): ")
        num2 = float(input("Enter next number: "))
        answer = operations_dict[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        num1 = answer
        choice = input("Type 'y' to continue, 'r' to reset, else exit: ")
        if choice == 'y':
            continue
        elif choice == 'r':
            calculator()
        else:
            break


calculator()
