#Importa os módulos necessários
import tkinter as tk #Tkinter recebe o apelido tk para facilitar a escrita do código
from tkinter import ttk #importa o módulo ttk para usar widgets mais avançados


#Cria a janela principal do aplicativo
janela = tk.Tk()
janela.title("Sistema de Gestão Escolar") #Título da janela
janela.geometry("600x400")


#Cria um rótulo (texto explicativo) para o campo de entrada do nome do aluno
tk.Label(janela, text="Nome do Aluno:").pack() 


#Cria campos de entrada para o nome do aluno e suas notas
entrada_nome = tk.Entry(janela)
entrada_nome.pack()
entrada_nota1 = tk.Entry(janela)
entrada_nota1.pack()
entrada_nota2 = tk.Entry(janela)
entrada_nota2.pack()


#Cria uma tabela para exibir os dados dos alunos
tabela = ttk.Treeview(janela, columns=("Nome", "Nota1", "Nota2", "Média", "Situação"), show="headings")
tabela.heading("Nome", text="Nome do Aluno")
tabela.heading("Nota1", text="Nota 1")
tabela.heading("Nota2", text="Nota 2")
tabela.heading("Média", text="Média")
tabela.heading("Situação", text="Situação")
tabela.pack()


#Adiciona uma barra de rolagem à tabela
scrollbar = ttk.Scrollbar(janela, orient="vertical", command=tabela.yview)
tabela.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")


#Carrega alguns alunos iniciais na tabela
alunos_iniciais = [
    ("Alice", 8.5, 7.0),
    ("Bruno", 5.0, 6.0),
    ("Carlos", 3.5, 4.0),
    ("Daniela", 9.0, 9.5)
]


#Loop para calcular a média e a situação de cada aluno e inserir na tabela
for aluno in alunos_iniciais:
    nome, nota1, nota2 = aluno
    media = (nota1 + nota2) / 2
    situacao = "Aprovado" if media >= 7 else "Recuperação" if media >= 5 else "Reprovado"
    tabela.insert("", "end", values=(nome, nota1, nota2, f"{media:.2f}", situacao))

#Função para adicionar um novo aluno à tabela
def cadastrar_aluno():
    nome = entrada_nome.get()
    nota1 = float(entrada_nota1.get())
    nota2 = float(entrada_nota2.get())
    media = (nota1 + nota2) / 2
    situacao = "Aprovado" if media >= 7 else "Recuperação" if media >= 5 else "Reprovado"

    tabela.insert("", "end", values=(nome, nota1, nota2, f"{media:.2f}", situacao)) #Insert serve para inserir os valores na tabela, o primeiro parâmetro é a posição onde será inserido, 
                                                                                    #o segundo é a posição do item e o terceiro são os valores que serão inseridos na tabela

tk.Button(janela, text="Cadastrar", command=cadastrar_aluno).pack() #botão para cadastrar o aluno, o comando chama a função cadastrar_aluno quando o botão é clicado

janela.mainloop() #Inicia o loop principal da interface gráfica, mantendo a janela aberta e aguardando interações do usuário.