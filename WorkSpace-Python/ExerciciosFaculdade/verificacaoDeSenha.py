print("Informe os dados abaixo para concluir o cadastro.")
usuarioCadastrado = input("Login: ")
senhaCadastrada = input("Senha: ")
verificador = 0
while verificador != 1:
    print("\nEntrar no email.")
    usuario = input("Login: ")
    senha = input("Senha: ")

    if usuario == usuarioCadastrado and senha == senhaCadastrada:
        print("Voce entrou!")
        verificador = 1
    else:
        print("Usuario ou senha incorreta, tente novamente.")

print("FIM")