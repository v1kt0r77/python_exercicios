n=int(input("Informe quantos números serão calculados a média: "))
soma = 0
iteracao = 1
while iteracao<=n:
    numb=float(input("Digite um número: "))
    soma += numb
    iteracao += 1
print(f"O valor da média é igual a : {soma/n}")
