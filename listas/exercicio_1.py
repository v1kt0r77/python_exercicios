# Criando uma lista vazia chamada "numeros"
numeros = []

# Pedindo ao usuário para digitar 5 números inteiros e adicionando-os à lista
for i in range(5):
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)

# Imprimindo a lista de números
print("Lista de números:", numeros)

# Calculando a soma de todos os números da lista
soma = sum(numeros)
print("Soma dos números:", soma)

# Encontrando o maior número da lista
maior_numero = max(numeros)
print("Maior número da lista:", maior_numero)

# Encontrando o menor número da lista
menor_numero = min(numeros)
print("Menor número da lista:", menor_numero)

# Calculando a média dos números da lista
media = soma / len(numeros)
print("Média dos números da lista:", media)
