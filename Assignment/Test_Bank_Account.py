import unittest
from bank_account import BankAccount


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.acc1 = BankAccount("12345", "Alice", 100.0)
        self.acc2 = BankAccount("67890", "Bob", 50.0)

    def test_that_account_initialization_sets_correct_values(self):
        self.assertEqual(self.acc1.account_number, "12345")
        self.assertEqual(self.acc1.owner, "Alice")
        self.assertEqual(self.acc1.balance, 100.0)

    def test_that_deposit_function_increases_balance(self):
        self.acc1.deposit(50)
        self.assertEqual(self.acc1.get_balance(), 150.0)

    def test_that_deposit_function_raises_error_for_negative_amount(self):
        try:
            self.acc1.deposit(-20)
            self.fail("Expected ValueError")
        except ValueError:
            pass

    def test_that_withdraw_function_reduces_balance(self):
        self.acc1.withdraw(50)
        self.assertEqual(self.acc1.get_balance(), 50.0)

    def test_that_withdraw_function_raises_error_for_insufficient_funds(self):
        try:
            self.acc1.withdraw(200)
            self.fail("Expected ValueError")
        except ValueError:
            pass

    def test_that_withdraw_function_raises_error_for_invalid_amount(self):
        try:
            self.acc1.withdraw(0)
            self.fail("Expected ValueError")
        except ValueError:
            pass

    def test_that_transfer_function_moves_money_between_accounts(self):
        self.acc1.transfer(self.acc2, 40)
        self.assertEqual(self.acc1.get_balance(), 60.0)
        self.assertEqual(self.acc2.get_balance(), 90.0)

    def test_that_transfer_function_raises_error_for_negative_amount(self):
        try:
            self.acc1.transfer(self.acc2, -10)
            self.fail("Expected ValueError")
        except ValueError:
            pass

    def test_that_transfer_function_raises_error_for_insufficient_funds(self):
        try:
            self.acc1.transfer(self.acc2, 200)
            self.fail("Expected ValueError")
        except ValueError:
            pass

    def test_that_transfer_function_raises_error_for_invalid_target_account(self):
        try:
            self.acc1.transfer("NotAnAccount", 20)
            self.fail("Expected TypeError")
        except TypeError:
            pass


if __name__ == "__main__":
    unittest.main()
