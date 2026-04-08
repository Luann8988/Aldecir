def alinhamentoBonito():
    print("~~"*30)
    print("//"*30)
    print("~~"*30)

def opcaoInvalida():
    print("~~"*30)
    print("Opção invalida")
    print("~~"*30)

def ordenar(campo, lista):
    for x in range(1, len(lista)):
        for y in range(len(lista) - 1):
            if lista[y][campo] > lista[y + 1][campo]:
                aux = lista[y]
                lista[y] = lista[y + 1]
                lista[y + 1] = aux

    return lista

def primeiro(lista):
    # empresa
    for x in lista:
        print("~~"*30)
        # nome, anoNasc, sexo, salario, funcao,                      anoEmpre,                          idadeApose
        print(f"Nome :{x['nome']}", end=" ,")
        print(f"Nascimento: {x['anoNasc']}", end=" ,")
        print(f"Sexo: {x['sexo']}", end=" ,")
        print(f"Salario: {x['salario']}", end=" ,")
        print(f"Cargo: {x['funcao']}", end=" ,")
        print(f"Empregado em {x['anoEmpre']}", end=" ,")
        print(f"Aposenta em:{x['idadeApose']} ")
        break

def listar(lista):
    # empresa
    for x in lista:
        print("~~"*30)
        # nome, anoNasc, sexo, salario, funcao,                      anoEmpre,                          idadeApose
        print(f"Nome :{x['nome']}", end=" ,")
        print(f"Nascimento: {x['anoNasc']}", end=" ,")
        print(f"Sexo: {x['sexo']}", end=" ,")
        print(f"Salario: {x['salario']}", end=" ,")
        print(f"Cargo: {x['funcao']}", end=" ,")
        print(f"Empregado em {x['anoEmpre']}", end=" ,")
        print(f"Aposenta em:{x['idadeApose']} ")

def pesquisar(lista, campo = "nome"):
    print("~~"*30)
    nomePesquisa = input("Digite o nome para pesquisa: ")
    encontrado = False
    for x in lista:
        if x[campo].lower() == nomePesquisa.lower():
            print("~~"*30)
            print(f"Nome :{x['nome']}", end=" ,")
            print(f"Nascimento: {x['anoNasc']}", end=" ,")
            print(f"Sexo: {x['sexo']}", end=" ,")
            print(f"Salario: {x['salario']}", end=" ,")
            print(f"Cargo: {x['funcao']}", end=" ,")
            print(f"Empregado em {x['anoEmpre']}", end=" ,")
            print(f"Aposenta em:{x['idadeApose']} ")
            encontrado = True
            break
    if encontrado == False:
        print("~~"*30)
        print(F"{campo} não encontrado.")

# novamente, n vou povoar essa lista n
empresa = [
    {
        'nome': 'Carlos Eduardo Silva',
        'anoNasc': 1985,
        'sexo': 'm',
        'salario': 5200.00,
        'funcao': 'Analista de Sistemas',
        'anoEmpre': 2010,
        'idadeApose': 2045
    },
    {
        'nome': 'Mariana Oliveira Santos',
        'anoNasc': 1990,
        'sexo': 'f',
        'salario': 6800.00,
        'funcao': 'Gerente de Projetos',
        'anoEmpre': 2015,
        'idadeApose': 2045
    },
    {
        'nome': 'João Pedro Almeida',
        'anoNasc': 1978,
        'sexo': 'm',
        'salario': 4100.00,
        'funcao': 'Técnico em Informática',
        'anoEmpre': 2005,
        'idadeApose': 2040
    },
    {
        'nome': 'Ana Beatriz Costa',
        'anoNasc': 1982,
        'sexo': 'f',
        'salario': 7350.00,
        'funcao': 'Diretora de TI',
        'anoEmpre': 2008,
        'idadeApose': 2038
    },
    {
        'nome': 'Roberto Carlos Mendes',
        'anoNasc': 1995,
        'sexo': 'm',
        'salario': 3800.00,
        'funcao': 'Desenvolvedor Júnior',
        'anoEmpre': 2020,
        'idadeApose': 2055
    },
    {
        'nome': 'Fernanda Lima Souza',
        'anoNasc': 1988,
        'sexo': 'f',
        'salario': 5900.00,
        'funcao': 'Arquiteta de Software',
        'anoEmpre': 2012,
        'idadeApose': 2042
    },
    {
        'nome': 'Paulo Henrique Gomes',
        'anoNasc': 1975,
        'sexo': 'm',
        'salario': 8200.00,
        'funcao': 'Coordenador de Infraestrutura',
        'anoEmpre': 2000,
        'idadeApose': 2035
    },
    {
        'nome': 'Juliana Ferreira Dias',
        'anoNasc': 1992,
        'sexo': 'f',
        'salario': 4700.00,
        'funcao': 'Analista de Suporte',
        'anoEmpre': 2018,
        'idadeApose': 2048
    },
    # teste teste teste teste teste teste teste teste teste teste teste teste teste teste
    {
        'nome': 'leo',
        'anoNasc': 1,
        'sexo': 'f',
        'salario': 1.00,
        'funcao': 'ads',
        'anoEmpre': 1,
        'idadeApose': 2
    },
    {
        'nome': 'Lucas Andrade Rocha',
        'anoNasc': 1980,
        'sexo': 'm',
        'salario': 6100.00,
        'funcao': 'Engenheiro de Dados',
        'anoEmpre': 2011,
        'idadeApose': 2046
    }
]
funcionario = dict()

while True:
    print("~~"*30)
    print("escolha uma opção:")
    print("1. Cadastrar funcionario")
    print("2. Listar funcionarios")
    print("3. Pesquisar funcionario")
    print("4. funcionario com o menor salario")
    print("5. funcionario mais velho")
    print("6. media salarial dos funcionario")
    print("7. Sair")
    print("~~"*30)
    opcao = int(input("Opção: "))

    if opcao == 1:
        # inserir daods do funcionario
        print("~~"*30)
        '''(nome, ano de nascimento, sexo, salário, função, ano primeiro emprego), '''
        funcionario['nome'] = input("Nome: ")
        funcionario['anoNasc'] = int(input("Ano de nascimento: "))
# nome, anoNasc, sexo, salario, funcao, anoEmpre, idadeApose
        # validar sexo para idade de aposentadoria
        while True:
            funcionario['sexo'] = input("Sexo: ")
            if funcionario['sexo'].upper() == "M" or funcionario['sexo'].upper() == "F":
                break
            print("insira valor valido F ou M")

        funcionario['salario'] = float(input("Salario: "))
        funcionario['funcao'] = input("Função: ")
        funcionario['anoEmpre'] = int(input("Ano do primeiro emprego: "))

        # calculo do ano de aposentadoria
        if funcionario['sexo'].upper() == "M":
            funcionario["idadeApose"] = funcionario["anoEmpre"] + 35
        else:
            funcionario["idadeApose"] = funcionario["anoEmpre"] + 30

        empresa.append(funcionario.copy())

    elif opcao == 2:
        print("~~"*30)
        # menu de listagem por nome, por idade aposentadoria decrescente e função
        while True:
                print("~~"*30)
                print("escolha tipo de lsitagem:")
                print("1. Por nome")
                print("2. Por idade de aposentadoria")
                print("3. Por função")
                print("4. Sair")
                print("~~"*30)
                opcao = int(input("Opção: "))

                if opcao == 1:
                    # ordena em ordem alfabetica
                    empresa = ordenar('nome', empresa)

                    # exibe lista 
                    listar(empresa)

                elif opcao == 2:
                    # ordena por idade de aposentadoria
                    empresa = ordenar('idadeApose', empresa)

                    # exibe lista
                    listar(empresa)
                elif opcao == 3:
                    # ordena por idade de função
                    empresa = ordenar('funcao', empresa)

                    # exibe lista
                    listar(empresa)
                elif opcao == 4:
                    break
                else:
                    opcaoInvalida()

    elif opcao == 3:
        print("~~"*30)
        while True:
            print("~~"*30)
            print("escolha uma opção:")
            print("1 - Pesquisar por nome")
            print("2 - Pesquisar por telefone")
            print("3 - Voltar")
            opcao = input("Opção: ")

            if opcao == '1':
                pesquisar(empresa, 'nome')

            elif opcao == '2':
                pesquisar(empresa, 'telefone')

            elif opcao == '3':
                break
            else:
                opcaoInvalida()

    elif opcao == 4:
        # organiza por idade
        empresa = ordenar('salario', empresa)
        #  imprimeo o primeiro da lsita
        primeiro(empresa)

    elif opcao == 5:
        # organiza por idade
        empresa = ordenar('anoNasc', empresa)
        #  imprimeo o primeiro da lsita
        primeiro(empresa)

    elif opcao == 6:
        print("~~"*30)
        totalSalario = 0
        for x in range(len(empresa)):
            totalSalario += empresa[x]['salario']
        print(f"media salaria: R${totalSalario /len(empresa)}")

    elif opcao == 7:
        break
    else:
        opcaoInvalida()
