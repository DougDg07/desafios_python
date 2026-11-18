produtos = [
    {"nome": "Cabo HDMI", "quantidade": 3},
    {"nome": "Mouse", "quantidade": 12},
    {"nome": "Teclado", "quantidade": 0},
    {"nome": "Adaptador USB", "quantidade": 5},
    {"nome": "Headset", "quantidade": 2},
]

# Conta quantos produtos precisam de reposição.
total = 0

for produto in produtos:
    # Quantidades de 0 a 4 precisam de reposição.
    if produto["quantidade"] < 5:
        print(f"Repor: {produto['nome']} | Quantidade: {produto['quantidade']}")
        total += 1

# Exibe o resultado após analisar todos os produtos.
if total == 0:
    print("Estoque em dia.")
else:
    print(f"Total de produtos para repor: {total}")
