class Account:
    def __init__(self, name: str) -> None:
        """Initialize an account with a name and balance of 0."""
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """Deposit the specified amount into the account."""
        if amount > 0:
            self.__account_balance += amount
            return True
        return False

    def withdraw(self, amount: float) -> bool:
        """Withdraw the specified amount from the account."""
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def get_balance(self) -> float:
        """Return the account balance."""
        return self.__account_balance

    def get_name(self) -> str:
        """Return the account name."""
        return self.__account_name
