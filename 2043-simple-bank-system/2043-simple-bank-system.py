class Bank:

    def __init__(self, balance: list[int]):
        self._balance = balance 
        # array of all balances, with each account starting at 1
        # balances are at 10 20 30
        # accounts are 1 2 3
        # account 1 is at balances[0] so to access it -> balances[account-1]

    def is_valid(self, account: int) -> bool:
        if account > 0 and account <= len(self._balance):
            # 1 to amount of accounts "1 2 3 4 5"
            # call self on balance since it came from init
            return True
        else: 
            return False

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if self.is_valid(account1) and self.is_valid(account2) and money <= self._balance[account1-1]:
            self._balance[account1-1] -= money
            self._balance[account2-1] += money
            return True
        else:
            return False

    def deposit(self, account: int, money: int) -> bool:
        if self.is_valid(account):
            self._balance[account-1] += money
            return True
        else:
            return False

    def withdraw(self, account: int, money: int) -> bool:
        if self.is_valid(account) and money <= self._balance[account-1]:
            self._balance[account-1] -= money
            return True
        else:
            return False

    @property
    def balance(self):
        return self._balance # lets outside code access balance safely