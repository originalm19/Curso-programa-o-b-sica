for contagem in range(0,10):
    nome=input("Digite um nome: ")
    idade=int(input("Digite a idade: "))
    sexo=input("Digite M se for homem e F se for mulher.")
    if idade > 21 and sexo=="M":
        print("Seu nome é", nome)
    
