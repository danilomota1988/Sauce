# 1 - Bibliotecas
from selenium import webdriver
from selenium.webdriver.common.by import By

# 2 - Classe (Opcional)
class Teste_Produtos():

    #2.1 atributos
    url = "https://www.saucedemo.com"                   # endereço do site
    #2.2 Funções e métodos

   
    def setup_method(self, method):                       # método de inicialização dos testes
        self.driver = webdriver.Chrome()            # intanciar o objeto Webdriver como chrome
        self.driver.implicitly_wait(10)         # define o tempo de espera padrão por elementos

    def teardown_method(self, method):                    # método de finalização dos testes         
        self.driver.quit()                         # encerra / destrói o objeto do Selenium Webdriver

    def test_selecionar_produto(self):                                      # método de teste
        self.driver.get(self.url)                                                   # abre o navegador
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")     # escreve no campo
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")       # escreve no campo
        self.driver.find_element(By.CSS_SELECTOR, "input.submit-button.btn_action").click()       # click no botão login

        # Transição de tela

        assert self.driver.find_element(By.CSS_SELECTOR, "span.title").text == "Products"          # COnfirma se o elemento tem o texto esperado
        assert self.driver.find_element(By.CSS_SELECTOR, "div.page_wrapper div.inventory_container div.inventory_list div.inventory_item:nth-child(1) div.inventory_item_description div.inventory_item_label a:nth-child(1) > div.inventory_item_name").text == "Sauce Labs Backpack"          # COnfirma se o elemento tem o texto esperado
        assert self.driver.find_element(By.CSS_SELECTOR, "div.page_wrapper div.inventory_container div.inventory_list div.inventory_item:nth-child(1) div.inventory_item_description div.pricebar > div.inventory_item_price").text == "$29.99"          # COnfirma se o elemento tem o texto esperado


