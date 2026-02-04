# Wrapping data and functions into a single unit (object)

'''.

🔐 What is Encapsulation?

Encapsulation means wrapping data (variables) and code (methods) together inside a class and restricting direct access to some of the data.

👉 In simple words:
“Hide the data and control how it is used.”

In Python, we do this using private variables and getter/setter methods.

🧍‍♂️ Real-Life Example

Think about a bank account.
You cannot directly change your bank balance from outside.
You must use:

Deposit

Withdraw
methods provided by the bank.

That's encapsulation.'''

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # Public variable
        self.__balance = balance    # Private variable (Encapsulated)

    # Getter method to view balance
    def get_balance(self):
        return self.__balance

    # Setter method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Invalid deposit amount")

    # Setter method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. Remaining balance: {self.__balance}")
        else:
            print("Insufficient balance or invalid amount")

acc = BankAccount("Rahul Shapri", 1000)

print(acc.owner)          # Accessible (Public)
print(acc.get_balance())  # Accessing private data via method

acc.deposit(500)
acc.withdraw(300)

print(acc.__balance)      # ❌ This will give an error (Private variable)

