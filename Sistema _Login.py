from time import sleep

print("***********************")
print("Bem vindo ao SISTEM UP!")
print("***********************")
print()

sleep (2)

usuarios = {'Admin': '123456', 'Comprador': '789123', 'Vendedor': '456789', 'Rh': '102030'}

while True:
    login = input("Login: ").capitalize().strip()
    tentativa = 0
    if login == 'Admin':
        tentativa_total = 3
        for tentativa in range(3):
            senha = input('Senha: ')
            if senha == usuarios['Admin']:
                print()
                print('***Login efetuado com sucesso***')
                print()
                while True:
                    sleep (2)
                    menu = int(input('\nMenu: \n1-Cadastro de novos usuários \n2-Remoção de usuários \n3-Imprimir lista de usuários \n4-Troca de senha de administrador \n5-Sair \n\nOpção escolhida: '))
                    print()
                    if menu == 1:
                        login_novo = input("Digite o funcionário a ser adicionado: ").capitalize().strip()
                        senha_cadastro = input('Digite a senha para cadastro: ').capitalize().strip()
                        usuarios[login_novo] = senha_cadastro
                        print(f'Login "{login_novo}" adicionado com sucesso!')
                        print()
                    elif menu == 2:
                        excluir = input("Digite o funcionário a ser removido: ")
                        print()
                        if excluir in usuarios:
                            usuarios.pop(excluir)
                            print(f"***Usuário {excluir} foi removido do sistema.***")
                            print()
                        else:
                            print(f"***Usuário {excluir} não existe no sistema.***")
                            print()
                    elif menu == 3:
                        print('Os usuários do sistema são:')
                        for usuario, senha in usuarios.items():
                            print(usuario)
                    elif menu == 4:
                        senha_antiga = input('Senha anterior: ').strip()                        
                        if senha_antiga == usuarios['Admin']:
                            nova_senha = input("Nova senha: ").strip()
                            repetir_nova_senha = input("Nova senha: ").strip()
                            if nova_senha == repetir_nova_senha:
                                usuarios['Admin'] = nova_senha
                                print()
                                print("Senha alterada com sucesso!")
                            else:
                                print()
                                print("Senhas não conferem, retorne a sua solicitação.")
                        else:
                            print("Senha incorreta, retorne a sua solicitação.")
                            print()
                    elif menu == 5:
                        print("Obrigado por usar nosso sistema!")
                        print()
                        break
                    else:
                        print("Opção inválida. \nTente novamente!")
                        print()
                break 
            else:
                tentativa_total -= 1
                if tentativa_total > 0:
                    print()
                    print('Senha incorreta!')
                    print()
                    print(f'Essa é sua tentativa de numero {tentativa + 1}. \nTentativas disponíveis: {tentativa_total}.')
                    print()
                else:
                    print()
                    print(f'Essa é sua tentativa de numero 3.')
                    print('Todas as tentativas de login foram utilizadas. Entre em contato com a empresa responsável pelo sistema.')
                    print()
                    break
    elif login in usuarios:
        tentativa_total = 3
        senha_digitada = input("Senha: ")
        senha = usuarios.get(login)
        if senha_digitada == senha:
            print()
            print("***Login efetuado com sucesso***")
            print("***Obrigado por utilizar o nosso sistema... até mais!!!***")
            print()
            break
        elif senha_digitada != senha:
            tentativa_total -= 1
            if tentativa_total > 0:
                print()
                print('Senha incorreta!')
                print()
                print(f'Essa é sua tentativa de numero {tentativa + 1}. \nTentativas disponíveis: {tentativa_total}.')
                print()
            else:
                print()
                print(f'Essa é sua tentativa de numero 3.')
                print('Todas as tentativas de login foram utilizadas. Entre em contato com o Administrador do sistema.')
                print()
                break
    else:
        print()        
        print("Usuário não cadastrado, tente novamente.")
        print()