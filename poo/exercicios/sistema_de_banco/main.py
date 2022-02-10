"""
Arquivo principal de POO com python, utilizando todos os conceitos aprendidos até agora
"""
from cliente import Client
from conta import SavingsAccount, CheckingAccount
from banco import Bank


def main():

    itau = Bank(1111)
    cliente1 = Client("Rodrigo", 19)
    cliente2 = Client("Luiz", 39)
    cliente3 = Client("Maria", 45)
    cc1 = SavingsAccount(1111, 21200)
    cc2 = CheckingAccount(1111, 21201)
    cc3 = CheckingAccount(1110, 21200)
    cliente1.set_client_account(cc1)
    cliente2.set_client_account(cc2)
    cliente3.set_client_account(cc3)

    itau.register_account(cliente1)
    itau.register_account(cliente2)

    for client in [cliente1, cliente2, cliente3]:
        # Depósitos
        client.account.deposit(200)
        print(f"Cliente {client.name} depositou 200")

        # Saques
        if not itau.authenticate(client):
            print(f"Cliente {client.name} não pode sacar")
        else:
            op_success = client.account.withdraw(50)
            print(f"Cliente {client.name} {'sacou 50' if op_success else 'não sacou'}")

        if not itau.authenticate(client):
            print(f"Cliente {client.name} não pode sacar")
        else:
            op_success = client.account.withdraw(200)
            print(f"Cliente {client.name} {'sacou 200' if op_success else 'não sacou'}")
        print(client)
        print("#########################")

    cliente2.account.withdraw(50)
    print(cliente2)
    cliente2.account.withdraw(0.01)
    print(cliente2)


if __name__ == "__main__":
    main()
