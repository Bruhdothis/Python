#Esse protótipo de aplicativo foi desenvolvido para simular o funcionamento de um sistema de pedidos em uma lanchonete.
#Ele permite que os usuários selecionem itens do menu, visualizem o pedido atual, finalizem o pedido e
#adicionem novos produtos ao menu.


# Importa a biblioteca Tkinter para criar a interface gráfica
import tkinter as tk

# Importa messagebox para exibir mensagens de informação e erro
from tkinter import messagebox


# Classe principal do aplicativo Sabor Rápido 
# class tem a função de agrupar os métodos e atributos relacionados ao aplicativo
class SaborRapidoApp:

    # Método construtor: executado ao criar um objeto da classe(self = referência ao próprio objeto, root = janela principal do Tkinter)
    def __init__(self, root):

        # Guarda a janela principal dentro do objeto
        self.root = root

        # Define o título e o tamanho da janela
        self.root.title("Sabor Rápido - Protótipo")
        self.root.geometry("400x600")

        # Dicionário que armazena os produtos e seus respectivos preços
        self.itens_menu = {
            "Hambúrguer": 10.00,
            "Batata Frita": 5.00,
            "Refrigerante": 3.00
        }

        # Lista que armazena os produtos adicionados ao pedido
        self.pedido = []

        # -----------------------------------------
        # SEÇÃO 1: EXIBIÇÃO DO MENU
        # -----------------------------------------

        # Cria um rótulo com a instrução para selecionar os produtos
        tk.Label(
            self.root,
            text="Selecione os itens do pedido:",
            font=("Arial", 12)
        ).pack(pady=10)

        # Cria uma lista que permite selecionar vários produtos
        self.listbox = tk.Listbox(
            self.root,
            selectmode=tk.MULTIPLE,
            font=("Arial", 10),
            height=5
        )

        # Preenche a lista com os produtos disponíveis
        self.atualizar_lista_menu()

        # Exibe a lista na janela
        self.listbox.pack()

        # -----------------------------------------
        # SEÇÃO 2: BOTÕES DO PEDIDO
        # -----------------------------------------

        # Botão que adiciona os produtos selecionados ao pedido
        tk.Button(
            self.root,
            text="Adicionar ao Pedido",
            command=self.adicionar_pedido
        ).pack(pady=5)

        # Botão que mostra os produtos do pedido atual
        tk.Button(
            self.root,
            text="Visualizar Pedido",
            command=self.visualizar_pedido
        ).pack(pady=5)

        # Botão que calcula o total e finaliza o pedido
        tk.Button(
            self.root,
            text="Finalizar Pedido",
            command=self.finalizar_pedido
        ).pack(pady=5)

        # -----------------------------------------
        # SEÇÃO 3: CADASTRO DE NOVOS PRODUTOS
        # -----------------------------------------

        # Rótulo que identifica a área de cadastro
        tk.Label(
            self.root,
            text="Adicionar Novo Item ao Menu:",
            font=("Arial", 12)
        ).pack(pady=10)

        # Campo de texto para informar o nome do produto
        self.entry_item = tk.Entry(
            self.root,
            font=("Arial", 10)
        )
        self.entry_item.pack()

        # Campo de texto para informar o preço do produto
        self.entry_preco = tk.Entry(
            self.root,
            font=("Arial", 10)
        )
        self.entry_preco.pack()

        # Botão que cadastra o novo produto no menu
        tk.Button(
            self.root,
            text="Adicionar Item",
            command=self.adicionar_item_menu
        ).pack(pady=5)

    # Método responsável por atualizar a lista de produtos
    def atualizar_lista_menu(self):

        # Remove todos os elementos atualmente exibidos na lista
        self.listbox.delete(0, tk.END)

        # Percorre os nomes dos produtos cadastrados no dicionário
        for item in self.itens_menu.keys():

            # Insere cada produto na lista da interface
            self.listbox.insert(tk.END, item)

    # Método que adiciona os produtos selecionados ao pedido
    def adicionar_pedido(self):

        # Obtém os índices dos produtos selecionados na Listbox
        selecionados = self.listbox.curselection()

        # Verifica se algum produto foi selecionado
        if not selecionados:
            messagebox.showwarning(
                "Atenção",
                "Selecione pelo menos um item do menu."
            )
            return

        # Percorre os índices dos produtos selecionados
        for index in selecionados:

            # Obtém o nome do produto correspondente ao índice
            item = self.listbox.get(index)

            # Adiciona o produto à lista do pedido
            self.pedido.append(item)

        # Exibe uma mensagem confirmando a operação
        messagebox.showinfo(
            "Pedido",
            "Itens adicionados com sucesso!"
        )

    # Método que exibe os produtos presentes no pedido
    def visualizar_pedido(self):

        # Verifica se a lista do pedido está vazia
        if not self.pedido:
            messagebox.showinfo(
                "Pedido",
                "Nenhum item no pedido."
            )
            return

        # Junta os nomes dos produtos em um único texto
        # Cada produto será exibido em uma linha
        pedido_texto = "\n".join(self.pedido)

        # Exibe os produtos adicionados ao pedido
        messagebox.showinfo(
            "Pedido Atual",
            f"Itens no pedido:\n{pedido_texto}"
        )

    # Método responsável por calcular o total e finalizar o pedido
    def finalizar_pedido(self):

        # Verifica se existem produtos no pedido
        if not self.pedido:
            messagebox.showinfo(
                "Pedido",
                "Adicione itens antes de finalizar o pedido."
            )
            return

        # Soma os preços de todos os produtos presentes no pedido
        total = sum(
            self.itens_menu[item] for item in self.pedido
        )

        # Exibe o valor total e confirma a finalização
        messagebox.showinfo(
            "Total",
            f"Total do pedido: R$ {total:.2f}\n"
            "Pedido finalizado!"
        )

        # Limpa a lista para permitir iniciar um novo pedido
        self.pedido.clear()

    # Método responsável por cadastrar novos produtos no menu
    def adicionar_item_menu(self):

        # Obtém o nome digitado e remove espaços extras
        item = self.entry_item.get().strip()

        # Obtém o preço digitado e remove espaços extras
        preco = self.entry_preco.get().strip()

        # Verifica se os dois campos foram preenchidos
        if not item or not preco:
            messagebox.showerror(
                "Erro",
                "Preencha o nome e o preço do produto."
            )
            return

        # Tenta converter o preço para um número decimal
        try:

            # Substitui a vírgula por ponto para aceitar, por exemplo, 5,50
            preco = float(preco.replace(",", "."))

            # Impede o cadastro de preços negativos ou iguais a zero
            if preco <= 0:
                messagebox.showerror(
                    "Erro",
                    "O preço deve ser maior que zero."
                )
                return

            # Adiciona o produto e seu preço ao dicionário
            self.itens_menu[item] = preco

            # Atualiza a lista exibida na interface
            self.atualizar_lista_menu()

            # Limpa o campo do nome após o cadastro
            self.entry_item.delete(0, tk.END)

            # Limpa o campo do preço após o cadastro
            self.entry_preco.delete(0, tk.END)

            # Confirma que o produto foi cadastrado
            messagebox.showinfo(
                "Sucesso",
                "Item adicionado ao menu com sucesso!"
            )

        # Executa este bloco se o preço não for numérico
        except ValueError:
            messagebox.showerror(
                "Erro",
                "Preço inválido. Digite um valor numérico."
            )


# Verifica se o arquivo está sendo executado diretamente
if __name__ == "__main__":

    # Cria a janela principal do Tkinter
    root = tk.Tk()

    # Cria uma instância do aplicativo
    app = SaborRapidoApp(root)

    # Mantém a janela aberta e aguardando as interações do usuário
    root.mainloop()
