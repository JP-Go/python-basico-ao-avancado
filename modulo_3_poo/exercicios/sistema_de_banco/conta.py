from abc import ABC, abstractmethod
from typing import Union

num = Union[int, float]


def check_if_number(value: object) -> None:
    if not isinstance(value, int or float):
        raise ValueError("Value has to be nit or float")


class Account(ABC):
    def __init__(self, agency: int, acc_number: int) -> None:
        self._agency = agency
        self._acc_number = acc_number
        self._balance: num = 0

    @property
    def agency(self) -> int:
        """The agency property."""
        return self._agency

    @agency.setter
    def agency(self, value: int) -> None:
        self._agency = value

    @property
    def balance(self) -> num:
        """The balance property."""
        return self._balance

    @balance.setter
    def balance(self, value: num) -> None:
        self._balance = value

    @property
    def acc_number(self):
        """The acc_number property."""
        return self._acc_number

    @acc_number.setter
    def acc_number(self, value):
        self._acc_number = value

    def deposit(self, amount: num) -> None:
        self.balance += amount

    @abstractmethod
    def withdraw(self, amount: num) -> None:
        pass

    def __str__(self):
        return f"Tipo: {self.__class__.__name__}, Agência: {self.agency}, Conta: {self.acc_number}, Saldo:{self.balance}"


class SavingsAccount(Account):
    def withdraw(self, value: num) -> bool:
        check_if_number(value)
        if not self.balance >= value:
            print(f"Can't withdraw more than {self.balance}")
            return False
        self.balance -= value
        return True


class CheckingAccount(Account):
    def __init__(self, agency: int, acc_number: int, limit: float = 100) -> None:
        super().__init__(agency, acc_number)
        self._limit = limit

    @property
    def limit(self) -> num:
        """The limit property."""
        return self._limit

    @limit.setter
    def limit(self, value: num) -> None:
        self._limit = value

    def withdraw(self, amount: num) -> bool:
        if not (self.balance + self.limit) >= amount:
            print(f"Can't widhdraw more than {self.limit + self.balance}")
            return False

        self.balance -= amount
        return True
