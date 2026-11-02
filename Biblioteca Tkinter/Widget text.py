import tkinter as tk
janela = tk.Tk()

#Variável T para armazenar o texto digitado pelo usuário
T = tk.Text(janela, height=2, width=30)#Exibe a caixa de texto na janela
T.pack()#Insere o texto "Este é um texto\ncom duas linhas\n" na caixa de texto:
T.insert(tk.END, "Este é um texto\ncom duas linhas\n")
tk.mainloop()
