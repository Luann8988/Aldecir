funcionarios = []

while True:
    print("1 - Cadastrar")
    print("2 - Listagem")
    print("3 - Buscar Funcionários")
    print("4 - Menor Salário")
    print("5 - Funcionário mais velho")
    print("6 - Média de salário")
    print("7 - Sair")

    opcao = int(input("Escolha uma opção: "))
    print("==" * 30)

    if opcao == 1:
        nome = input("Digite seu nome: ")
        nasc = (input("Digite seu ano de nascimento: ")) 
        sexo = input("Sexo (M/F): ")
        salario = float(input("Digite seu salário: "))
        funcao = input("Digite sua função: ")
        primeiroE = int(input("Digite o ano do seu primeiro emprego: "))

        idade = 2026 - nasc
        print(f"Sua idade é {idade} anos:")
        temp_trabalhado = 2026 - primeiroE

        if sexo == "M":
            aposentadoria = primeiroE + 35
        else:
            aposentadoria = primeiroE + 30

        funcionario = {
            "nome": nome,
            "nascimento": nasc,
            "sexo": sexo,
            "salario": salario,
            "funcao": funcao,
            "primeiroE": primeiroE,
            "idade": idade,
            "aposentadoria": aposentadoria
        }

        funcionarios.append(funcionario)
        print("Funcionário cadastrado com sucesso!")
        print("=" * 40)

    elif opcao == 2:
        for f in funcionarios:
            print(f)

    elif opcao == 7:
        print("Encerrando programa...")
        break
