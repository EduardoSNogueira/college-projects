from datetime import date, datetime, timedelta
import csv
import os

livros = {};
usuarios = {};

#====================== CARREGAR ======================
    
def carregarDados():
    global livros, usuarios

    # Carrega Livros
    if os.path.exists("livros.csv"):
        with open("livros.csv", "r", encoding= "utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
            
                dataDevolucao = ""
                if linha ["devolucao"]:
                    dataDevolucao = datetime.strptime(linha["devolucao"], "%d/%m/%Y" ).date()
            
                livros[linha["codigo"]] ={
                    "titulo": linha["titulo"],
                    "situacao": linha["situacao"],
                    "aluno": linha["aluno"],
                    "matricula": linha["matricula"],
                    "devolucao": dataDevolucao
                }
    
    # Carrega Usuarios
    if os.path.exists("usuarios.csv"):
        with open("usuarios.csv", "r", encoding= "utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:

                usuarios[linha["matricula"]] ={
                    "nome": linha["nome"]
                }

#====================== SALVAR ======================

def salvarCsv(livros):
    # Salvar Livros
    with open("livros.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)

        escritor.writerow([            
            "codigo",
            "titulo",
            "situacao",
            "aluno",
            "matricula",
            "devolucao"
        ])

        for codigo, dados in livros.items():
            devolucao = ""
            if dados["devolucao"]:
                devolucao = dados["devolucao"].strftime("%d/%m/%Y")

            escritor.writerow([
                codigo,
                dados["titulo"],
                dados["situacao"],
                dados["aluno"],
                dados["matricula"],
                devolucao
            ])
    #Salvar Usuarios
    with open("usuarios.csv", "w", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)

        escritor.writerow([
            "matricula", 
            "nome"
        ])
        for matricula, dados in usuarios.items():
            
            escritor.writerow([
                matricula,
                dados["nome"]
            ])

    print("Salvo com sucesso!")

#====================== CADASTRO ====================== 

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

#====================== LEITURA ====================== 

def consultarLivros(livros):
    if not livros:
        print("Nenhum livro no banco de dados.")
        return
    
    for codigo, dados in livros.items():
        print(f"""
Código:   {codigo}
Título:   {dados["titulo"]}
Situação: {dados["situacao"]}             
        """)

def consultarUsuario(usuarios):
    if not usuarios:
        print("Nenhum aluno cadastrado")
        return
    
    for matricula, dados in usuarios.items():
        print(f"""
Matricula: {matricula}
Nome:      {dados["nome"]}        
        """)

def relatorio(livros):
    if not livros:
        print("Nenhum livro no banco de dados.")
        return
    
    print("\n===== RELATÓRIO =====")

    for codigo, dados in livros.items():
        print(f"""
Código: {codigo}
Título: {dados["titulo"]}
Situação: {dados["situacao"]}
Aluno: {dados["aluno"]}
Matrícula: {dados["matricula"]}
Devolução: {dados["devolucao"]}
        """)

#====================== ESCRITA ====================== 

def emprestarLivro(livros, usuarios):
    codigo = input("Código do Livro: ")
    if codigo not in livros:
        print("Livro não encontrado!")
        return
    
    if livros[codigo]["situacao"] == "emprestado":
        print("Este livro esta emprestado!")
        return
    
    matricula = input("Numero da Matricula: ")

    if matricula not in usuarios:
        print("Aluno não encontrado!")
        return
    
    dataDevolucao = date.today() + timedelta(days=15)

    livros[codigo]["situacao"] = "emprestado"
    livros[codigo]["aluno"] = usuarios[matricula]["nome"]
    livros[codigo]["matricula"] = matricula
    livros[codigo]["devolucao"] = dataDevolucao

    print("\n" + "="*30)
    print("   COMPROVANTE DE EMPRÉSTIMO   ")
    print("="*30)
    print(f"Livro: {livros[codigo]['titulo']}")
    print(f"Código: {codigo}")
    print(f"Aluno: {livros[codigo]['aluno']}")
    print(f"Matrícula: {matricula}")
    print(f"Data de Devolução: {dataDevolucao.strftime('%d/%m/%Y')}")
    print("="*30)

def devolverLivro(livros):
    codigo = input("Digite o codigo do livro: ")
    
    if codigo not in livros:
        print("Livro não encontrado!")
        return
        
    if livros[codigo]["situacao"] == "disponivel":
        print("Este livro não esta emprestado!")
        return
    
    print("\n" + "="*30)
    print("   COMPROVANTE DE DEVOLUÇÃO   ")
    print("="*30)
    print(f"Livro: {livros[codigo]["titulo"]}")
    print(f"Código: {codigo}")
    print(f"Aluno: {livros[codigo]["aluno"]}")
    
    hoje = date.today()
    dataDevolucao = livros[codigo]["devolucao"]

    if hoje > dataDevolucao:
        diasAtraso = (hoje - dataDevolucao).days
        valorMultaDia = 1.25
        valorMultaTotal = valorMultaDia * diasAtraso

        print(f"Status: Dias de atraso: ({diasAtraso} dias)")
        print(f"Multa por atraso: R$ {valorMultaTotal:.2f}")
    else:
        print("Status: Devolução dentro do prazo. Sem multas.")


    livros[codigo]["situacao"] = "disponivel"
    livros[codigo]["aluno"] = ""
    livros[codigo]["matricula"] = ""
    livros[codigo]["devolucao"] = ""

    print("Livro devolvido!")
    print("="*30)

#====================== MENU ======================

carregarDados()

while True:
    print("\n" + "="*38)
    print("   SISTEMA DE EMPRESTIMO BIBLIOTECA   ")
    print("="*38)
    print("1. Cadastrar livro")
    print("2. Cadastrar usuário")
    print("3. Consultar livros")
    print("4. Consultar alunos")
    print("5. Emprestar livro")
    print("6. Devolver Livro")
    print("7. Gerar relatório")
    print("8. Salvar")
    print("9. SAIR")
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
            consultarUsuario(usuarios)
        case "5":
            emprestarLivro(livros, usuarios)
        case "6":
            devolverLivro(livros)
        case "7":
            relatorio(livros)
        case "8":
            salvarCsv(livros)
        case "9":
            print("Saindo... ate logo")
            break
        case _:
            print("ERRO: Opção Invalida")