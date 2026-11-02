import tkinter as tk
janela = tk.Tk()

#Define a mensagem que será exibida na janela
mensagem_para_usuario = "Esta é uma mensagem.\n(Pode ser bastante útil para o usuário)"

#Variável msg para armazenar a mensagem que será exibida na janela
msg = tk.Message(janela, text = mensagem_para_usuario)

#Estabelece a cor de fundo da mensagem como verde claro e define a fonte como Times, tamanho 24, em itálico
msg.config(bg='red', font=('times',25, 'italic'))

#Exibe a mensagem na janela
msg.pack()
janela.mainloop()