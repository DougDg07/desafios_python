chamados = [
    {"id": 1, "titulo": "Computador sem internet", "status": "aberto"},
    {"id": 2, "titulo": "Instalar impressora", "status": "concluido"},
    {"id": 3, "titulo": "Monitor sem imagem", "status": "aberto"},
]

def buscar_chamado(chamados, id_procurado):
    for chamado in chamados:
        if chamado["id"] == id_procurado:
            return {"codigo": 200, "dados": chamado}

    return {"codigo": 404, "erro": "Chamado nao encontrado"}

print(buscar_chamado(chamados, 2))
