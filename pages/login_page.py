import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_login_message = (By.XPATH, "//*[@data-test='error']")

    def fazer_login(self, usuario, senha):
        self.escrever(self.username_field, usuario)
        self.escrever(self.password_field, senha)
        self.clicar(self.login_button)

    def verificar_mensagem_erro_login_existe(self):
        self.verificar_elemento_existente(self.error_login_message)

    def verificar_texto_mensagem_erro_login_existe(self, texto_esperado):
        texto_encontrado = self.pegar_texto_elemento(self.error_login_message)
        assert texto_encontrado == texto_esperado, f"O texto encontrado foi '{texto_encontrado}', mas era esperado o texto '{texto_esperado}'."