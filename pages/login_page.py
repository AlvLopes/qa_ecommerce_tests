class LoginPage:
    def __init__(self, page):
        self.page = page
        self.input_user = "#user-name"
        self.input_password = "#password"
        self.btn_login = "#login-button"

    def acessar(self):
        self.page.goto("https://www.saucedemo.com/")

    def fazer_login(self, usuario, senha):
        self.page.fill(self.input_user, usuario)
        self.page.fill(self.input_password, senha)
        self.page.click(self.btn_login)