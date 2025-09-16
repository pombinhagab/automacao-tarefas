# Automação de Tarefas com Python

Este repositório contém scripts Python desenvolvidos como parte da **Jornada Python**, um intensivo de 4 dias. Este projeto corresponde à **Aula 1** do programa. O objetivo do "case" desta aula foi criar um script para cadastrar produtos em um sistema de uma empresa (já existente nos dados fornecidos).
O projeto utiliza `PyAutoGUI` para simular interações do usuário (cliques e digitação) e `pandas` para manipulação de dados.

> **Objetivo:** Este projeto também serviu como prática para treinar automação de tarefas com Python, simulação de interações com sistemas web e manipulação de dados automatizada.

---

## Funcionalidades

### `main.py`

Script principal para automação de login e cadastro de produtos em uma plataforma web da empresa:

* Abre um navegador configurável (ex.: Firefox) e acessa um URL específico.
* Realiza login com credenciais fornecidas.
* Lê dados de produtos de um arquivo `produtos.csv`.
* Cadastra produtos automaticamente na plataforma, preenchendo formulários.

### `pegarposicao.py`

Utilitário para identificar coordenadas de tela:

* Exibe uma notificação solicitando que o usuário posicione o mouse.
* Após um breve atraso, imprime as coordenadas X e Y do cursor no console.
* Útil para configurar cliques precisos em `main.py`.

---

## Tecnologias Utilizadas

* **Python**
* **pyautogui** – Automação de GUI, teclado e mouse.
* **pandas** – Leitura e manipulação de dados (CSV).
* **time** – Introdução de delays para garantir execução correta das ações.
* **winotify** – Exibição de notificações no Windows (`pegarposicao.py`).

---

## Como Usar

### Pré-requisitos

* Python 3.x instalado.
* Instalar dependências:

```bash
pip install -r requirements.txt
```

### Configuração

1. **`main.py`**:

   * Ajuste as variáveis `site`, `navegador`, `email` e `senha` para seu ambiente.

   > **Obs:** O padrão já irá funcionar normalmente.

   * Garanta que `produtos.csv` esteja no mesmo diretório.
   * Ajuste as coordenadas de clique (`pyautogui.click(X, Y)`) conforme a resolução da sua tela e layout do site.

   > **Obs:** Caso seu monitor seja 1920x1080, o padrão já irá funcionar normalmente.

2. **`produtos.csv`**:

   * Deve conter as colunas: `codigo`, `marca`, `tipo`, `categoria`, `preco_unitario`, `custo`, `obs`.

   > **Obs:** Contém um arquivo normalizado e já funcional para testes.

   * Cada linha representa um produto a ser cadastrado.

### Execução

* Executar script de automação:

```bash
python main.py
```

* Obter coordenadas do mouse (para configuração e depuração):

```bash
python pegarposicao.py
```
