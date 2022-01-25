nome = input("Qual seu nome? ")
idade = input("Qual sua idade? ")
idade = int(idade)
maior_de_idade = 18

if idade >= maior_de_idade:
    print("Você já pode tirar sua licença de motorista!")

else:
    print("Você ainda não pode tirar sua licença de motorista! Porque ainda é menor de idade. Ao invés disso,"
          "já pensou em ir assistir Peppa Pig?")
    peppaPig = input("Sim ou Não? ")
    if peppaPig == 'Sim':
        print("Continue assistindo!")
    elif peppaPig == 'Não':
        print("Deveria assistir, fazer algo da sua idade...")
    else:
        print("Escreva com a primeira letra maiúscula e com acentuação.")

    # Obs: Ainda não aprendi return T_T



