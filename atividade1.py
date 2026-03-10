biblioteca = []
livro = {}

while True:
    print('Cadastro de livro')
    print("~~"*30)

    livro['codigo'] = input("codigo: ")
    livro['titulo'] = input("titulo: ")
    livro['autor'] = input("autor: ")
    livro['ano'] = input("ano de publicação: ")
    livro['qtdd'] = int(input("quantidade: "))

    biblioteca.append(livro.copy())

    print("~~"*30)
    resp = input("Deseja continuar (S/N)? ")

    if resp.upper() == "N":
        break

for x in range(len(biblioteca)):
    for y in range(len(biblioteca) - 1):
        if biblioteca[y]['qtdd'] > biblioteca[y + 1]['qtdd']:
            aux = biblioteca[y]
            biblioteca[y] = biblioteca[y + 1]
            biblioteca[y + 1] = aux

for l in biblioteca:
    print("Código:", l['codigo'])
    print("Título:", l['titulo'])
    print("Autor:", l['autor'])
    print("Ano:", l['ano'])
    print("Quantidade:", l['qtdd'])
    print("-" * 30)

