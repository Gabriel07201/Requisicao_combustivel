from tkinter import *

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
