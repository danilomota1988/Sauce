# 1 - Biblioteca / Imports
import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'que acesso o site Sauce Demo')
def step_impl(context):
    context.driver = webdriver.Chrome()                 # Instanciar o objeto Selenium WebDriber especializado para o Chrome
    context.driver.maximize_window()                    # Maximizar a janela do navegador
    context.driver.implicitly_wait(10)                  # Esperar
    context.driver.get("https://www.saucedemo.com")     # abrir o navegador no endereço do site alvo

# Preencher com usuario e senha
@when(u'preencho os campos de login com usuario {usuario} e senha {senha}')
def step_impl(context, usuario, senha):
    context.driver.find_element(By.ID, "user-name").send_keys(usuario)
    context.driver.find_element(By.ID, "password").send_keys(senha)
    context.driver.find_element(By.ID, "login-button").click()

# Preencher com usuario em branco e senha
@when(u'preencho os campos de login com usuario  e senha {senha}')
def step_impl(context, senha):
    context.driver.find_element(By.ID, "password").send_keys(senha)
    context.driver.find_element(By.ID, "login-button").click()

# Preencher com usuario, mas deixar senha em branco
@when(u'preencho os campos de login com usuario {usuario} e senha ')
def step_impl(context, usuario):
    context.driver.find_element(By.ID, "user-name").send_keys(usuario)
    context.driver.find_element(By.ID, "login-button").click()

# Clica no botão de login sem ter peenchido o usuário e senha
@when(u'preencho os campos de login com usuario  e senha ')
def step_impl(context):
    context.driver.find_element(By.ID, "login-button").click()

# Preencher com usuario e senha usando (IF)
@when(u'digito os campos de login com usuario {usuario} e senha {senha} com IF')
def step_impl(context, usuario, senha):
    if usuario != '<branco>':
        context.driver.find_element(By.ID, "user-name").send_keys(usuario)
        # se o usuário estiver em <branco> não há ação de preenchimento
    if senha != '<branco>':
        context.driver.find_element(By.ID, "password").send_keys(senha)
        # se a senha estiver em <branco> não há ação de preenchimento

    context.driver.find_element(By.ID, "login-button").click()

# Redireciona o usuário para a Home
@then(u'sou direcionado para a pagina Home')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".title").text == "Products"
    #time.sleep(5)
    
    # teardown / encerramento
    context.driver.quit()

@then(u'exibe a mensagem de erro no login')
def step_impl(context):
    # Validar mensagem de erro
    assert context.driver.find_element(By.CSS_SELECTOR, "h3").text == "Epic sadface: Username and password do not match any user in this service"

# Verifica a mensagem para o scenario outline
@then(u'exibe a {mensagem} de erro no login')
def step_impl(context, mensagem):
    # Validar mensagem de erro
    assert context.driver.find_element(By.CSS_SELECTOR, "h3").text == mensagem

    # teardown / encerramento
    context.driver.quit()
