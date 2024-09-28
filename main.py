
import os
import time

# Dicionário para armazenar os nomes de usuários e senhas
usuarios = {}


def cadastrar_usuario():
    """
    Cadastra um novo usuário com nome de usuário e senha.
    """
    try:
        usuario = input("Digite o nome de usuário: ")
        senha = input("Digite a senha: ")

        if usuario in usuarios:
            print("Usuário já cadastrado!")
            time.sleep(2)
        else:
            usuarios[usuario] = senha
            print("Usuário cadastrado com sucesso!")
            time.sleep(2)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        time.sleep(2)


def login():
    """
    Realiza o login do usuário, se o nome e senha estiverem corretos.
    """
    try:
        usuario = input("Digite o nome de usuário: ")
        senha = input("Digite a senha: ")

        if usuario in usuarios and usuarios[usuario] == senha:
            print("Login realizado com sucesso!")
            time.sleep(2)
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("1. Curiosidade sobre carros")
                print("2. Últimas corridas")
                print("3. Próximas corridas")
                print("4. Times")
                print("5. Sair")

                escolha = input("Escolha uma opção: ")
                os.system('cls' if os.name == 'nt' else 'clear')
                if escolha == "1":
                    curiosidades_sobre_carros()
                elif escolha == "2":
                    ultimas_corridas()
                elif escolha == "3":
                    proximas_corridas()
                elif escolha == "4":
                    times()
                elif escolha == "5":
                    print("Saindo...")
                    time.sleep(2)
                    break
                else:
                    print("Opção inválida!")
                    input("Pressione Enter para continuar...")
        else:
            print("Usuário não encontrado ou senha incorreta!")
            time.sleep(2)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        time.sleep(2)


def curiosidades_sobre_carros():
    """
    Exibe curiosidades sobre carros de Fórmula E e Fórmula 1.
    """
    try:
        print("Curiosidades sobre carros de Fórmula E e Fórmula 1:")
        with open('curiosidade.txt', 'r', encoding='utf-8') as arq:
            for linha in arq:
                print(linha.strip())
        input("Pressione Enter para voltar ao menu...")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        input("Pressione Enter para voltar ao menu...")


def ultimas_corridas():
    """
    Exibe as últimas corridas de Fórmula E.
    """
    try:
        print("Últimas corridas de Fórmula E:")
        with open('ult-corridas.txt', 'r', encoding='utf-8') as arqu:
            for linh in arqu:
                print(linh.strip())
        print()
        input("Pressione Enter para voltar ao menu...")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        input("Pressione Enter para voltar ao menu...")


def proximas_corridas():
    """
    Exibe as próximas corridas de Fórmula E.
    """
    try:
        print("Próximas corridas de Fórmula E:")
        with open('Proximas-corridas.txt', 'r', encoding='utf-8') as arqui:
            for lin in arqui:
                print(lin.strip())
        print()
        input("Pressione Enter para voltar ao menu...")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        input("Pressione Enter para voltar ao menu...")


def times():
    """
    Exibe os times de Fórmula E e suas vitórias.
    """
    try:
        print("Times de Fórmula E:")
        with open('times.txt', 'r', encoding='utf-8') as arquiv:
            for li in arquiv:
                print(li.strip())
        print()
        input("Pressione Enter para voltar ao menu...")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        input("Pressione Enter para voltar ao menu...")


def main():
    """
    Função principal que mostra o menu inicial e permite cadastro e login de usuários.
    """
    while True:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("1. Cadastrar usuário")
            print("2. Fazer login")
            print("3. Sair")

            opcao = input("Escolha uma opção: ")
            os.system('cls' if os.name == 'nt' else 'clear')
            if opcao == '1':
                cadastrar_usuario()
            elif opcao == '2':
                login()
            elif opcao == '3':
                print('Encerrando, obrigado')
                time.sleep(2)
                break
            else:
                print("Opção inválida!")
                input("Pressione Enter para continuar...")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            input("Pressione Enter para continuar...")


# Execução do programa principal
if __name__ == '__main__':
    main()
