import flet as ft

def main(page: ft.Page):
    page.title = "Software de Venda"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    # Lista para armazenar os produtos
    produtos = []

    # Função para adicionar produto
    def adicionar_produto(e):
        nome = nome_produto.value
        preco = float(preco_produto.value)
        quantidade = int(quantidade_produto.value)
        total = preco * quantidade

        produtos.append({
            "nome": nome,
            "preco": preco,
            "quantidade": quantidade,
            "total": total
        })

        # Limpar campos de entrada
        nome_produto.value = ""
        preco_produto.value = ""
        quantidade_produto.value = ""

        # Atualizar a lista de produtos
        atualizar_lista_produtos()

    # Função para atualizar a lista de produtos
    def atualizar_lista_produtos():
        lista_produtos.controls.clear()
        for produto in produtos:
            lista_produtos.controls.append(
                ft.Text(f"{produto['nome']} - {produto['quantidade']} x R${produto['preco']:.2f} = R${produto['total']:.2f}")
            )
        page.update()

    # Função para calcular o total da venda
    def calcular_total(e):
        total_venda = sum(produto['total'] for produto in produtos)
        total_venda_text.value = f"Total da Venda: R${total_venda:.2f}"
        page.update()

    # Função para finalizar a venda
    def finalizar_venda(e):
        produtos.clear()
        lista_produtos.controls.clear()
        total_venda_text.value = "Total da Venda: R$0.00"
        page.update()

    # Campos de entrada para o produto
    nome_produto = ft.TextField(label="Nome do Produto", width=300)
    preco_produto = ft.TextField(label="Preço Unitário", width=300)
    quantidade_produto = ft.TextField(label="Quantidade", width=300)

    # Botão para adicionar produto
    btn_adicionar = ft.ElevatedButton("Adicionar Produto", on_click=adicionar_produto)

    # Lista de produtos
    lista_produtos = ft.Column()

    # Botão para calcular o total
    btn_calcular_total = ft.ElevatedButton("Calcular Total", on_click=calcular_total)

    # Texto para exibir o total da venda
    total_venda_text = ft.Text("Total da Venda: R$0.00")

    # Botão para finalizar a venda
    btn_finalizar_venda = ft.ElevatedButton("Finalizar Venda", on_click=finalizar_venda)

    # Layout da página
    page.add(
        nome_produto,
        preco_produto,
        quantidade_produto,
        btn_adicionar,
        lista_produtos,
        btn_calcular_total,
        total_venda_text,
        btn_finalizar_venda
    )

# Executar o aplicativo
ft.app(target=main)
