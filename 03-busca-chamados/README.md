# Busca de chamados por ID

Exercício de Python que simula a lógica de consulta de
um chamado de suporte, preparando conceitos usados em APIs.

## Objetivo

Criar uma função que recebe uma lista de chamados e um ID,
retornando os dados encontrados ou uma mensagem de erro.

## Regras

- Se o ID existir, retornar um dicionário com código 200
  e os dados do chamado.
- Se não existir, retornar código 404 e a mensagem
  "Chamado nao encontrado".
- Preservar a lista original.
- Funcionar também com uma lista vazia.

Os códigos são valores no dicionário.
Este exercício ainda não utiliza um servidor HTTP.

## Conceitos praticados

- Listas e dicionários
- Funções e parâmetros
- Repetição com for
- Condições com if
- Retorno de resultados com return

## Como executar

Com o Python instalado, abra o terminal na pasta do exercício:

```bash
python chamados.py
```

Não é necessário instalar bibliotecas externas.

## Resultado esperado

Para a consulta ao ID 2:

```python
{
    "codigo": 200,
    "dados": {
        "id": 2,
        "titulo": "Instalar impressora",
        "status": "concluido"
    }
}
```

## Casos de teste

| Consulta | Resultado esperado |
|---|---|
| ID 2 | Código 200 e dados de Instalar impressora |
| ID 3 | Código 200 e dados de Monitor sem imagem |
| ID 99 | Código 404 e mensagem de erro |
| Lista vazia e ID 1 | Código 404 e mensagem de erro |

## Sobre o desenvolvimento

Solução desenvolvida por mim como exercício de estudo.
