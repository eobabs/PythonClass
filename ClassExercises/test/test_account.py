import unittest
from decimal import Decimal

from account import Account

class TestAccount (unittest.TestCase):

    def setUp(self):
        self.account_one = Account("EOB", "08099999999")

    def test_that_account_exist(self):
        account_one = Account("EOB", "08099999999")

    def test_deposit_function(self):
        self.account_one.deposit(Decimal('1000'))
        self.assertEqual(self.account_one.get_balance(), Decimal('1000'))

    def test_deposit_function_does_not_allow_negatives(self):
        account_one = Account("EOB", "08099999999")
        self.assertRaises(ValueError,self.account_one.deposit, Decimal('-1000'))


    def test_withdrawal_function(self):
        self.account_one.deposit(Decimal('1000'))
        self.account_one.change_pin("2000")
        self.account_one.withdraw(Decimal('100'), "2000")
        self.assertEqual(self.account_one.get_balance(), Decimal('900'))

    def test_withdrawal_function_requires_correct_pin(self):
        self.account_one.deposit(Decimal('1000'))
        self.account_one.change_pin("2000")
        self.assertRaises(ValueError,self.account_one.withdraw, Decimal('100'), "9000")
        # self.assertEqual(self.account_one.get_balance(), Decimal('900'))

    def test_withdrawal_function_does_not_allow_negatives(self):
        self.account_one.deposit(Decimal('1000'))
        self.account_one.change_pin("2000")
        # account_one.withdraw(Decimal('-100'))
        self.assertRaises(ValueError,self.account_one.withdraw, Decimal('-100'), "2000")

    def test_that_withdrawal_function_checks_insufficient_balance(self):
        self.account_one.deposit(Decimal('1000'))
        self.account_one.change_pin("2000")
        # print(account_one.balance)
        self.assertRaises(ValueError,self.account_one.withdraw, Decimal('10000'), "2000")

    def test_that_pin_is_changed(self):
        self.account_one.deposit(Decimal('1000'))
        self.account_one.change_pin("2000")
        self.assertEqual(self.account_one.get_balance(), Decimal('1000'))
        self.assertEqual(self.account_one.pin,"2000")
        self.account_one.withdraw(Decimal('100'), "2000")
        self.assertEqual(self.account_one.get_balance(), Decimal('900'))
        self.assertRaises(ValueError, self.account_one.withdraw, Decimal('100'), "0000")
        self.account_one.change_pin("2060")
        self.assertRaises(ValueError, self.account_one.withdraw, Decimal('100'), "2000")



