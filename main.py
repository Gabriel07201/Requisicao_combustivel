from tkinter import *
from tkinter import messagebox

# ----------------------------------------------------------------------------------------------------
# logins
logins = [['Admin', 'Admin'], ['Gabriel', '04220801']]

# ----------------------------------------------------------------------------------------------------
# tela principal
class Main_tela():
    def __init__(self, nome):
        self.nome = nome
        self.nome = Tk()
        self.nome.title('Requisição de abastecimento')
        Posicao(self.nome, 320, 200)
        # botão para nova requisição
        self.new_req = Button(self.nome, text='Nova Requisição', font= 'Times 15', command=lambda: Nova_req_tela('nova req') and self.nome.destroy())
        self.new_req.place(width=180,x=70, y=20)
        # botão para atualizar uma requisição
        self.att_req = Button(self.nome, text='Atualizar requisição', font= 'Times 15', command=lambda: Att_req_tela('att req') and self.nome.destroy())
        self.att_req.place(width=180,x=70, y=80)
        # botão para gerar relatório
        self.rel_req = Button(self.nome, text='Relatório', font= 'Times 15', command=lambda: Relatorio_req_tela('rel req') and self.nome.destroy())
        self.rel_req.place(width=180, x=70, y=140)
        

# ----------------------------------------------------------------------------------------------------
# tela nova requisição
class Nova_req_tela():
    def __init__(self, nome):
        self.nome = nome
        self.nome = Tk()
        self.nome.title('Requisição de abastecimento')
        Posicao(self.nome, 500, 500)


# ----------------------------------------------------------------------------------------------------
# tela atualizar requisição
class Att_req_tela():
    def __init__(self, nome):
        self.nome = nome
        self.nome = Tk()
        self.nome.title('Requisição de abastecimento')
        Posicao(self.nome, 500, 500)


# ----------------------------------------------------------------------------------------------------
# tela relatório
class Relatorio_req_tela():
    def __init__(self, nome):
        self.nome = nome
        self.nome = Tk()
        self.nome.title('Requisição de abastecimento')
        Posicao(self.nome, 500, 500)



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

