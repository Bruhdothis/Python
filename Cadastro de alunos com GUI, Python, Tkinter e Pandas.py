#pip install tkinter pandas openpyxl no terminal - install tkinter pandas openpyxl

#Importa as bibliotecas necessárias
import tkinter as tk
from tkinter import ttk
import pandas as pd

#cria dicionário de usuários
usuarios = {
    "professor": {"senha": "1234", "tipo": "professor"},
    "aluno1": {"senha": "1234", "tipo": "aluno"},
    "aluno2": {"senha": "1234", "tipo": "aluno"},
}

#Cria a janela principal
janela = tk.Tk()
janela.title("Sistema de Cadastro de Alunos")
janela.geometry("820x600")

#Cria os rótulos e campos de entrada
lblNome = tk.Label(janela, text="Nome do Aluno:")
lblNota1 = tk.Label(janela, text="Nota 1")
lblNota2 = tk.Label(janela, text="Nota 2")
txtNome = tk.Entry(janela, bd=3)
txtNota1 = tk.Entry(janela)
txtNota2 = tk.Entry(janela)

#tabela de visualização com treeview(treeview = tabela de visualização)
colunas = ("Aluno", "Nota1", "Nota2", "Média", "Situação")
treeMedias = ttk.Treeview(janela, columns=colunas, show="headings")

for coluna in colunas:
    treeMedias.heading(coluna, text=coluna)
    treeMedias.column(coluna, width=100)

treeMedias.pack(padx=10, pady=10)

#Adiciona a barra de rolagem à tabela
scrollbar = ttk.Scrollbar(janela, orient="vertical", command=treeMedias.yview)
treeMedias.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")

tipo_usuario = None

#Função de cadastro e calculo de média e situação
def verificar_situacao(nota1, nota2):
    media = (nota1 + nota2) / 2
    if media >= 7.0:
        situacao = "Aprovado"
    elif media >= 5.0:
        situacao = "Em Recuperação"
    else:
        situacao = "Reprovado"
    return media, situacao

#Função para cadastrar aluno
def cadastrar_aluno():
    try:
        nome = txtNome.get()
        nota1 = float(txtNota1.get())
        nota2 = float(txtNota2.get())

        media, situacao = verificar_situacao(nota1, nota2)

        treeMedias.insert("", "end", values=(nome, nota1, nota2, f"{media:.2f}", situacao)) 
        salvar_dados()
    except ValueError:
        print("Erro: Digite valores numéricos válidos.")
    finally:
        txtNome.delete(0, "end")
        txtNota1.delete(0, "end")
        txtNota2.delete(0, "end")

#Função para salvar os dados em um arquivo Excel
def salvar_dados():
    dados = []
    for line in treeMedias.get_children():
        valores = treeMedias.item(line)["values"]
        dados.append(valores)

    df = pd.DataFrame(data=dados, columns=colunas)
    df.to_excel("planilhaAlunos.xlsx", index=False, engine="openpyxl")
    print("Dados salvos com sucesso.")

#Carrega os dados do arquivo Excel ao iniciar o programa
def carregar_dados_iniciais():
    try:
        df = pd.read_excel("planilhaAlunos.xlsx")
        for _, row in df.iterrows():
            treeMedias.insert("", "end", values=(row["Aluno"], row["Nota1"], row["Nota2"], row["Média"], row["Situação"]))
    except FileNotFoundError:
        print("Nenhum dado encontrado.")

#botão de cadastro
btnCadastrar = tk.Button(janela, text="Cadastrar", command=cadastrar_aluno)
btnCadastrar.pack()

#Cria a função para abrir a tela de login
def abrir_tela_login():
    login_win = tk.Toplevel()
    login_win.title("Login")
    login_win.geometry("300x200")

    tk.Label(login_win, text="Usuário:").pack()
    entry_usuario = tk.Entry(login_win)
    entry_usuario.pack()

    tk.Label(login_win, text="Senha:").pack()
    entry_senha = tk.Entry(login_win, show="*")
    entry_senha.pack()

    def validar_login():
        global tipo_usuario

        usuario = entry_usuario.get()
        senha = entry_senha.get()

        if usuario in usuarios and usuarios[usuario]["senha"] == senha:
            tipo_usuario = usuarios[usuario]["tipo"]
            login_win.destroy()
            iniciar_sistema(tipo_usuario, usuario)
        else:
            tk.messagebox.showerror("Erro", "Credenciais inválidas!")

    tk.Button(login_win, text="Entrar", command=validar_login).pack()

#Apenas professores podem cadastrar alunos, então adicionamos uma verificação na função cadastrar_aluno
def cadastrar_aluno():
    if tipo_usuario != "professor":
        tk.messagebox.showwarning("Acesso Negado", "Somente professores podem adicionar alunos.")
        return

    try:
        nome = txtNome.get()
        nota1 = float(txtNota1.get())
        nota2 = float(txtNota2.get())

        media, situacao = verificar_situacao(nota1, nota2)

        treeMedias.insert("", "end", values=(nome, nota1, nota2, f"{media:.2f}", situacao))
        salvar_dados()
    except ValueError:
        print("Erro: Digite valores numéricos válidos.")
    finally:
        txtNome.delete(0, "end")
        txtNota1.delete(0, "end")
        txtNota2.delete(0, "end")

#Apenas professores podem excluir alunos, então adicionamos uma verificação na função excluir_aluno
def excluir_aluno():
    if tipo_usuario != "professor":
        tk.messagebox.showwarning("Acesso Negado", "Somente professores podem excluir registros.")
        return

    selected_item = treeMedias.selection()
    if not selected_item:
        tk.messagebox.showerror("Erro", "Nenhum aluno selecionado para exclusão.")
        return

    treeMedias.delete(selected_item)
    salvar_dados()

#chama essa função para iniciar o sistema com base no tipo de usuário
def iniciar_sistema(tipo_usuario, usuario):
    janela.deiconify()

    if tipo_usuario == "professor":
        btnExcluir = tk.Button(janela, text="Excluir Aluno", command=excluir_aluno)
        btnExcluir.pack()

    carregar_dados(usuario, tipo_usuario)

#Carrega e exibe dados com base no tipo de usuário
def carregar_dados(usuario, tipo_usuario):
    try:
        df = pd.read_excel("planilhaAlunos.xlsx")

        treeMedias.delete(*treeMedias.get_children())

        if tipo_usuario == "professor":
            for _, row in df.iterrows():
                treeMedias.insert("", "end", values=(row["Aluno"], row["Nota1"], row["Nota2"], row["Média"], row["Situação"]))
        else:
            df_aluno = df[df["Aluno"] == usuario]
            for _, row in df_aluno.iterrows():
                treeMedias.insert("", "end", values=(row["Aluno"], row["Nota1"], row["Nota2"], row["Média"], row["Situação"]))
    except FileNotFoundError:
        print("Nenhum dado encontrado.")

#chama a função para carregar os dados iniciais
carregar_dados_iniciais()
#Inicia o sistema pela tela de login
janela.withdraw()
abrir_tela_login()
janela.mainloop()
