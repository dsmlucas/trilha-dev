#Instrução Break - Aula 40

print("Antes de entrar no laço")
for item in range(10):
    if(item==6):
        print("A condição estabelecida retornou true")
        break
print("Depois de ter entrado no laço")


#Instrução Continue - Aula 41
print()
print("Início")
i = 10
while(i<10):
    if(i%2==0):
        continue
    if(i>5) :
        break
    print(i)
else:
    print("else")
print("fim")
print()