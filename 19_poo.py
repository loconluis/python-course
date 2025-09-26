class Person:
    def __init__(self, name: str, age: int):  # Constructor
        self.name: str = name
        self.age: int = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


person1 = Person("John", 30)
person2 = Person("Jane", 25)

person1.greet()
person2.greet()


class BankAccount:
    def __init__(self, account_holder: str, balance: float):
        self.account_holder: str = account_holder
        self.balance: float = balance
        self.is_active: bool = True

    def deposit(self, amount: float):
        if self.is_active:
            self.balance += amount
            print(f"Deposited {amount} into {self.account_holder}'s account.")
        else:
            print("Account is inactive")

    def withdraw(self, amount: float):
        if self.is_active:
            if amount <= self.balance:
                self.balance -= amount
            else:
                print("Insufficient funds")
        else:
            print("Account is inactive")

    def get_balance(self) -> float:
        return self.balance

    def transfer(self, amount: float, other_account: "BankAccount"):
        if self.is_active:
            if amount <= self.balance:
                self.balance -= amount
                other_account.balance += amount
            else:
                print("Insufficient funds")
        else:
            print("Account is inactive")

    def deactivate(self):
        self.is_active = False
        print(f"{self.account_holder}'s account has been deactivated.")

    def activate(self):
        self.is_active = True
        print(f"{self.account_holder}'s account has been activated.")


acc1 = BankAccount("John", 1000)
acc2 = BankAccount("Jane", 500)

acc1.deposit(500)
acc1.withdraw(200)
acc1.transfer(300, acc2)

acc1.deactivate()
acc1.deposit(100)
