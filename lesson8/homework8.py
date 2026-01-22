# Parent class
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


# Child classes
class Cow(Animal):
    def __init__(self, name, age, milk_per_day):
        super().__init__(name, age)
        self.milk_per_day = milk_per_day

    def produce_milk(self):
        print(f"{self.name} produces {self.milk_per_day} liters of milk per day.")


class Chicken(Animal):
    def __init__(self, name, age, eggs_per_week):
        super().__init__(name, age)
        self.eggs_per_week = eggs_per_week

    def lay_eggs(self):
        print(f"{self.name} lays {self.eggs_per_week} eggs per week.")


class Sheep(Animal):
    def __init__(self, name, age, wool_kg):
        super().__init__(name, age)
        self.wool_kg = wool_kg

    def produce_wool(self):
        print(f"{self.name} produces {self.wool_kg} kg of wool.")


# Testing the farm
cow = Cow("Bessie", 5, 10)
chicken = Chicken("Clucky", 2, 12)
sheep = Sheep("Wooly", 4, 6)

animals = [cow, chicken, sheep]

for animal in animals:
    print("\nAnimal info:")
    print(f"Name: {animal.name}, Age: {animal.age}")
    animal.eat()
    animal.sleep()

cow.produce_milk()
chicken.lay_eggs()
sheep.produce_wool()
    print(f"Tuition mean: $ {tuition_mean:.2f}")
    print(f"Tuition median: $ {tuition_median}")

####################################################################################################################
####################################################################################################################

import os

# Account class
class Account:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"Account Number: {self.account_number}, Name: {self.name}, Balance: ${self.balance}"


# Bank class
class Bank:
    def __init__(self, filename="accounts.txt"):
        self.accounts = {}
        self.filename = filename
        self.load_from_file()

    def generate_account_number(self):
        return str(len(self.accounts) + 1001)

    def create_account(self, name, initial_deposit):
        if initial_deposit < 0:
            print("Initial deposit must be positive.")
            return

        acc_number = self.generate_account_number()
        account = Account(acc_number, name, initial_deposit)
        self.accounts[acc_number] = account
        self.save_to_file()
        print("Account created successfully!")
        print(account)

    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(account)
        else:
            print("Account not found.")

    def deposit(self, account_number, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return

        account = self.accounts.get(account_number)
        if account:
            account.balance += amount
            self.save_to_file()
            print("Deposit successful.")
            print(account)
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if not account:
            print("Account not found.")
            return

        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > account.balance:
            print("Insufficient balance.")
        else:
            account.balance -= amount
            self.save_to_file()
            print("Withdrawal successful.")
            print(account)

    def save_to_file(self):
        with open(self.filename, "w") as file:
            for acc in self.accounts.values():
                file.write(f"{acc.account_number},{acc.name},{acc.balance}\n")

    def load_from_file(self):
        if not os.path.exists(self.filename):
            return

        with open(self.filename, "r") as file:
            for line in file:
                acc_number, name, balance = line.strip().split(",")
                self.accounts[acc_number] = Account(acc_number, name, float(balance))


# Command-line interface
def main():
    bank = Bank()

    while True:
        print("\n--- BANK MENU ---")
        print("1. Create Account")
        print("2. View Account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter name: ")
            deposit = float(input("Enter initial deposit: "))
            bank.create_account(name, deposit)

        elif choice == "2":
            acc = input("Enter account number: ")
            bank.view_account(acc)

        elif choice == "3":
            acc = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            bank.deposit(acc, amount)

        elif choice == "4":
            acc = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            bank.withdraw(acc, amount)

        elif choice == "5":
            print("Thank you for using the bank system!")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
