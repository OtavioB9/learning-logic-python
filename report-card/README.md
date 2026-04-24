# Impressora de Boletim Escolar

Programa focado em fundamentos de lógica, tipagem de dados e validação de instâncias em Python.

## Como funciona

O código armazena dados de um estudante (nome, idade, status de matrícula e nota) e realiza a verificação do tipo de dado de cada variável, garantindo que as informações sigam o padrão esperado pelo sistema.

## Fluxo de execução

1. Atribui valores a variáveis de diferentes tipos (String, Boolean, Int, Float).
2. Utiliza a função `type()` para identificar a classe de cada variável.
3. Realiza uma validação lógica com `isinstance()` para confirmar se a nota é um valor decimal.
4. Exibe os resultados no console de forma organizada.

## Verificação de Tipos

| Variável | Tipo Esperado | Finalidade |
| :--- | :--- | :--- |
| `name` | `str` | Armazena o nome do aluno. |
| `is_student` | `bool` | Valida se o aluno possui matrícula ativa. |
| `age` | `int` | Armazena a idade em números inteiros. |
| `score` | `float` | Armazena a nota final com casas decimais. |

## Operadores e Validações

* `type()`: Retorna o tipo primitivo do dado.
* `isinstance(valor, tipo)`: Retorna um booleano (True/False) confirmando se o dado pertence à categoria especificada.