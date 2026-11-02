#Widgets da biblioteca Tkinter (semelhantes aos componentes do form no VBA do Excel) 
#mais comuns:
#Label - para exibir texto ou imagens
#Button - para criar botões
#Entry - para criar campos de entrada de texto
#Text - para criar campos de texto multilinha
#Frame - para criar contêineres para outros widgets
import tkinter as tk #importando a biblioteca Tkinter com o apelido tk

#Variável janela = janela principal do programa
janela = tk.Tk()
janela.title(" Aplicação GUI") #definindo o título da janela
janela.mainloop()
janela.resizable(False, False) #Resizing da janela desativado (não permite redimensionar a janela)
janela.mainloop()