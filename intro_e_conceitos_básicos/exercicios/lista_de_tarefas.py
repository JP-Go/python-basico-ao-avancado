def add_task(tasks_list: list[str] = []) -> list[str]:
    task = input("Digite a nova tarefa e pressione enter: ")
    tasks_list.append(task)
    return tasks_list


def list_tasks(tasks_list: list[str]) -> None:
    if not tasks_list:
        print("Vocẽ não tem tarefas ainda!")
        return
    for i, task in enumerate(tasks_list):
        print(f"Tarefa {i+1}: {task}")


def undo_task(tasks_list: list[str], undone_tasks: list[str]) -> None:
    if not tasks_list:
        print("Não há tarefas a serem desfeitas")
        return
    undone_tasks.append(tasks_list.pop())


def redo_task(tasks_list: list[str], undone_tasks: list[str]) -> None:
    if not undone_tasks:
        print("Não há tarefas desfeitas a refazer")
        return
    tasks_list.append(undone_tasks.pop())


def main():
    print("Bem vindo a lista de tarefas!")
    tarefas = []
    redo = []
    actions = {0: add_task, 1: list_tasks, 2: undo_task, 3: redo_task}
    while True:
        print("Digite:")
        print("\t0: para adicionar uma tarefa")
        print("\t1: para listar as tarefas")
        print("\t2: para desfazer a última adição")
        print("\t3: para refazer a última adição desfeita")
        try:
            action = int(input("O que você deseja fazer: "))
            if not (0 <= action <= 3):
                raise ValueError
        except ValueError:
            print("Por favor digite uma ação válida!")
        else:
            if 0 <= action <= 1:
                actions[action](tarefas)
            else:
                actions[action](tarefas, redo)
        print()


if __name__ == "__main__":
    main()
