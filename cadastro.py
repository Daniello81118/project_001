
cadastro = {}

def cadastrar_usuario():
    nome = input("Digite o nome: ")
    email = input("Digite o email: ")
    telefone = input("Digite o telefone: ")
    
    cadastro[email] = {"Nome": nome, "Email": email, "Telefone": telefone}
    print("Usuário cadastrado com sucesso!")

def mostrar_usuario(email):
    if email in cadastro:
        usuario = cadastro[email]
        print("Nome:", usuario["Nome"])
        print("Email:", usuario["Email"])
        print("Telefone:", usuario["Telefone"])
    else:
        print("Usuário não encontrado.")

while True:
    print("\nOpções:")
    print("1. Cadastrar novo usuário")
    print("2. Mostrar dados de um usuário")
    print("3. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        cadastrar_usuario()
    elif opcao == "2":
        email = input("Digite o email do usuário que deseja visualizar: ")
        mostrar_usuario(email)
    elif opcao == "3":
        break
    else:
        print("Opção inválida. Tente novamente.")
