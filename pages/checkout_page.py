from selenium.webdriver.common.by import By
import conftest
from pages.base_page import BasePage


class CheckoutPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.campo_first_name = (By.ID, "first-name")
        self.campo_last_name = (By.ID, "last-name")
        self.campo_zip_postalcode = (By.ID, "postal-code")
        self.botao_continue = (By.ID, "continue")
        self.botao_finish = (By.ID, "finish")
        self.compra_realizado_com_sucesso = (By.XPATH, "//h2 [@class='complete-header' and text()='Thank you for your order!']")

    def preencher_informacoes_do_checkout(self, firstname, lastname, postalcode):
        self.escrever(self.campo_first_name, firstname)
        self.escrever(self.campo_last_name, lastname)
        self.escrever(self.campo_zip_postalcode, postalcode)

    def clicar_continue(self):
        self.clicar(self.botao_continue)

    def clicar_finish(self):
        self.clicar(self.botao_finish)

    def veriicar_se_a_compra_foi_realizada_com_sucesso(self):
        self.verificar_se_elemento_existe(self.compra_realizado_com_sucesso)










