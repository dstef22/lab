class Account:
    def __init__(self, name: str) -> None:
        """
        Function to set up account object
        :param name: Account name
        :return: None
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        Function to increment the account balance
        :param amount: Amount to increment
        :return: Boolean value True if successful, False if unsuccessful
        """
        if amount <= 0:
            return False
        else:
            self.__account_balance += amount
            return True

    def withdraw(self, amount: float) -> bool:
        """
        Function to decrement the account balance
        :param amount: Amount to decrement
        :return: Boolean value True if successful, False if unsuccessful
        """
        if amount <= 0 or amount > self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self) -> float:
        """
        Function to show current account balance
        :return: Float value, current account balance
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Function to show current account name
        :return: String, current account name
        """
        return self.__account_name
