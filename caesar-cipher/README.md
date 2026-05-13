# Caesar Cipher

Implementação da cifra de César em Python.

## O que faz

Cifra e decifra textos deslocando cada letra do alfabeto por um número definido de posições.

## Como funciona

- `caesar(text, shift, encrypt=True)` — função principal; aceita letras maiúsculas e minúsculas
- `encrypt(text, shift)` — atalho para cifragem
- `decrypt(text, shift)` — atalho para decifragem
- Valida se o shift é inteiro e está entre 1 e 25

## Exemplo

```python
encrypted = encrypt("Hello World", 5)  # → "Mjqqt Btwqi"
decrypted = decrypt(encrypted, 5)      # → "Hello World"
```

## Tecnologias

- Python 3
- `str.maketrans` e `str.translate` para substituição de caracteres
