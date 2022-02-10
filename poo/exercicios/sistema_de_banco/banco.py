from cliente import Client
from conta import Account


class Bank:
    def __init__(self, agency: int) -> None:
        self._clients: list[Client] = []
        self._accounts: list[Account] = []
        self._agencies = [agency]

    @property
    def agencies(self) -> list[int]:
        """The agency property."""
        return self._agencies

    @agencies.setter
    def agencies(self, value: list[int]) -> None:
        self._agencies = value

    @property
    def accounts(self) -> list[Account]:
        """The agency property."""
        return self._accounts

    @accounts.setter
    def accounts(self, value: list[Account]) -> None:
        self._accounts = value

    @property
    def clients(self) -> list[Client]:
        """The agency property."""
        return self._clients

    @clients.setter
    def clients(self, value: list[Client]) -> None:
        self._clients = value

    def add_agency(self, agency_number: int) -> None:
        self.agencies.append(agency_number)

    def register_account(self, client: Client) -> None:
        """Creates a new account for bank

        :params client: a client that belongs to th bank
        :params account: the client's account
        :rtype: None
        """
        if client.account.agency not in self.agencies:
            self.agencies.append(client.account.agency)
        self.accounts.append(client.account)
        self.clients.append(client)

    def authenticate(self, client: Client):
        is_client_in_bank = client in self.clients
        is_account_in_bank = client.account in self.accounts
        is_agency_from_bank = client.account.agency in self.agencies
        return is_account_in_bank and is_agency_from_bank and is_client_in_bank

    def __str__(self) -> str:
        return f"Banco: Clientes {len(self.clients)}; \n Agencias: {len(self.agencies)} \n Contas:{len(self.accounts)}"
