import time

import pytest

from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown" )
class TestCT02:
    def test_ct02_login_invalido(self):

        # Instancia os objetos a serem usados no teste
        login_page = LoginPage()

        # Faz login
        login_page.fazer_login("standard_user", "error123")

        # Verificar se o login não foi realizado e se a mensagem de erro apareceu
        login_page.verificar_mensagem_erro_login()
        time.sleep(3)
