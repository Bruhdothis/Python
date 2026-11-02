import tkinter as tk #importando a biblioteca Tkinter
from tkinter import ttk #Esse módulo fornece acesso a widgets temáticos do Tkinter, 
                        #que são uma versão aprimorada dos widgets padrão do Tkinter.
                        #Ele permite criar interfaces gráficas com aparência mais moderna
                        #e consistente em diferentes sistemas operacionais.
janela = tk.Tk() #Variável que cria a janela principal da aplicação
janela.title(" Aplicação GUI com o Widget Label") #Texto que aparece na barra de título da janela
ttk.Label(janela, text="Componente Label" ).grid(column=0, row=0)   #O widget Label é usado para exibir texto ou imagens na interface gráfica. 
                                                                    #Ele é comumente utilizado para fornecer informações, instruções ou rótulos 
                                                                    #para outros widgets na janela. O método grid() é usado para posicionar o widget Label na janela, 
                                                                    #especificando a coluna e a linha em que ele deve aparecer.
janela.mainloop()   #Chamando o método mainloop() da janela principal, que inicia o loop de eventos da aplicação. 
                    #Esse loop mantém a janela aberta e aguarda interações do usuário, como cliques de botão ou entrada de texto.