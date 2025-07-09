# Resumo

## Capítulo 1: Introdução a Algoritmos e Variáveis

### ✅ **Aula 1.1: O que é um algoritmo? Pseudocódigo e fluxogramas**

**Resumo:**
Um **algoritmo** é um conjunto de passos finitos e ordenados para resolver um problema. Pode ser descrito como texto (pseudocódigo) ou visualmente (fluxograma).

**Pseudocódigo exemplo (verificar se um número é positivo):**

```
Início
  Ler número
  Se número > 0 então
    Escreva "Positivo"
  Senão
    Escreva "Negativo ou zero"
Fim
```

**Python equivalente:**

```python
numero = int(input("Digite um número: "))
if numero > 0:
    print("Positivo")
else:
    print("Negativo ou zero")
```

### Links úteis

https://www.youtube.com/watch?v=H6OFlBu5d20

---

### ✅ **Aula 1.2: Fluxogramas usando Mermaid**

**Resumo:**
Fluxogramas são diagramas que representam a lógica de um algoritmo. Usamos formas como **retângulos** (ações), **losangos** (decisões), **setas** (fluxo).

**Exemplo Mermaid (verifica se número é par):**

````markdown
```mermaid
flowchart TD
    A[Início] --> B[Ler número]
    B --> C{número % 2 == 0?}
    C -->|Sim| D[Mostrar \"Par\"]
    C -->|Não| E[Mostrar \"Ímpar\"]
    D --> F[Fim]
    E --> F
```
````

---

### ✅ **Aula 1.3: Variáveis e tipos de dados (inteiros, strings, booleanos)**

**Resumo:**
Variáveis são nomes usados para armazenar valores na memória. Cada valor pode ser de um tipo:

- `int` → número inteiro
- `str` → texto (string)
- `bool` → verdadeiro ou falso

**Exemplo em Python:**

```python
nome = "Lucas"           # str
idade = 16               # int
maior_idade = idade >= 18  # bool

print(nome, idade, maior_idade)
```

---

### ✅ **Aula 1.4: Operadores matemáticos e lógicos**

**Resumo:**

- Operadores matemáticos: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- Operadores lógicos: `and`, `or`, `not`

**Exemplo em Python:**

```python
a = 10
b = 3

print("Soma:", a + b)            # 13
print("Divisão inteira:", a // b)  # 3
print("Resto:", a % b)           # 1

print("É par e > 5?", a % 2 == 0 and a > 5)
```

---

### ✅ **Aula 1.5: Entrada e saída de dados**

**Resumo:**

- **Entrada**: `input()` → Lê valor digitado pelo usuário
- **Saída**: `print()` → Exibe algo na tela

**Exemplo em Python:**

```python
nome = input("Qual seu nome? ")
print("Olá,", nome)
```
