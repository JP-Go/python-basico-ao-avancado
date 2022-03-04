from threading import Thread, Lock
from time import sleep

"""
# Criando uma thread (Classe que herda de Thread)
class PrintingThread(Thread):
    def __init__(self, text: str, timeout: int) -> None:
        self.text = text
        self.timeout = timeout

        # Não esquecer do super
        super().__init__()

    # O metodo run precisa ser definido
    def run(self) -> None:
        sleep(self.timeout)
        print(self.text)


# Cria a thread
t1 = PrintingThread("A thread called 1", 5)
t2 = PrintingThread("A thread called 2", 4)

t1.start()
t2.start()


def slow_function(text: str, timeout: int) -> None:
    sleep(timeout)
    print(text)


# Outra maneira de criar uma thread
t3 = Thread(target=slow_function, args=("Hello mon", 5))
t3.start()

for i in range(6):
    print(f"{i+1} second{'s' if i +1 > 1 else ''} {'has' if i+1<=1 else 'have'} passed")
    sleep(1)
"""

"""
def slow_function(text: str, timeout: int) -> None:
    sleep(timeout)
    print(text)


# Outra maneira de criar uma thread
t1 = Thread(target=slow_function, args=("Thread 1: -- Urgh!", 5))

c = 1
t1.start()
# Thread.is_alive(): Se a thread ainda estiver sendo executada, retorna True
while t1.is_alive():
    print(f"waiting the inevitable death of Thread 1 {'.' * c}")
    sleep(1)
    c += 1
    if c == 5:
        # Thread.join(): Faz a tarefa da Thread ser executada na Thread principal (Não para a execução da Thread)
        t1.join()

print("We're gathered here today to mourn the passing of thread1")
"""


class Ticket:
    def __init__(self, stock) -> None:
        self.stock = stock
        # Um lock para não deixar executar o código
        self.lock = Lock()

    def buy(self, quantity):
        # Não permite a execução do método enquanto a thread é executada
        self.lock.acquire()
        if self.stock < quantity:
            print("No ticket in stock")
            # Permite a execução do método (lembrar de soltar antes de retornar)
            self.lock.release()
            return

        sleep(1)

        self.stock -= quantity
        print(f"Bought {quantity} ticket(s). {self.stock=}")
        # Permite a execução do método
        self.lock.release()


if __name__ == "__main__":
    tickets = Ticket(10)

    # Cria uma lista de Threads para armazenar
    threads: list[Thread] = []
    for i in range(1, 6):
        t = Thread(target=tickets.buy, args=(i,))
        threads.append(t)

    for t in threads:
        print("Processing")
        t.start()

    executing = True
    # Enquanto estive executando, manter-se no loop
    while executing:
        executing = False
        for t in threads:
            if t.is_alive():
                executing = True
                break

    print(tickets.stock)
