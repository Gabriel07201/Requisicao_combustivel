from tkinter import *
from funcoes import *

# criando tela de login
tela_login = Tk()
tela_login.title('Requisição de abastecimento')
Posicao(tela_login,320,300)

# configurando label login centralizado
label_login = Label(tela_login, text='Login', font= 'Times 30')
label_login.place(x=100, y=15)
label_linha = Label(tela_login, text='', font= 'Times 1', width=200, bg='#808080', anchor=N)
label_linha.place(x=50, y=70)

#configurando label/entry usuario
label_usuario = Label(tela_login, text='Usuário', font='Times 10')
label_usuario.place(x=50, y=90)
text_usuario = Entry(tela_login, font='Arial 12')
text_usuario.place(width=200,x=50, y=110)

# cofigurando label/entry senha
label_senha = Label(tela_login, text='Senha: ', font='Times 10')
label_senha.place(x=50, y=150)
text_senha = Entry(tela_login, font='Arial 12', show='*')
text_senha.place(width=200,x=50, y=170)

tela_login.mainloop()