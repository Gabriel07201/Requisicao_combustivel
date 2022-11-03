from tkinter import *
from tkinter import messagebox

# Logins
logins = [['Admin', 'Admin'], ['Gabriel', '04220801']]

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

# Função para verificar o login
class Login():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        for user in logins:
            if self.username == user[0] and self.password == user[1]:
                messagebox.showinfo('Login', 'Login successful')
                break           
            else:
                continue
            

