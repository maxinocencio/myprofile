'''

Myprofile - Uma forma rápida e simples de se apresentar

- Consiste em um app de apresentação rápida, onde é possivel se apresentar e deixar seu contato rápidamente
- O app tem 4 telas: Tela principal, Sobre mim, Contato e Creditos

'''

from tkinter import *                               # Importanto a biblioteca tkinter
from sobremim import Sobremim                       # Importando a segunda tela
from contato import Contato                         # Importando a terceira tela
from creditos import Creditos                       # Importando a quarta tela

class Myprofile(Toplevel):
    def __init__(self, original):
        self.frame_original = original
        Toplevel.__init__(self)

class Inicio():                                     # Criando a primeira tela (inicio)
    corprincipal = '#4594E5'                        # Cor principal (background) Azul
    cor1 = '#ffffff'                                # Cor secundaria (Textos e etc) Branco

    def __init__(self):                             # Método construtor
        self.root = root

        self.config()                               # Chamando as configurações da janela
        self.frames()                               # Chamando todos os frames da primeira tela

        self.widgetstitulo()                        # Chamando os widgets do frame título   (Texto, My Profile)
        self.widgetslogo()                          # Chamando os widgets do frame logo     (Imagem, logo)
        self.widgetslogan()                         # Chamando os widgets do frame slogan   (Texto, Uma forma rápida e simples de se apresentar)
        self.widgetsbotao1()                        # Chamando os widgets do frame botao1   (Botão, Sobre Mim)
        self.widgetsbotao2()                        # Chamando os widgets do frame botao2   (Botão, Contato)
        self.widgetsbotao3()
        self.widgetsbotao4()

        root.mainloop()

    def config(self):                               # Configurações da janela 1
        self.root.title('My Profile')               # Título da janela
        self.root.geometry('375x667+700+15')        # Tamaho da janela e onde ela vai abrir
        self.root.resizable(False, False)           # Impedindo a janeja de ser redimensionada
        self.root.configure(bg = self.corprincipal) # Determinando a cor de background da janela
        self.root.iconbitmap('myprofile\icon.ico')  # Determinando o icone

    def frames(self):                               # Frames Janela 1
        self.titulo = Frame(                        # Criando frame ítulo
            self.root,
            bg = self.corprincipal                  # Determinando a cor de fundo do frame 
        )

        self.titulo.place(                          # Determinando onde o frame título ficará
            relx = 0,
            rely = 0.1,
            relwidth = 1,
            relheight = 0.1
        )

        self.logo = Frame(                          # Criando frame logo
            self.root,                               
            bg = self.cor1                          # Determinando a cor de fundo do frame
        )

        self.logo.place(                            # Determinando onde o frame logo ficará
            relx = 0.25,
            rely = 0.25,
            relwidth = 0.51,
            relheight = 0.288
        )

        self.slogan = Frame(                        # Criando frame slogan
            self.root,
            bg = self.corprincipal                  # Determinando a cor de fundo do frame
        )

        self.slogan.place(                          # Determinando onde o frame slogan ficará
            relx = 0,
            rely = 0.6,
            relwidth = 1,
            relheight = 0.1
        )

        self.botao1 = Frame(                        # Criando frame botao1
            self.root,
            bg = self.corprincipal                  # Determinando a cor de fundo do frame
        )

        self.botao1.place(                          # Determinando onde o frame botao1 ficará
            relx = 0.05,
            rely = 0.7,
            relwidth = 0.45,
            relheight = 0.1
        ) 

        self.botao2 = Frame(                        # Criando frame botao2
            self.root,
            bg = self.corprincipal                  # Determinando a cor de fundo do frame
        )

        self.botao2.place(                          # Determinando onde o frame botao2 ficará
            relx = 0.51,
            rely = 0.7,
            relwidth = 0.45,
            relheight = 0.1
        )

        self.botao3 = Frame(                        # Criando frame botao3
            self.root,
            bg = self.cor1                          # Determinando a cor de fundo do frame
        )

        self.botao3.place(                          # Determinando onde o frame botao2 ficará
            relx = 0.05,
            rely = 0.805,
            relwidth = 0.45,
            relheight = 0.1
        )

        self.botao4 = Frame(                        # Criando frame botao3
            self.root,
            bg = self.cor1                          # Determinando a cor de fundo do frame
        )

        self.botao4.place(                          # Determinando onde o frame botao2 ficará
            relx = 0.51,
            rely = 0.805,
            relwidth = 0.45,
            relheight = 0.1
        )   

    def widgetslogo(self):                                      # Widgets do frame logo
        self.profile = PhotoImage(file = 'myprofile\logo.png')  # Chamando a imagem (logo)
        self.img1 = Label(
            self.logo,                                          # Mostrando que pertence ao frame logo
            image = self.profile,                               # Chamando a imagem
            bd = 0
        )
        self.img1.pack()

    def widgetstitulo(self):                                    # Widgets do frame titulo
        title = Label(self.titulo,                              # Mostrando que pertence ao frame titulo
            text='My Profile',                                  # Texto que será inserido no frame
            font=('Poppins', 30, 'bold'),                       # Fonte usada no texto
            bg = self.corprincipal,                             # Cor backgroud do texto
            fg = self.cor1,                                     # Cor do texto
        )
        title.pack()

    def widgetslogan(self):                                     # Widgets do frame slogan
        slogan = Label(
            self.slogan,                                        # Mostrando que pertence ao frame slogan
            text='Uma forma rápida e simples de se apresentar', # Texto que será inserido no frame
            font=('Poppins', 11, 'bold'),                       # Fonte usada no texto
            bg = self.corprincipal,                             # Cor backgroud do texto
            fg = self.cor1,                                     # Cor do texto
        )
        slogan.pack()

    def widgetsbotao1(self):                                    # Widgets do frame botao1
        self.btn1 = Button(                                     # Criando botao
            self.botao1,                                        # Mostrando que pertence ao frame botao1
            text = 'Sobre Mim',                                 # Texto inserido no botão
            bg = self.cor1,                                     # Cor de fundo do botão
            activebackground = self.cor1,                       # Cor de fundo do botão quando acionado
            font = ('Poppins', 19),                             # Fonte no texto do botão
            fg = self.corprincipal,                             # Cor do texto
            activeforeground = self.corprincipal,               # Cor de fundo do texto quando o botão estiver acionado
            command = self.clickbtn1                            # Comando atribuido ao botão
        )
        self.btn1.place(                                        # Determinando onde o botão ficará
            relx = 0,
            rely = 0,
            relheight = 1,
            relwidth = 1
        )

    def widgetsbotao2(self):                                    # Widgets do frame botao2
        self.btn2 = Button(                                     # Criando botao
            self.botao2,                                        # Mostrando que pertence ao frame botao2
            text = 'Contato',                                   # Texto inserido no botão
            bg = self.cor1,                                     # Cor de fundo do botão
            activebackground = self.cor1,                       # Cor de fundo do botão quando acionado
            font = ('Poppins', 19),                             # Fonte no texto do botão
            fg = self.corprincipal,                             # Cor do texto
            activeforeground = self.corprincipal,               # Cor de fundo do texto quando o botão estiver acionado
            command = self.clickbtn2                            # Comando atribuido ao botão
        )
        self.btn2.place(                                        # Determinando onde o botão ficará
            relx = 0,
            rely = 0,
            relheight = 1,
            relwidth = 1
        )

    def widgetsbotao3(self):                                    # Widgets do frame botao3
        self.btn3 = Button(                                     # Criando botao
            self.botao3,                                        # Mostrando que pertence ao frame botao3
            text = 'Creditos',                                  # Texto inserido no botão
            bg = self.cor1,                                     # Cor de fundo do botão
            activebackground = self.cor1,                       # Cor de fundo do botão quando acionado
            font = ('Poppins', 19),                             # Fonte no texto do botão
            fg = self.corprincipal,                             # Cor do texto
            activeforeground = self.corprincipal,               # Cor de fundo do texto quando o botão estiver acionado
            command = self.clickbtn3                            # Comando atribuido ao botão
        )
        self.btn3.place(                                        # Determinando onde o botão ficará
            relx = 0,
            rely = 0,
            relheight = 1,
            relwidth = 1
        )
    
    def widgetsbotao4(self):                                    # Widgets do frame botao4
        self.btn4 = Button(                                     # Criando botao
            self.botao4,                                        # Mostrando que pertence ao frame botao4
            text = 'Sair',                                      # Texto inserido no botão
            bg = self.cor1,                                     # Cor de fundo do botão
            activebackground = self.cor1,                       # Cor de fundo do botão quando acionado
            font = ('Poppins', 19),                             # Fonte no texto do botão
            fg = self.corprincipal,                             # Cor do texto
            activeforeground = self.corprincipal,               # Cor de fundo do texto quando o botão estiver acionado
            command = self.clickbtn4                            # Comando atribuido ao botão
        )
        self.btn4.place(                                        # Determinando onde o botão ficará
            relx = 0,
            rely = 0,
            relheight = 1,
            relwidth = 1
        )

    def hide(self):                                             # Criando método para esconder a janela
        self.root.withdraw()
    
    def show(self):                                             # Criando método para mostrar a janela
        self.root.update()
        self.root.deiconify()

    def clickbtn1(self):                                        # Criando método para atribuir um comando ao botão1
        self.hide()
        self.subFrame = Sobremim(self)

    def clickbtn2(self):                                        # Criando método para atribuir um comando ao botão2
        self.hide()
        self.subFrame = Contato(self)

    def clickbtn3(self):                                        # Criando método para atribuir um comando ao botão3
        self.hide()
        self.subFrame = Creditos(self)

    def clickbtn4(self):                                        # Criando método para atribuir um comando ao botão4
        self.root.destroy()

root = Tk()
Inicio()