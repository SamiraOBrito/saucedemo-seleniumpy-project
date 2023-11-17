import time
import pytest
from pages.carrinho_page import CarrinhoPage
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
class TestCT003:
    def test_ct003_adicionar_produtos_carrinho(self):
        login_page = LoginPage()
        home_page = HomePage()
        carrinho_page = CarrinhoPage()

        produto_1 = "Sauce Labs Backpack"
        produto_2 = "Sauce Labs Bike Light"

        #Realizando o Login

        login_page.fazer_login("standard_user", "secret_sauce")

        # *** Adicionar a mochila ao carrinho***

        home_page.adicionar_ao_carrinho(produto_1)

        # ***Verificando que o produto foi adicionado***

        home_page.acessar_carrinho()
        carrinho_page.verificar_produto_carrinho_existe(produto_1)

        # *** Clicando em voltar para tela de produtos ***

        carrinho_page.clicar_continuar_comprando()

        # *** Adicionar outro produto ao carrinho ***

        home_page.adicionar_ao_carrinho(produto_2)

        # *** Verificando que os dois produto foi adicionado ao carrinho ***

        home_page.acessar_carrinho()
        carrinho_page.verificar_produto_carrinho_existe(produto_1)
        carrinho_page.verificar_produto_carrinho_existe(produto_2)

