# Software de Vendas em Flet

[![MIT License](https://img.shields.io/badge/license-MIT-007EC7.svg?style=flat-square)](/LICENSE)
![Poetry](https://img.shields.io/badge/Poetry-%233B82F6.svg?style=for-the-badge&logo=poetry&logoColor=0B3D8D)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

Este é um software simples de vendas desenvolvido com Flet, uma biblioteca Python que permite criar interfaces gráficas multiplataforma usando Flutter.

## Funcionalidades

- Adicionar produtos com nome, preço e quantidade
- Visualizar lista de produtos adicionados
- Calcular total da venda
- Finalizar venda e limpar dados

## Instalação via Poetry

1. Crie um novo projeto Poetry:
```bash
poetry new software-vendas
```

2. Entre no diretório do projeto:
```bash
cd software-vendas
```

3. Adicione a dependência do Flet:
```bash
poetry add flet
```

4. Verifique a versão instalada:
```bash
poetry run flet --version
```

## Executando o Projeto

Para rodar como aplicativo desktop:
```bash
poetry run python software_vendas.py
```

Para rodar como aplicativo web:
```bash
poetry run flet run -w software_vendas.py
```

## Estrutura do Código

O software utiliza os seguintes componentes do Flet:

- `ft.TextField`: Para entrada de dados do produto
- `ft.ElevatedButton`: Para botões de ação
- `ft.Column`: Para organizar a lista de produtos
- `ft.Text`: Para exibir informações

### Funções Principais

- `adicionar_produto()`: Adiciona um novo produto à lista
- `atualizar_lista_produtos()`: Atualiza a exibição dos produtos
- `calcular_total()`: Calcula o valor total da venda
- `finalizar_venda()`: Limpa todos os dados da venda atual

## Possíveis Erros e Soluções

Se você encontrar o erro relacionado à biblioteca `libmpv.so.1` no Ubuntu:

```bash
error while loading shared libraries: libmpv.so.1: cannot open shared object file
```

Siga estes passos para resolver:

1. Instale as dependências necessárias:
```bash
sudo apt install libmpv-dev libmujs-dev libjpeg62
```

2. Crie um link simbólico:
```bash
cd /usr/lib/x86_64-linux-gnu
sudo ln -s libmpv.so libmpv.so.1
```

## Referências

- [Documentação oficial do Flet](https://flet.dev/)
- [Python com Flet](https://phylos.net/2023-07-10/python-com-flet)
- [Gerenciamento de dependências com Poetry](https://python-poetry.org/docs/)
