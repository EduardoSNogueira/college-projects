
livros = {};
usuarios = {};

def cadastrarLivro(livros):
    codigo = input("Código do Livro: ").strip()
    if codigo in livros:
        print("ERRO: Este código já foi cadastrado")
        return
    
    titulo = input("Título: ").strip()
    livros[codigo] = {
        "titulo": titulo,
        "situacao": "disponivel",
    }
    print("Livro cadastrado! ")

def cadastrarUsuario(usuarios):
    matricula = input("Número de Matrícula: ").strip()
    if matricula in usuarios:
        print("ERRO: Esta matrícula ja foi cadastrada")
        return
    
    nome = input("Nome do Aluno: ").strip()
    usuarios[matricula] = {
        "nome": nome
        }
    print("Usuario cadastrado! ")


# MENU

def menu():
    while True:
        print("\n   SISTEMA DE EMPRESTIMO BIBLIOTECA   ")
        print("1. Cadastrar livro")
        print("2. Cadastrar usuário")
        print("3. Consultar livros")
        print("4. Emprestar livro")
        print("5. Devolver Livro")
        print("6. Gerar relatório")
        print("7. Salvar")
        print("8. SAIR")

        opcao = input("").strip()

        match opcao:
            case "1":
                cadastrarLivro(livros)
            case "2":
                cadastrarUsuario(usuarios)
            case "3":
                consultarLivros(livros)
            case "4":
                emprestarLivro(livros, usuarios)
            case "5":
                devolverLivro(livros)
            case "6":
                relatorio(livros, usuarios)
            case "7":
                salvarCsv(livros, usuarios)
            case "8":
                print("Saindo... ate logo")
                break
            case _:
                print("ERRO: Opção Invalida")

menu()