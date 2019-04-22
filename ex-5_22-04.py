#valor=int(input("Insira um número: "))
#num=valor%valor
#num1=valor%1
#if num==1 and num1==valor:
    #print("O número ", valor, "é um número primo.")
#else:
    #print("O número", valor, "não é um número primo.")
num=int(input("Digite um número: "))
div=0
for contagem in range(1,num+1):
    if num%contagem==0:
        div=div+1
if div==2:
    print("É número primo")
else:
    print("Não é número primo")
