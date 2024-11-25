from decimal import Decimal
import random


class Account:
    def __init__(self, name:str , phone : str) -> None:
        self.name = name.title()
        self.phone = self.set_phone(phone)
        self.balance = Decimal('0.00')
        self.pin = "0000"
        self.account_number = self.generate_account_number()

    def get_balance(self) -> Decimal:
        return self.balance

    def validate_balance(self, amount: Decimal):
        if amount < Decimal('0.00'):
            return "Invalid amount"
        self.balance = amount
        return self.balance

    def deposit(self, amount: Decimal):
        self.validate_amount(amount)
        self.balance += amount

    def validate_amount(self, amount):
        if amount < Decimal('0.00'):
            raise ValueError("Invalid amount")

    def withdraw(self, amount: Decimal, pin : str):
        self.validate_amount(amount)
        self.check_insufficient_balance(amount)
        self.confirm_pin(pin)
        self.balance -= amount

    def check_insufficient_balance(self, amount):
        if amount > self.balance:
            raise ValueError("Not enough balance")

    def set_phone(self, phone: str):
        if len(phone) != 11:
            raise ValueError("Invalid phone number")
        self.phone = phone

    def get_phone(self):
        return self.phone

    def generate_account_number(self):
        account_digits = []
        for _ in range(10):
            digits = random.randint(0, 9)
            account_digits.append(str(digits))
        return "".join(account_digits)

    def change_pin(self, new_pin):
        if len(new_pin) != 4 or not new_pin.isdigit():
            raise ValueError("Invalid pin")
        self.pin = new_pin

    def confirm_pin(self, pin):
        if pin != self.pin:
            raise ValueError("Incorrect pin")

    def get_account_number(self):
        return self.account_number


