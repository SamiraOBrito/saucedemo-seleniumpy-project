import time
import pytest
from pages.carrinho_page import CarrinhoPage
from pages.checkout_page import CheckoutPage
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
class TestCT004:
    def test_ct004_finalizar_compras(self):
        login_page = LoginPage()
        home_page = HomePage()
        carrinho_page = CarrinhoPage()
        checkout_page = CheckoutPage()

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

        # *** Clicando em checkout ***
        carrinho_page.clicar_em_checkout()

        # *** Preencher formulario para o chekout ***
        checkout_page.preencher_informacoes_do_checkout("Bruna", "Oliveira","03441560")
        checkout_page.clicar_continue()
        checkout_page.clicar_finish()

        # *** Verificar se a compra foi realizada com sucesso
        checkout_page.veriicar_se_a_compra_foi_realizada_com_sucesso()

        #Voltar para a pagina Home
        home_page.voltar_para_pagina_home()






