lista_compras = []


num_produtos = int(input('Quantos produtos você deseja adicionar: '))

for i in range(num_produtos):
    produto = input('Nome do Produto: ')
    quantidade = int(input('Quantidade: '))
    lista_compras.append([produto,quantidade])

print('Lista de Compras: ')
for produto, quantidade in lista_compras:
    print(f"Produto: {produto} - Qtd: {quantidade}")
                        