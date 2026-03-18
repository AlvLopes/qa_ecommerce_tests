from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.carrinho_page import CarrinhoPage

def test_adicionar_ao_carrinho(page):
    login = LoginPage(page)
    home = HomePage(page)
    carrinho = CarrinhoPage(page)

    login.acessar()
    login.fazer_login("standard_user", "secret_sauce")

    home.adicionar_produto_carrinho()
    home.ir_para_carrinho()

    assert carrinho.verificar_produto_no_carrinho()