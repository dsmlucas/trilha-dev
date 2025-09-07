#Blocos de Instrução na prática

num1= int(input("Digite um número: "))

if(num1 >15) :
    print("O valor é maior que 15!")
    if(num1<=30) :
         print("O valor é maior do que 10 porem menor que 30.")
    else:
        if(num1>50) :
            print("O valor é maior que 30, porem menor ou igual a  50.")
else:
    if(num1>5) :
        print ("O número é menor que 15, porem maior que 5.")
        if(num1==8) :
            print ("O número é igual a 8.")

    else: 
        print ("O valor é menor que 5.") 

