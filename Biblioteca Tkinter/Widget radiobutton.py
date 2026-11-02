import tkinter as tk
janela = tk.Tk()
v = tk.IntVar() # Variável para armazenar a opção selecionada

#Em seguida, são criados os widgets de interface gráfica, incluindo um rótulo (Label) 
#que solicita ao usuário que escolha uma linguagem de programação, 
#e dois botões de opção (Radiobutton) para as opções "python" e "C++". 
# Cada botão de opção está associado à variável 'v' e possui um valor específico
# (1 para "python" e 2 para "C++"). A função 'pack()' é utilizada para organizar os widgets na janela.
tk.Label(janela,text="""Escolha uma linguagem de programação:""",justify = tk.LEFT, padx = 20).pack()

#Configuração dos botões de opção (Radiobutton) para as opções "python" e "C++", 
#variable =  v de vertical
tk.Radiobutton(janela,text="python",padx = 25,variable=v,value=1).pack(anchor=tk.W)
tk.Radiobutton(janela,text="C++",padx = 25,variable=v,value=2).pack(anchor=tk.W)

#o mainloop() é chamado para iniciar o loop principal da aplicação,
#permitindo que a janela permaneça aberta e interativa até que o usuário a feche.
janela.mainloop()