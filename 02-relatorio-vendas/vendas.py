vendas = [
    {"produto": "Mouse", "quantidade": 2, "preco_unitario": 50, "status": "pago"},
    {"produto": "Teclado", "quantidade": 1, "preco_unitario": 120, "status": "pendente"},
    {"produto": "Cabo HDMI", "quantidade": 3, "preco_unitario": 20, "status": "pago"},
    {"produto": "Headset", "quantidade": 1, "preco_unitario": 150, "status": "cancelado"},
    {"produto": "Adaptador USB", "quantidade": 2, "preco_unitario": 25, "status": "pago"},
]

unidades = 0
faturamento = 0
vendas_pagas = 0

for venda in vendas:
    if venda["status"] == "pago":
        subtotal = venda["quantidade"] * venda["preco_unitario"]
        print(f"{venda['produto']} | Subtotal: R$ {subtotal}")
        unidades += venda["quantidade"]
        faturamento += subtotal
        vendas_pagas += 1

if vendas_pagas == 0:
    print("Nenhuma venda paga.")
else:
    print(f"Unidades vendidas: {unidades}")
    print(f"Faturamento total: R$ {faturamento}")
