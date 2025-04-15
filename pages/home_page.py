from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage


class HomePage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.titulo_pagina = (By.XPATH, "//span[@class='title']")

    def verificar_login_sucedido(self):
        self.verificar_elemento_existente(self.titulo_pagina)