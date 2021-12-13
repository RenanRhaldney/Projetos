cadastroLogin = input("Informe seu login para cadastro. ")
cadastroSenha = input("Informe sua senha para cadastro. ")

while True:
    login = input("Login: ")
    senha = input("senha: ")
    if login == cadastroLogin:
        if senha == cadastroSenha:
            print("Login efetuado com sucesso.")
            break
    else:
        print("Login ou senha invalido. ")

print("FIM...")