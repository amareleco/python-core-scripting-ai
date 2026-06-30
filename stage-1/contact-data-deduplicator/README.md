# 📊 Contact & Data Deduplicator (Dicts, Tuples, Sets)

## 📌 Sobre o Projeto

Este projeto é um programa de gerenciamento de contatos desenvolvido em Python para demonstrar como trabalhar com **tuplas, conjuntos (sets) e dicionários (dicts)**.

O programa recebe uma coleção de nomes e números, remove contatos duplicados, organiza os dados em uma estrutura de fácil consulta e realiza comparações entre diferentes grupos de contatos usando operações matemáticas de conjuntos.

---

## 🎯 Objetivos

* Praticar criação e manipulação de **tuplas** para armazenar dados ordenados e imutáveis.
* Utilizar **sets** para garantir que contatos duplicados sejam eliminados.
* Criar e gerenciar **dicionários** para relacionar nomes e números.
* Aprender métodos de dicionários como:

  * `keys()`
  * `values()`
  * `items()`
  * `get()`
  * `update()`
* Aplicar operações de conjuntos:

  * `union()`
  * `intersection()`
  * `difference()`
  * `symmetric_difference()`

---

## 🛠️ Tecnologias Utilizadas

* Python 3.x

---

## 📂 Estrutura do Projeto

```
contact-deduplicator/
│
├── contact_manager.py
└── README.md
```

---

## ▶️ Como Executar

1. Certifique-se de ter o Python instalado:

```bash
python --version
```

2. Execute o programa:

```bash
python contact_manager.py
```

---

## 📋 Funcionamento

O programa segue este fluxo:

1. Recebe uma lista de contatos contendo nomes e números.
2. Converte os dados em uma coleção de tuplas.
3. Usa um `set` para remover registros duplicados.
4. Cria um `dictionary` para mapear nome → número.
5. Exibe o registro organizado.
6. Compara grupos de contatos usando operações de conjuntos.

---

## 💻 Exemplo de Entrada

```python
[
    ("Alice", "555-0101"),
    ("Bob", "555-0102"),
    ("Alice", "555-0101"),
    ("Cara", "555-0103")
]
```

---

## ✅ Exemplo de Saída

```
Registry:
Alice -> 555-0101
Bob -> 555-0102
Cara -> 555-0103

Common: {'Alice', 'Cara'}
Only new: {'Bob', 'David'}
All contacts: {'Alice', 'Cara', 'Bob', 'David'}
```

---

## 📚 Conceitos Aprendidos

### Tuples

Usadas para armazenar pares fixos de informações:

```python
("Alice", "555-0101")
```

Como são imutáveis, ajudam a proteger dados que não devem ser alterados.

---

### Sets

Usados para eliminar duplicações automaticamente:

```python
unique_contacts = set()
```

Exemplo:

```
Alice
Alice
Bob
```

Resultado:

```
Alice
Bob
```

---

### Dictionaries

Permitem consultas rápidas através de pares chave/valor:

```python
contacts = {
    "Alice": "555-0101"
}
```

Consulta:

```python
contacts.get("Alice")
```

Resultado:

```
555-0101
```

---

## 🚀 Possíveis Melhorias Futuras

* Salvar contatos em arquivos JSON ou CSV.
* Criar uma interface gráfica.
* Permitir adicionar e remover contatos pelo usuário.
* Implementar busca por nome ou número.
* Criar testes automatizados.

---

## 👨‍💻 Nível do Projeto

**Beginner — Python Fundamentals**

Projeto criado para praticar estruturas de dados essenciais do Python.
