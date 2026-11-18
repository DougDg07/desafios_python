# Alerta de estoque

Exercício de Python que identifica produtos com estoque baixo e informa quais precisam de reposição.

## Objetivo

Automatizar a conferência de uma lista de produtos.

## Regras

- Produtos com quantidade menor que 5 precisam de reposição.
- O programa exibe o nome e a quantidade desses produtos.
- Ao final, informa quantos produtos precisam de reposição.
- Se nenhum precisar, exibe "Estoque em dia.".

## Conceitos praticados

- Listas e dicionários
- Repetição com for
- Condições com if e else
- Contadores
- Formatação de textos com f-strings

## Como executar

Com o Python instalado, abra o terminal na pasta deste exercício e execute:

```bash
python estoque.py
```

## Resultado esperado

```text
Repor: Cabo HDMI | Quantidade: 3
Repor: Teclado | Quantidade: 0
Repor: Headset | Quantidade: 2
Total de produtos para repor: 3
```

## Casos de teste

- Lista original: três produtos precisam de reposição.
- Produto com quantidade 5: não precisa de reposição.
- Produto com quantidade 0: precisa de reposição.
- Lista vazia: exibe "Estoque em dia.".

## Sobre o desenvolvimento

Solução desenvolvida por mim como exercício de estudo,
com revisão e explicações do ChatGPT.
