logo = r"""
   _____________________
  |  _________________  |
  | | CALCULATOR      | |
  | |_________________| |
  |  ___ ___ ___ ___    |
  | | 7 | 8 | 9 | + |   |
  | |___|___|___|___|   |
  | | 4 | 5 | 6 | - |   |
  | |___|___|___|___|   |
  | | 1 | 2 | 3 | * |   |
  | |___|___|___|___|   |
  | | 0 | . | = | / |   | 
  | |___|___|___|___|   |
  |_____________________|
"""






def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2 

operations = {
    "+": add ,
    "-": subtract,
    "*": multiply,
    "/": divide 
}

def calculator():
    print(logo)

    should_accumulate = True
    num1 = float(input("what's the first number ? : "))

    while should_accumulate:
        for symbols in operations:
            print(symbols)
        operaton_symbol = input("Pick an operation ? : ")
        num2 = float(input("What's the next number : "))
        answer = operations[operaton_symbol](num1,num2)
        print(f"{num1} {operaton_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer} Or Type 'n' to start a new calculation Or Type 'stop' to stop program ").lower()
        if choice =="stop":
            return 0
        if choice =="y":
            num1 = answer

        else:
            should_accumulate = False
            print("\n"*50)
            calculator()

calculator()