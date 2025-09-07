#Escopo

a = 1
b = 2

def soma_num(var1, var2):
    s=var1+var2
    return s


def imprime(x_vezes):
    for i in range (x_vezes):
        print (i)    
    

resultado = soma_num(a, b)
print(resultado)
# imprime(500)