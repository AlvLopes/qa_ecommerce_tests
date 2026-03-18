from pages.login_page import LoginPage
from pages.home_page import HomePage

def test_login_sucesso(page):
    login = LoginPage(page)
    home = HomePage(page)

    login.acessar()
    login.fazer_login("standard_user", "secret_sauce")

    assert home.verificar_login_sucesso()