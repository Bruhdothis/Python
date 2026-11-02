import tkinter as tk
from tkinter import ttk

#Essa função mostra os valores das escalas
def mostrar_valores():
   print (w1.get(), w2.get()) #Exibe os valores das escalas no console
janela = tk.Tk()#Exibe a janela

#Exibe as duas escalas na janela
w1 = ttk.Scale(janela, from_=0, to=50)
w1.pack()
w2 = ttk.Scale(janela, from_=0, to=100, orient=tk.HORIZONTAL)
w2.pack()

#Exibe o botão "Mostrar a Escala" na janela, que chama a função mostrar_valores() ao ser clicado
ttk.Button(janela, text='Mostrar a Escala', command=mostrar_valores).pack()
janela.mainloop()