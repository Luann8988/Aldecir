biblioteca = list()
livro = dict()
qtdlivros = 0

while True:
    print("Cadastro dos Livros")
    print("~~~" * 30)
    livro['codigo'] = input ('codigo: ')
    livro['titulo'] = input ('titulo: ')
    livro['autor']  = input ('autor  : ')
    livro['ano']    = input ('ano de pulicação : ')
    livro['qtdd']   = input ('quantidade : ')
    
    #adicionar o aluno e a turma 
    biblioteca.append(livro.copy())
    
    print('~~' * 40)
    resp = input("Deseja continuar (S/N)")
    
    if resp.upper() == "N":
        break
    
    for x in range(1,len(biblioteca)):
        for y in range(len(biblioteca) - 1,): 
            if biblioteca[y]['qtdd'] < biblioteca[y + 1]['qtdd']:
                aux = biblioteca[y] = biblioteca[y + 1]
                biblioteca[y + 1] = aux
                
                print(f"{biblioteca[0]['codigo']}")
                print(f"{biblioteca[0]['titulo']}")
                print(f"{biblioteca[0]['autor']}")
                print(f"{biblioteca[0]['ano']}")
                print(f"{biblioteca[0]['qtdd']}")
                
                for x in range(len(biblioteca)):
                    qtdlivros += (biblioteca[x]['qtdd'])
                    
                    print("~~" * 30)
                    print(f" QUANTIDADE TOTAL DE LIVROS{qtdlivros}")
            
    
    

    
    