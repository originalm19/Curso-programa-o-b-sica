cont=0
quant=0
while cont!=10:        #enquanto a variavel cont for diferente de 10, pergutar nome,idade e sexo
    nome=input("Digite um nome: ")
    idade=int(input("Digite a idade: "))
    sexo=input("Digite o sexo, 'M' para masculino ou 'F' para feminino: ")
    cont = cont + 1
    if(sexo=="M" and idade==21):  #se tiver a idade de 21 anos e o sexo for masculino, adicionar +1 a variavel quant
        quant = quant + 1
if(cont==10):    #se a variavel cont chegar a 10, imprimir o valor da variavel quant
    print("O resultado é: ", quant) 
           
    
            
            
