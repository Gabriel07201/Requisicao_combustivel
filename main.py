from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from datetime import date
# biblioteca penas para conversão de vírgula para ponto
from locale import atof, setlocale, LC_NUMERIC
import pandas as pd

# ----------------------------------------------------------------------------------------------------
# configs
setlocale(LC_NUMERIC, '')
today = date.today()
today = today.strftime("%d/%m/%Y")


# ----------------------------------------------------------------------------------------------------
# logins
logins = [['Admin', 'Admin'], ['Gabriel', '04220801'], ['3', '3']]

# ----------------------------------------------------------------------------------------------------
# tela principal
class Main_tela():
    def __init__(self, nome):
        self.nome = nome
        self.nome = Tk()
        self.nome.title('Requisição de abastecimento')
        Posicao(self.nome, 320, 200)
        # botão para nova requisição
        self.new_req = Button(self.nome, text='Nova Requisição', font= 'Times 15', command=lambda: Nova_req_tela('nova req') and self.nome.destroy(), relief='groove')
        self.new_req.place(width=180,x=70, y=20)
        # botão para atualizar uma requisição
        self.att_req = Button(self.nome, text='Atualizar requisição', font= 'Times 15', command=lambda: Att_req_tela('att req') and self.nome.destroy(), relief='groove')
        self.att_req.place(width=180,x=70, y=80)
        # botão para gerar relatório
        self.rel_req = Button(self.nome, text='Relatório', font= 'Times 15', command=lambda: Relatorio_req_tela('rel req') and self.nome.destroy(), relief='groove')
        self.rel_req.place(width=180, x=70, y=140)
        

# ----------------------------------------------------------------------------------------------------
# tela nova requisição
class Nova_req_tela():
    def __init__(self, nome):
        # banco de dados feito em excel, onde será salvo os dados
        self.banco_de_dados = pd.read_excel('banco_de_dados.xlsx', engine='openpyxl')
        self.nome = nome
        self.nome = Tk()
        self.nome.title('Nova Requisição')
        Posicao(self.nome, 480, 500)
        Menu_superior(self.nome)
        # label e box para o id
        self.label_id = Label(self.nome, text='ID', font= 'Times 12')
        self.message_id = Message(self.nome, font='Arial 15', text=(self.banco_de_dados.shape[0] + 1), relief='sunken', bg='white')
        # combo_box com o solicitante do abastecimento
        self.label_solicitante = Label(self.nome, font='Times 12', text='Solicitante')
        self.combo_box_solicitante = ttk.Combobox(self.nome,font='Arial 15', state="readonly")
        self.combo_box_solicitante.focus()
        self.combo_box_solicitante['values'] = ['Gemerson', 'Adilson', 'Gabriel']
        # label e combo box motorista
        self.label_motorista = Label(self.nome, font='Times 12', text='Motorista')
        self.combo_box_motorista = ttk.Combobox(self.nome, font='Arial 15', state="readonly")
        self.combo_box_motorista['values'] = ['Gemerson', 'Adilson', 'Gabriel']
        # label e combo box categoria
        self.label_categoria = Label(self.nome, font='Times 12', text='Categoria')
        self.combo_box_categoria = ttk.Combobox(self.nome, font='Arial 15', state='readonly')
        self.combo_box_categoria['values'] = ['Gasolina', 'Etanol', 'Filtro de óleo', 'Filtro de ar']
        # label e entry quantidade
        self.label_quantidade = Label(self.nome, font='Times 12', text='Quantidade')
        self.entry_quantidade = Entry(self.nome, font='Arial 15')
        # label e entry preço unitário
        self.label_preco = Label(self.nome, font='Times 12', text='Preço Unitário')
        self.entry_preco = Entry(self.nome, font='Arial 15')
        # função para buscar o valor digitado e com isso fazer a conversão para o tipo float, independente se o valor for passado com vírgula ou ponto.
        def float_number(event):
            try:
                if self.entry_preco.get() == '' or self.entry_quantidade.get() == '':
                    number_preco = 0
                    number_quantidade = 0
                else:
                    if ',' in self.entry_quantidade.get():
                        number_quantidade = atof(self.entry_quantidade.get())
                    if ',' in self.entry_preco.get():
                        number_preco = atof(self.entry_preco.get())
                    if '.' in self.entry_preco.get():
                        number_preco = float(self.entry_preco.get())
                    if '.' in self.entry_quantidade.get():
                        number_quantidade = float(self.entry_quantidade.get())
                    if ',' not in self.entry_quantidade.get():
                        number_quantidade = float(self.entry_quantidade.get())
                    if ',' not in self.entry_preco.get():
                        number_preco = float(self.entry_preco.get())
                self.message_total.config(text=round(number_preco*number_quantidade, 2))
            except Exception as e:
                # usar o exception depois pra registrar possíveis bugs
                self.message_total.config(text='Valores inválidos')
        self.entry_preco.bind("<Tab>", float_number)
        # label e message total
        self.label_total = Label(self.nome, font='Times 12', text='Total')

        self.message_total = Label(self.nome, font='Arial 15', text=0, relief='sunken', bg='white')
        # label data
        self.label_data = Label(self.nome, font='Times 12', text='Data')
        self.data_now = Label(self.nome, font='Arial 15', text=today, relief='sunken', bg='white')
        # label maior para observação
        self.label_observacao = Label(self.nome, font='Times 12', text='Observação')
        self.campo_observacao = Text(self.nome, font='Arial 12', relief='sunken', bg='white')
        # botao para salvar, no salvamento teremos algumas funções
        # função para salvar as informações 
        def Save_new_req(self):
            dados = [[]]
            dados[0].append(self.message_id['text'])
            if self.combo_box_solicitante.get() == '':
                messagebox.showinfo('Solicitante', 'Informe o solicitante')
            else:
                dados[0].append(self.combo_box_solicitante.get())
            if self.combo_box_motorista.get() == '':
                messagebox.showinfo('Motorista', 'Informe o motorista')
            else:
                dados[0].append(self.combo_box_motorista.get())
            if self.combo_box_categoria.get() == '':
                messagebox.showinfo('Categoria', 'Informe a categoria')
            else:
                dados[0].append(self.combo_box_categoria.get())
            dados[0].append(self.entry_quantidade.get())
            dados[0].append(self.entry_preco.get())
            dados[0].append(self.message_total['text'])
            dados[0].append(self.data_now['text'])
            dados[0].append(self.campo_observacao.get(1.0, "end-1c"))
            if len(dados[0]) == 9:
                dados = pd.DataFrame(dados, columns=['ID', 'Solicitante', 'Motorista', 'Categoria', 'Quantidade', 'Preço Unitário', 'Total', 'Data', 'Observação'])
                banco_de_dados_to_save = self.banco_de_dados.append(dados)
                banco_de_dados_to_save.to_excel("banco_de_dados.xlsx", index=False)
        self.button_save = Button(self.nome, font='Times 12', text='Salvar', relief='raised', borderwidth=3, command= lambda: Save_new_req(self))
        # botao para nova requisição, que irá limpar a tela e atualizar algumas informações
        # botão para dar um refresh na tela e cadastrar novos dados
        def refresh(self):
            self.nome.destroy()
            self.__init__(nome)
        self.button_new = Button(self.nome, font='Times 12', text='Nova', relief='raised', borderwidth=3, command=lambda: refresh(self))

        # -------------------------------
        # posicionamento do front
        self.label_id.place(x=10, y=10)
        obrigatorio(self.nome, 10, 10)
        self.message_id.place(x=10, y=32, width=70, height=30)
        self.label_solicitante.place(x=90, y=10)
        obrigatorio(self.nome, 137, 10)
        self.combo_box_solicitante.place(x=90, y=32, height=30, width=130)
        self.label_motorista.place(x=250, y=10)
        obrigatorio(self.nome, 295, 10)
        self.combo_box_motorista.place(x=250, y=32, height=30, width=210)
        self.label_categoria.place(x=10, y=90)
        obrigatorio(self.nome, 55, 90)
        self.combo_box_categoria.place(x=10, y=112, height=30, width=210)
        self.label_quantidade.place(x=250, y=90)
        self.entry_quantidade.place(x=250, y=112, height=30, width=210)
        self.label_preco.place(x=10, y=160)
        self.entry_preco.place(x=45, y=182, width=175, height=30)
        label_moeda(self.nome, 10, 182, 25)
        self.label_total.place(x=250, y=160)
        self.message_total.place(x=285, y=182, width=175, height=30)
        label_moeda(self.nome, 250, 182, 25)
        self.label_data.place(x=10, y=215)
        self.data_now.place(x=10, y=237)
        self.label_observacao.place(x=10, y=270)
        self.campo_observacao.place(x=10, y=292, width=460, height=150)
        self.button_save.place(x=10, y=450, width=70, height=30)
        self.button_new.place(x=90, y=450, width=70, height=30)


        
# ----------------------------------------------------------------------------------------------------
# tela atualizar requisição
class Att_req_tela():
    def __init__(self, nome):
        self.nome = nome
        self.nome = Tk()
        self.nome.title('Atualizar Requisição')
        Posicao(self.nome, 500, 500)
        Menu_superior(self.nome)


# ----------------------------------------------------------------------------------------------------
# tela relatório
class Relatorio_req_tela():
    def __init__(self, nome):
        self.nome = nome
        self.nome = Tk()
        self.nome.title('Relatório')
        Posicao(self.nome, 500, 500)
        Menu_superior(self.nome)


# ----------------------------------------------------------------------------------------------------
# funções

# centralizando a tela, no eixoy um pouco mais para cima
class Posicao():
    def __init__(self, master=None, largura=700, altura=400):
        self.largura = largura
        self.altura = altura
        self.largura_screen = master.winfo_screenwidth()
        self.altura_screen = master.winfo_screenheight()
        self.posx = self.largura_screen/2 - self.largura/2
        self.posy = self.altura_screen/2 - self.altura/2
        master.geometry("%dx%d+%d+%d" % (self.largura, self.altura, self.posx, self.posy - 70))
        master.resizable(0,0)


# Menu superior
class Menu_superior():
    def __init__(self, nome):
        self.cascade = Menu(nome, tearoff=0)
        self.cascade.add_command(label='Início', command= lambda: Main_tela("main_tela") and self.nome.destroy())
        self.cascade.add_command(label='Nova Requisição', command=lambda: Nova_req_tela('nova req') and self.nome.destroy())
        self.cascade.add_command(label='Atualizar Requisição', command=lambda: Att_req_tela('att req') and self.nome.destroy())
        self.cascade.add_command(label='Relatório', command=lambda: Relatorio_req_tela('rel req') and self.nome.destroy())
        self.menu = Menu(nome, tearoff=0)        
        self.menu.add_cascade(label='Menu', menu=self.cascade)
        self.menu.add_command(label='Sair', command= lambda: self.nome.destroy())
        self.nome = nome
        self.nome.configure(menu=self.menu)

def obrigatorio(master, posx, posy):
    obg = Message(master, text='*', fg='red', justify=LEFT, anchor=SW)
    obg.place(x=posx+18, y=posy-3)

def label_moeda(master, posx, posy, width):
    label_moeda = Label(master, text='R$', font='Arial 15')
    label_moeda.place(x=posx, y=posy, width=width)



# ----------------------------------------------------------------------------------------------------
# criando tela de login
class Tela_login():
    def __init__(self):
        self.tela_login = Tk()
        self.tela_login.title('Requisição de abastecimento')
        Posicao(self.tela_login,320,300)

        # configurando label login centralizado
        self.label_login = Label(self.tela_login, text='Login', font= 'Times 30')
        self.label_login.place(x=100, y=15)
        self.label_linha = Label(self.tela_login, text='', font= 'Times 1', width=195, bg='#808080', anchor=N)
        self.label_linha.place(x=55, y=70)

        #configurando label/entry usuario
        self.label_usuario = Label(self.tela_login, text='Usuário', font='Times 10')
        self.label_usuario.place(x=55, y=90)
        self.text_usuario = Entry(self.tela_login, font='Arial 12')
        self.text_usuario.place(width=200,x=55, y=110)

        # cofigurando label/entry senha
        self.label_senha = Label(self.tela_login, text='Senha: ', font='Times 10')
        self.label_senha.place(x=55, y=150)
        self.text_senha = Entry(self.tela_login, font='Arial 12', show='*')
        self.text_senha.place(width=200,x=55, y=170)

        # função para verificar o login
        def Login(username, password):
            self.username = username
            self.password = password
            # pega cada lista com usuario e login e passa uma vericação
            for user in logins:
                if self.username == user[0] and self.password == user[1]:
                    messagebox.showinfo('Login', 'Login successful')
                    self.login = 1
                    break
                # caso o login não funcione a função vai armazenar um valor, para aparecer a mensagem de login falhado somente no final, já que a verificação teste todos.           
                else:
                    self.login = 0
                    continue
            if self.login == 0:
                messagebox.showinfo('Login', 'Login failed')
            if self.login == 1:
                Main_tela("main_tela")
                self.tela_login.destroy()
                
        # configurando o botão login
        self.button_login = Button(text='Login', font='Times 10', relief='groove', command=lambda: Login(self.text_usuario.get(), self.text_senha.get()))
        self.button_login.place(width=200,x=55, y=220)


        self.tela_login.mainloop()


# ----------------------------------------------------------------------------------------------------
Tela_login()

