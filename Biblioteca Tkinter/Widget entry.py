import tkinter as tk
#Este programa cria uma aplicação GUI com o widget Entry, permitindo que o usuário insira seu nome 
#e sobrenome. Ao clicar no botão "Exibir Dados", os valores inseridos são exibidos no console.
#O botão "Sair" fecha a aplicação.
def mostrar_nomes():
   print("Nome: %s\nSobrenome: %s" % (e1.get(), e2.get()))#Exibe os valores inseridos no console
janela = tk.Tk()
janela.title("Aplicação GUI com o Widget Entry")
tk.Label(janela,text="Nome").grid(row=0)#Exibe o rótulo "Nome" na primeira linha da janela

tk.Label(janela,text="Sobrenome").grid(row=1)#Exibe o rótulo "Sobrenome" na segunda linha da janela
#Cria dois campos de entrada (Entry) para o usuário inserir seu nome e sobrenome
e1 = tk.Entry(janela)
e2 = tk.Entry(janela)
#Posiciona os campos de entrada na janela usando o método grid
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
#Cria dois botões: "Sair" para fechar a aplicação e "Exibir Dados" para mostrar os valores inseridos 
#no console
tk.Button(janela, text='Sair',command=janela.quit).grid(row=3,column=0,sticky=tk.W,pady=4)
tk.Button(janela, text='Exibir Dados', command=mostrar_nomes).grid(row=3,column=1,sticky=tk.W,pady=4)
tk.mainloop()#Mantém a janela aberta até que o usuário a feche