while True:
    nome = input("Digite o seu nome: ")
    idade = input("Digite sua Idade: ")
    print(nome)
    print(idade)
    if nome == "" or idade == "":
        print("Você deixou campos vazios")
    else:
        print(f"Seu nome é {nome}")
        print(f"Seu nome invertido é {nome[::-1]}")
        if ' ' in nome:
            print('Seu nome contém espaços')
        else:
            print('Seu nome não contém espaços')
        print(f"A primenta letra do seu nome é {nome[0]}")
        print(f"A última letra do seu nome é {nome[-1]}")
        break


