# Relatório de vendas confirmadas

Exercício de Python que analisa vendas e gera um resumo dos pedidos pagos.

## Objetivo

Calcular o faturamento e a quantidade de unidades vendidas,
considerando apenas vendas com status "pago".

## Regras

- Ignorar vendas pendentes ou canceladas.
- Calcular o subtotal de cada venda paga: quantidade × preço unitário.
- Exibir o produto e seu subtotal.
- Somar as unidades vendidas e o faturamento.
- Se não houver vendas pagas, exibir "Nenhuma venda paga.".

## Conceitos praticados

- Listas e dicionários
- Repetição com for
- Condições com if e else
- Operações matemáticas
- Contadores e acumuladores
- Formatação de textos com f-strings

## Como executar

Com o Python instalado, abra o terminal na pasta deste exercício:

```bash
python vendas.py
```

Não é necessário instalar bibliotecas externas.

## Resultado esperado

Para os dados de exemplo e valores sem casas decimais:

```text
Mouse | Subtotal: R$ 100
Cabo HDMI | Subtotal: R$ 60
Adaptador USB | Subtotal: R$ 50
Unidades vendidas: 7
Faturamento total: R$ 210
```

## Casos de teste

| Entrada | Resultado esperado |
|---|---|
| Lista original | 7 unidades e faturamento de R$ 210 |
| Apenas a venda paga de Mouse | 2 unidades e faturamento de R$ 100 |
| Apenas uma venda pendente | Nenhuma venda paga. |
| Lista vazia | Nenhuma venda paga. |

## Sobre o desenvolvimento

Solução desenvolvida por mim como exercício de estudo,
com revisão e explicações 
