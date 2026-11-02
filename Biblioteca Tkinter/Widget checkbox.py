import tkinter as tk
from tkinter import ttk
janela = tk.Tk()

#Essa função vai mostrar a escolha da carreira do usuário no console
def escolha_carreira():
   #Exibe os valores das checkbuttons no console
   print("Gerencial: %d,\nTécnica : %d" % (var1.get(), var2.get()))

#Exibe o rótulo "Escolha sua vocação:" na primeira linha da janela 
ttk.Label(janela, text="Escolha sua vocação:").grid(row=0, sticky=tk.W)
var1 = tk.IntVar()
ttk.Checkbutton(janela, text="Gerencial", variable=var1).grid(row=1, sticky=tk.W)
var2 = tk.IntVar()
ttk.Checkbutton(janela, text="Técnica", variable=var2).grid(row=2, sticky=tk.W)

#Exibe o botão "Sair" na quarta linha da janela, que fecha a aplicação ao ser clicado
ttk.Button(janela, text='Sair', command=janela.quit).grid(row=3, sticky=tk.W, pady=4)
#Exibe o botão "Mostrar" na quinta linha da janela, que chama a função escolha_carreira() ao ser clicado
ttk.Button(janela, text='Mostrar', command=escolha_carreira).grid(row=4, sticky=tk.W, pady=4)
janela.mainloop()