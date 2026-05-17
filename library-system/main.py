
livros = {};
usuarios = {};

# CADASTRO
 
def cadastrarLivro(livros):
    codigo = input("Código do Livro(ISBN): ").strip() #implementar verificação do isbn 13 digitos
    if codigo in livros:
        print("ERRO: Este código já foi cadastrado")
        return
    
    titulo = input("Título: ").strip()
    livros[codigo] = {
        "titulo": titulo,
        "situacao": "disponivel",
        "aluno": "",
        "matricula": "",
        "devolucao": ""
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

#LEITURA

def consultarLivros(livros):
    if not livros:
        print("Nenhum livro no banco de dados.")
        return
    
    for codigo, dados in livros.items():
        print(f"""
Código:   {codigo}
Título:   {dados['titulo']}
Situação: {dados['situacao']}             
        """)

# MENU

def menu():
    while True:
        print("="*38)
        print("   SISTEMA DE EMPRESTIMO BIBLIOTECA   ")
        print("="*38)
        print("1. Cadastrar livro")
        print("2. Cadastrar usuário")
        print("3. Consultar livros")
        print("4. Emprestar livro")
        print("5. Devolver Livro")
        print("6. Gerar relatório")
        print("7. Salvar")
        print("8. SAIR")
        print("="*38)
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