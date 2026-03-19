class HomePage:
    def __init__(self, page):
        self.page = page
        self.produto = ".inventory_item"

    def verificar_login_sucesso(self):
        return self.page.locator(self.produto).count() > 0

    def adicionar_produto_carrinho(self):
        self.page.click("text=Add to cart")

    def ir_para_carrinho(self):
        self.page.click(".shopping_cart_link")

    def obter_titulo_pagina(self):
        return self.page.locator(".title").text_content()