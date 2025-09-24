class BankAccount:
    def __init__(self, account_number, owner, balance=0.0):
        if not account_number or not isinstance(account_number, str):
            raise ValueError("Account number must be a non-empty string.")
        if not owner or not isinstance(owner, str):
            raise ValueError("Owner name must be a non-empty string.")
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")

        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance

    def transfer(self, target_account, amount):
        if not isinstance(target_account, BankAccount):
            raise TypeError("Target account must be a BankAccount instance.")
        if amount <= 0:
            raise ValueError("Transfer amount must be greater than zero.")
        if amount > self.balance:
            raise ValueError("Insufficient funds for transfer.")

        self.withdraw(amount)
        target_account.deposit(amount)
        return self.balance, target_account.balance
