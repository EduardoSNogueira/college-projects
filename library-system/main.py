
livros = {};
aluno = {};

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
    print("Livro cadastrado. ")

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
                cadastrarUsuario(aluno)
            case "3":
                consultarLivros(livros)
            case "4":
                emprestarLivro(livros, aluno)
            case "5":
                devolverLivro(livros)
            case "6":
                relatorio(livros, aluno)
            case "7":
                salvarCsv(livros, aluno)
            case "8":
                print("Saindo... ate logo")
                break
            case _:
                print("ERRO: Opção Invalida")

menu()