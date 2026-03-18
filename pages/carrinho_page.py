class CarrinhoPage:
    def __init__(self, page):
        self.page = page

    def verificar_produto_no_carrinho(self):
        return self.page.locator(".cart_item").is_visible()

    def ir_para_checkout(self):
        self.page.click("text=Checkout")