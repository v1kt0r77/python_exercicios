print("Bem vindo ")
par=0
impar=0
iteracao=0
while iteracao<5:
    numero=int(input('Informe um número: '))
    if numero%2==0:
        print('Seu número é par')
        par+=1
    else:
        print('Seu número é ímpar')
        impar+=1
    iteracao+=1
print(f'{par} são pares')
print(f'{impar} são ímpares')