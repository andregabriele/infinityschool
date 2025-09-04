tarefas = []
proximo_id = 1

prioridades_validas = {
    1: "muito alta",
    2: "alta",
    3: "média",
    4: "baixa",
    5: "muito baixa"
}

def adicionar_tarefa(nome, descricao, prioridade, categoria):
    global proximo_id
    if prioridade not in prioridades_validas:
        print("Prioridade inválida. Use um número de 1 a 5.")
        return
    tarefa = {
        "id": proximo_id,
        "nome": nome.strip(),
        "descricao": descricao.strip(),
        "prioridade": prioridade,
        "categoria": categoria.strip(),
        "concluida": False
    }
    tarefas.append(tarefa)
    proximo_id += 1
    print("\nTarefa adicionada com sucesso!")

def exibir_tarefa(tarefa):
    prioridade_nome = prioridades_validas[tarefa["prioridade"]]
    status = "Concluída" if tarefa["concluida"] else "Pendente"
    print("ID:        ", tarefa["id"])
    print("Nome:      ", tarefa["nome"])
    print("Descrição: ", tarefa["descricao"])
    print("Prioridade:", prioridade_nome)
    print("Categoria: ", tarefa["categoria"])
    print("Status:    ", status)
    print("-" * 40)

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    print("\n=== LISTA DE TAREFAS ===")
    for tarefa in tarefas:
        exibir_tarefa(tarefa)
    print(f"Total de tarefas: {len(tarefas)}\n")

def buscar_por_id(id_tarefa):
    for t in tarefas:
        if t["id"] == id_tarefa:
            return t
    return None

def marcar_concluida():
    if not tarefas:
        print("Não há tarefas cadastradas.")
        return

    while True:
        print("\n=== TAREFAS ===")
        for t in tarefas:
            status = "Concluída" if t["concluida"] else "Pendente"
            print(f"ID {t['id']}: {t['nome']} ({status})")
        print("0. Cancelar operação")

        try:
            id_tarefa = int(input("Digite o ID da tarefa para marcar como concluída (ou 0 para cancelar): "))
            if id_tarefa == 0:
                print("Operação cancelada.")
                return

            tarefa = buscar_por_id(id_tarefa)
            if tarefa:
                if tarefa["concluida"]:
                    print("Essa tarefa já está concluída. Escolha outra.")
                    continue
                tarefa["concluida"] = True
                print("\nTarefa marcada como concluída!")
                return
            else:
                print("ID não encontrado. Escolha novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

def excluir_tarefa():
    global tarefas  # global declarado no início
    if not tarefas:
        print("Não há tarefas cadastradas.")
        return

    while True:
        print("\n=== TAREFAS ===")
        for t in tarefas:
            status = "Concluída" if t["concluida"] else "Pendente"
            print(f"ID {t['id']}: {t['nome']} ({status})")
        print("0. Cancelar exclusão")

        try:
            id_tarefa = int(input("Digite o ID da tarefa para excluir (ou 0 para cancelar): "))
            if id_tarefa == 0:
                print("Exclusão cancelada.")
                return

            tamanho_inicial = len(tarefas)
            tarefas = [t for t in tarefas if t["id"] != id_tarefa]
            if len(tarefas) < tamanho_inicial:
                print("\nTarefa excluída com sucesso!")
                return
            else:
                print("ID não encontrado. Escolha novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

def filtrar_por_prioridade(prioridade):
    if prioridade not in prioridades_validas:
        print("Prioridade inválida.")
        return
    filtradas = [t for t in tarefas if t["prioridade"] == prioridade]
    if not filtradas:
        print("Nenhuma tarefa com essa prioridade.")
        return
    print(f"\n=== TAREFAS COM PRIORIDADE '{prioridades_validas[prioridade].upper()}' ===")
    for t in filtradas:
        exibir_tarefa(t)

def filtrar_por_categoria():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    categorias = sorted(set([t["categoria"] for t in tarefas]))
    if not categorias:
        print("Nenhuma categoria encontrada.")
        return

    print("\n=== CATEGORIAS DISPONÍVEIS ===")
    for i, cat in enumerate(categorias, start=1):
        print(f"{i}. {cat}")

    try:
        escolha = int(input("Escolha o número da categoria: "))
        if escolha < 1 or escolha > len(categorias):
            print("Número inválido.")
            return
        categoria_escolhida = categorias[escolha - 1]
    except ValueError:
        print("Entrada inválida.")
        return

    filtradas = [t for t in tarefas if t["categoria"] == categoria_escolhida]
    print(f"\n=== TAREFAS NA CATEGORIA '{categoria_escolhida.upper()}' ===")
    for t in filtradas:
        exibir_tarefa(t)

def menu():
    print("\n=== MENU DE TAREFAS ===")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Marcar tarefa como concluída")
    print("4. Excluir tarefa")
    print("5. Filtrar por prioridade")
    print("6. Filtrar por categoria")
    print("0. Sair")

    escolha = input("Escolha uma opção: ").strip()

    if escolha == "1":
        nome = input("Nome da tarefa: ")
        descricao = input("Descrição: ")
        try:
            prioridade = int(input("Prioridade (1=muito alta, 2=alta, 3=média, 4=baixa, 5=muito baixa): "))
        except ValueError:
            print("Entrada inválida.")
            return menu()
        categoria = input("Categoria (digite qualquer nome): ")
        adicionar_tarefa(nome, descricao, prioridade, categoria)

    elif escolha == "2":
        listar_tarefas()

    elif escolha == "3":
        marcar_concluida()

    elif escolha == "4":
        excluir_tarefa()

    elif escolha == "5":
        try:
            prioridade = int(input("Prioridade (1 a 5): "))
            filtrar_por_prioridade(prioridade)
        except ValueError:
            print("Entrada inválida.")

    elif escolha == "6":
        filtrar_por_categoria()

    elif escolha == "0":
        print("Saindo do programa...")
        return

    else:
        print("Opção inválida. Tente novamente.")

    menu() 

if __name__ == "__main__":
    menu()

