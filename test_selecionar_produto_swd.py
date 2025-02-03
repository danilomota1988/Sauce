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


