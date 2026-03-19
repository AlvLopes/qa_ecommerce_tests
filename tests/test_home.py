from pages.login_page import LoginPage
from pages.home_page import HomePage

def test_titulo_pagina_apos_login(page):
    login = LoginPage(page)
    home = HomePage(page)

    login.acessar()
    login.fazer_login("standard_user", "secret_sauce")

    titulo = home.obter_titulo_pagina()

    assert titulo == "Products"