import tkinter as tk
from tkinter import ttk
janela = tk.Tk()

#essa função vai mostrar a escolha da carreira do usuário no console
def escolha_carreira():

   print("Gerencial: %d,\nTécnica : %d" % (var1.get(), var2.get()))#Exibe os valores das checkbuttons no console
ttk.Label(janela, text="Escolha sua vocação:").grid(row=0, sticky=tk.W)#Exibe o rótulo "Escolha sua vocação:" na primeira linha da janela
var1 = tk.IntVar() #Variável para armazenar o valor da checkbutton "Gerencial"
ttk.Checkbutton(janela, text="Gerencial", variable=var1).grid(row=1, sticky=tk.W)#Exibe a checkbutton "Gerencial" na segunda linha da janela
var2 = tk.IntVar()
ttk.Checkbutton(janela, text="Técnica", variable=var2).grid(row=2, sticky=tk.W)#Exibe a checkbutton "Técnica" na terceira linha da janela
ttk.Button(janela, text='Sair', command=janela.quit).grid(row=3, sticky=tk.W, pady=4)#Exibe o botão "Sair" na quarta linha da janela, que fecha a aplicação ao ser clicado
ttk.Button(janela, text='Mostrar', command=escolha_carreira).grid(row=4, sticky=tk.W, pady=4)#Exibe o botão "Mostrar" na quinta linha da janela, que chama a função escolha_carreira() ao ser clicado
janela.mainloop()