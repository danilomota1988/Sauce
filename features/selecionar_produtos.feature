Feature: Selecionar Produto

    Scenario: Selecionar produto "Sauce Labs Backpack"

        Given que acesso o site Sauce Demo
        When preencho os campos de login com usuario standard_user e senha secret_sauce
        Then sou direcionado para a pagina Home

    Scenario: Login com a senha invalida
        Given que acesso o site Sauce Demo
        When preencho os campos de login com usuario standard_user e senha laranja
        Then exibe a mensagem de erro no login

    Scenario Outline: Login com negativo
        Given que acesso o site Sauce Demo
        When preencho os campos de login com usuario <usuario> e senha <senha>
        Then exibe a <mensagem> de erro no login

        Examples:
        | id | usuario       | senha        | mensagem                                                                      |
        | 01 | standard_user | laranja      | Epic sadface: Username and password do not match any user in this service     |
        | 02 | standard_user |              | Epic sadface: Password is required                                            |
        | 03 |               | secret_sauce | Epic sadface: Username is required                                            |
        | 04 | standard      | secret_sauce | Epic sadface: Username and password do not match any user in this service     |
        | 05 | standard      | laranja      | Epic sadface: Username and password do not match any user in this service     |
        | 06 | standard      |              | Epic sadface: Password is required                                            |
        | 07 |               |              | Epic sadface: Username is required                                            |
        | 08 |               | laranja      | Epic sadface: Username is required                                            |
        