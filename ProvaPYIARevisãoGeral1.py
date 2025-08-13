produtos = {}

for i in range(5):
    nome = input(f"Digite o nome do produto {i+1}: ")
    preco = float(input(f"Digite o preço do produto {i+1}: "))
    produtos[nome] = preco 

valor_total = sum(produtos.values())

print(f"O valor total da compra é de R$ {valor_total:.2f}")