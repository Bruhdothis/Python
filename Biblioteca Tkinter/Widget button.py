import tkinter as tk  # Importa a biblioteca Tkinter

contador = 0  # Armazena os segundos contados

def contador_label(lblRotulo):
   def funcao_contar():
      global contador  # Permite alterar o contador global
      contador = contador + 1  # Soma um segundo
      lblRotulo.config(text=str(contador))  # Atualiza o texto do label
      lblRotulo.after(1000, funcao_contar)  # Repete a contagem após 1 segundo

   funcao_contar()  # Inicia a contagem pela primeira vez

janela = tk.Tk()
janela.title("Contagem dos Segundos")  # Define o título da janela

lblRotulo = tk.Label(janela, fg="green")  # Cria o label do contador
lblRotulo.pack()  # Adiciona o label à janela
contador_label(lblRotulo)  # Inicia a função que atualiza o contador

btnAcao = tk.Button(
   janela,
   text="Clique aqui para Interromper a contagem",
   width=50,
   command=janela.destroy
)
btnAcao.pack()  # Adiciona o botão à janela

janela.mainloop()  # Mantém a janela aberta