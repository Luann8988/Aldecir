agenda = list()
contato = dict()

while True:
    print('==' * 30)
    print('Agencia de Informações')
    print("1 - Cadastrar Contato")
    print("2 - Listar Contato")
    print("3 - Pesquisar Contato")
    print("4 - Sair")
    print("==" * 40)

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        if len(agenda) == 10:
            print("Agenda Lotada (Máximo 10 Pessoas)")
        else:
            contato['nome'] = input("Nome: ")
            contato['idade'] = input("Idade: ")
            contato['cep'] = input("CEP: ")
            contato['cidade'] = input("Cidade: ")
            contato['telefone'] = input("Telefone: ")

            agenda.append(contato.copy())
            print("Contato cadastrado!")

    elif opcao == 2:
        print("1 - Ordem Alfabética")
        print("2 - Ordem por Telefone")

        tipo = int(input("Escolha uma dessas: "))

        if tipo == 1:
            for x in range(1, len(agenda)):
                for y in range(len(agenda) - 1):
                    if agenda[y]['nome'] > agenda[y + 1]['nome']:
                        aux = agenda[y]
                        agenda[y] = agenda[y + 1]
                        agenda[y + 1] = aux

        elif tipo == 2:
            for x in range(1, len(agenda)):
                for y in range(len(agenda) - 1):
                    if agenda[y]['telefone'] > agenda[y + 1]['telefone']:
                        aux = agenda[y]
                        agenda[y] = agenda[y + 1]
                        agenda[y + 1] = aux

        for x in range(len(agenda)):
            print("-----")
            print(f"Nome: {agenda[x]['nome']}")
            print(f"Idade: {agenda[x]['idade']}")
            print(f"CEP: {agenda[x]['cep']}")
            print(f"Cidade: {agenda[x]['cidade']}")
            print(f"Telefone: {agenda[x]['telefone']}")

    elif opcao == 3:
        print("1 - Pesquisar por Nome")
        print("2 - Pesquisar por Telefone")

        busca = int(input("Escolha: "))

        if busca == 1:
            nome = input("Digite o nome: ")
            for x in range(len(agenda)):
                if agenda[x]['nome'] == nome:
                    print("Contato Encontrado")
                    print(agenda[x])

        elif busca == 2:
            tel = input("Digite o telefone: ")
            for x in range(len(agenda)):
                if agenda[x]['telefone'] == tel:
                    print("Contato Encontrado")
                    print(agenda[x])

    elif opcao == 4:
        print("Saindo...")
        break