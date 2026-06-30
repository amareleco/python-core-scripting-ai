# 📋 Basic To-Do Manager (Conditionals & List Manipulation)

Um gerenciador de tarefas simples desenvolvido em Python para linha de comando. O projeto permite adicionar, remover, visualizar e consultar tarefas usando estruturas fundamentais da linguagem, como condicionais, listas e pattern matching.

## 🚀 Objetivo do Projeto

Este projeto foi criado para praticar conceitos básicos de Python através de uma aplicação real:

* Uso de `if`, `elif` e `else` para tomada de decisões
* Uso de `match` e `case` para controlar diferentes comandos
* Criação e manipulação de listas
* Adição e remoção de elementos com métodos de lista
* Uso de slicing para acessar partes da lista
* Tratamento seguro de entradas do usuário

## 🛠️ Tecnologias Utilizadas

* Python 3.10+
* Terminal / Linha de comando

## 📌 Funcionalidades

### ➕ Adicionar tarefas

Permite inserir novas tarefas na lista.

Exemplo:

```text
Command: add
Task: estudar Python
Added
```

Também aceita múltiplas tarefas separadas por vírgula:

```text
Task: estudar, praticar, revisar
Added
```

### 👀 Visualizar tarefas

Mostra todas as tarefas cadastradas e uma parte da lista usando slicing.

Exemplo:

```text
Command: view
['estudar Python', 'praticar']
```

### ❌ Remover tarefas

Remove uma tarefa específica.

Caso a tarefa não seja encontrada, o programa remove a última tarefa disponível como alternativa.

### 📊 Consultar estatísticas

Mostra informações básicas sobre a quantidade de tarefas.

Exemplo:

```text
Command: stats
Few: 2
```

### 🚪 Sair do programa

Finaliza a execução:

```text
Command: quit
Bye
```

## ▶️ Como Executar

1. Certifique-se de ter o Python instalado:

```bash
python --version
```

2. Execute o arquivo do projeto:

```bash
python todo_manager.py
```

3. Digite os comandos disponíveis:

```text
add
remove
view
stats
quit
```

## 📚 Conceitos Python Praticados

| Conceito                    | Aplicação no projeto            |
| --------------------------- | ------------------------------- |
| `if/elif/else`              | Decisão de ações e validações   |
| `match/case`                | Controle dos comandos digitados |
| Listas                      | Armazenamento das tarefas       |
| `append()`                  | Adicionar uma tarefa            |
| `extend()`                  | Adicionar várias tarefas        |
| `remove()`                  | Excluir tarefas específicas     |
| `pop()`                     | Remover último item             |
| Slicing `[start:stop:step]` | Exibir partes da lista          |

## 🎯 Possíveis Melhorias Futuras

* Salvar tarefas em um arquivo JSON
* Adicionar prioridades
* Criar sistema de categorias
* Implementar datas de vencimento
* Criar uma interface gráfica

## 📄 Licença

Projeto educacional desenvolvido para prática de programação em Python.
