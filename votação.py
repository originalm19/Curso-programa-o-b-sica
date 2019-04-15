print("Votação")
idade=int(input("Qual a sua idade ? "))
if(idade>=18 and idade<=65):
    print("Você está autorizado a votar !")
elif(idade>=16 and idade<=17 or idade>65):
    print("Sua participação não é obrigatória !")
else:
    print("Você não está autorizado a votar !")