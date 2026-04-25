# Divisor de Conta

Programa em Python que divide a conta de um restaurante entre amigos, aplicando gorjeta automática de 10%.

---

## Como funciona

O programa solicita os valores gastos em cada categoria, soma tudo em um acumulador (`running_total`), calcula a gorjeta, e divide o total pelo número de pessoas.

---

## Fluxo de execução

1. Lê o número de amigos via `input()`, convertido para inteiro com `int()`
2. Lê os valores de cada categoria via `input()`, convertidos para decimal com `float()`
3. Soma todos os itens no acumulador `running_total`
4. Calcula a gorjeta de 10% sobre o subtotal
5. Adiciona a gorjeta ao `running_total`
6. Divide o total pelo número de pessoas para obter `final_bill`
7. Arredonda o valor por pessoa para 2 casas decimais com `round()`

---

## Variáveis principais

| Variável | Tipo | Descrição |
|---|---|---|
| `running_total` | `float` | Acumulador — começa em 0, recebe os valores progressivamente |
| `num_of_friends` | `int` | Número de pessoas que dividem a conta |
| `appertizers` | `float` | Valor gasto com aperitivos |
| `main_courses` | `float` | Valor gasto com pratos principais |
| `drinks` | `float` | Valor gasto com bebidas |
| `tip` | `float` | Gorjeta calculada (10% do subtotal), arredondada com `round()` |
| `final_bill` | `float` | Total com gorjeta dividido pelo número de pessoas |
| `each_pays` | `float` | Valor final por pessoa, arredondado para 2 casas decimais |

---

## Funções e operadores utilizados

| Função / Operador | Descrição |
|---|---|
| `input()` | Lê texto digitado pelo usuário no terminal |
| `int()` | Converte string para número inteiro |
| `float()` | Converte string para número decimal |
| `round(valor, 2)` | Arredonda um número para 2 casas decimais |
| `print(f'...')` | Exibe texto formatado; `:.2f` dentro das chaves garante 2 casas decimais |
| `+=` | Operador de acumulação: `x += y` é equivalente a `x = x + y` |

---

## Exemplo de saída

```
Valor total da conta 6170.0
Gorjeta (10%) 617.0
Valor total da conta com gorjeta: R$ 6787.00
O valor total dividido por pessoa ficou R$ 754.11
Cada pessoa deve pagar R$ 754.11
```
**Este script foi feito com base em um exercício da plataforma, mas modificado para aplicar o conceito estudado de "f string"**
