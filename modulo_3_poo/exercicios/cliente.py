from conta import Account


class Person:
    """A class that represents a person with a name and an age"""

    def __init__(self, name: str, age: int) -> None:
        """Creates a person

        :params name: The name of the person
        :params age: The age of the person
        """
        self._name = name
        self._age = age

    @property
    def name(self) -> str:
        return self._name

    @property
    def age(self) -> int:
        return self._age

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @age.setter
    def age(self, value: int) -> None:
        self._age = value


class Client(Person):
    """A class that represents a client of some store, inherits from person"""

    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)

    @property
    def account(self):
        """The clients's account in a bank"""
        return self._account

    @account.setter
    def account(self, value):
        self._account = value

    def set_client_account(self, account: Account):
        self.account = account

    def __str__(self) -> str:
        return f"Nome: {self.name}, idade: {self.age} conta: {self.account}"
