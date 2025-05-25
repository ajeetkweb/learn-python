# test_bank.py
import unittest
from bank import BankAccount

class TestBankAccount(unittest.TestCase):
    
    def setUp(self):
        self.acc = BankAccount(100)
    
    def test_deposit(self):
        self.acc.deposit(50)
        self.assertEqual(self.acc.balance, 150)

    def test_withdraw_success(self):
        self.acc.withdraw(30)
        self.assertEqual(self.acc.balance, 70)

    def test_withdraw_failure(self):
        with self.assertRaises(ValueError):
            self.acc.withdraw(200)


if __name__ == "__main__":
    unittest.main()
