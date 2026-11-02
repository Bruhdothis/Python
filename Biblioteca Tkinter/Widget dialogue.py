import tkinter as tk
from tkinter import messagebox as mb #importa a biblioteca de mensagens do tkinter

#Essa função mostra uma mensagem de erro
def resposta():
   mb.showerror("Resposta", "Desculpe, nenhuma resposta disponível!")

#Essa função verifica se o usuário quer sair e exibe uma mensagem de aviso ou de informação 
#dependendo da resposta do usuário
def verificacao():
   if mb.askyesno('Verificar', 'Realmente quer sair?'):
      mb.showwarning('Yes', 'Ainda não foi implementado')
   else:
      mb.showinfo('No', 'A opção de Sair foi cancelada')
tk.Button(text='Sair', command=verificacao).pack(fill=tk.X)
tk.Button(text='Resposta', command=resposta).pack(fill=tk.X)
tk.mainloop()