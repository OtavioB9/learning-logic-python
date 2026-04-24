# Gerador de Perfil de Empregado

Este programa em Python automatiza a criação de cartões de identificação de funcionários, processando dados pessoais e extraindo informações específicas de códigos internos via fatiamento (slicing).

## Como funciona

O programa centraliza informações como nome, idade e salário, gera uma string formatada (f-string) e utiliza técnicas de fatiamento para decompor o código do funcionário em departamento, ano e ID.

## Fluxo de execução

1. Define variáveis de texto e numéricas para o perfil.
2. Formata as informações em uma apresentação única usando f-strings.
3. Processa a string `employee_code` para extrair sub-informações.
4. Utiliza índices positivos para capturar início e meio da string.
5. Utiliza índice negativo (`-3:`) para capturar os últimos caracteres da string.

## Tabela de Fatiamento (Slicing)

| Dado Extraído | Código de Slicing | Descrição |
| :--- | :--- | :--- |
| **Departamento** | `[0:3]` | Captura os 3 primeiros caracteres (Ex: DEV). |
| **Ano** | `[4:8]` | Captura o ano contido no meio do código. |
| **Iniciais/Meio** | `[9:11]` | Captura identificadores intermediários. |
| **ID Numérico** | `[-3:]` | Captura os 3 dígitos finais de trás para frente. |

## Principais Funções

* `f-strings`: Utilizadas para injetar variáveis diretamente dentro de textos de forma limpa.
* `Slicing`: Técnica para recortar partes específicas de uma string através de índices.