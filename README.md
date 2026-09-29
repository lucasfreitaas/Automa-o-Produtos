# Automação de Cadastro de Produtos com Python

Este projeto automatiza o cadastro de produtos em um sistema web, eliminando a necessidade de inserção manual de dados.

## O que o projeto faz

O script lê uma planilha de produtos (`produtos.csv`) e preenche automaticamente o formulário do sistema, cadastrando cada produto com as informações:

- **Código** do produto
- **Marca**
- **Tipo**
- **Categoria**
- **Preço unitário**
- **Custo**
- **Observações** (quando houver)

## Como funciona

1. O script abre o navegador Chrome automaticamente
2. Acessa o sistema de cadastro via link
3. Realiza o login
4. Lê os dados da planilha `produtos.csv`
5. Preenche e envia o formulário para cada produto da lista

## Tecnologias utilizadas

- **Python**
- **PyAutoGUI** — para controle do mouse e teclado
- **Pandas** — para leitura e manipulação da planilha CSV

## Como executar

1. Instale as dependências:
   ```bash
   pip install pyautogui pandas
   ```

2. Certifique-se de que o arquivo `produtos.csv` está na mesma pasta do script.

3. Execute o script principal:
   ```bash
   python codigo.py
   ```

> **Atenção:** Não mexa no mouse ou teclado enquanto o script estiver rodando, pois o PyAutoGUI controla esses dispositivos durante a execução.

## Arquivos do projeto

| Arquivo        | Descrição                                              |
|----------------|--------------------------------------------------------|
| `codigo.py`    | Script principal que realiza a automação               |
| `auxiliar.py`  | Script auxiliar para capturar coordenadas da tela      |
| `produtos.csv` | Base de dados com os produtos a serem cadastrados      |
