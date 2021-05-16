from tkinter import *

class Contato(Toplevel):                            # Criando a segunda tela (Sobre mim)
    corprincipal = '#4594E5'                        # Cor principal (background) Azul
    cor1 = '#ffffff'                                # Cor secundaria (Textos e etc) Branco

    def __init__(self, original):                   # Método construtor
        self.frame_original = original
        Toplevel.__init__(self)

        self.config()                               # Chamando as configurações da janela
        self.frames()                               # Chamando todos os frames da segunda tela
        
        self.widgetstitulo()                        # Chamando os widgets do frame título       (Texto, Contato)
        self.widgetslogo()                          # Chamando os widgets do frame logo         (Imagem, logo)
        self.widgetsinstaimg()                      # Chamando os widgets do frame instaimg     (Imagem, Instagram)
        self.widgetsinsta()                         # Chamando os widgets do frame insta        (Nome, Instagram)
        self.widgetswhatsappimg()                   # Chamando os widgets do frame whatsappimg  (Imagem, whatsapp)
        self.widgetswhatsapp()                      # Chamando os widgets do frame whatsapp     (Nome, whatsapp)
        self.widgetsbotao()                         # Chamando os widgets do frame botao        (Botão, Voltar)

    def config(self):                               # Configurações da janela 3
        self.title('Contato')                       # Título da janela
        self.geometry('375x667+700+15')             # Tamaho da janela e onde ela vai abrir
        self.resizable(False, False)                # Impedindo a janeja de ser redimensionada
        self.configure(bg = self.corprincipal)      # Determinando a cor de background da janela
        self.iconbitmap('myprofile\icon.ico')       # Determinando o icone

    def frames(self):                               # Frames Janela 3
        self.titulo = Frame(                        # Criando frame título
            self,
            bg = self.corprincipal                  # Determinando a cor de fundo do frame
        )

        self.titulo.place(                          # Determinando  onde o frame título ficará
            relx = 0,
            rely = 0.15,
            relwidth = 1,
            relheight = 0.1
        )

        self.logo = Frame(                          # Criando frame logo
            self,
            bg = self.corprincipal                  # Determinando a cor de fundo do frame
        )

        self.logo.place(                            # Determinando onde o frame logo ficará
            relx = 0.11,
            rely = 0.08,
            relwidth = 0.1275,
            relheight = 0.072
        )

        self.instaimg = Frame(                      # Criando frame instaimg
            self,
            bg = self.corprincipal                  # Determinando a cor de fundo do frame
        )

        self.instaimg.place(                        # Determinando onde o frame instaimg ficará
            relx = 0.1,
            rely = 0.29,
            relwidth = 0.1275,
            relheight = 0.072
        )    

        self.insta = Frame(                         # Criando frame insta
            self,
            bg = self.corprincipal                  # Determinando a cor de fundo do frame
        )

        self.insta.place(                           # Determinando onde o frame insta ficará
            relx = 0.25,
            rely = 0.3,
            relwidth = 0.9,
            relheight = 0.05
        )

        self.whatsapp = Frame(                      # Criando frame whatsapp
            self,
            bg = self.corprincipal                  # Determinando a cor de fundo do frame
        )

        self.whatsapp.place(                        # Determinando onde o frame whatsapp ficará
            relx = 0.25,
            rely = 0.41,
            relwidth = 1,
            relheight = 0.06
        )

        self.whatsappimg = Frame(                   # Criando frame whatsappimg
            self,
            bg = self.corprincipal                  # Determinando a cor de fundo do frame      
        )

        self.whatsappimg.place(                     # Determinando onde o frame whatsappimg ficará
            relx = 0.1,
            rely = 0.4,
            relwidth = 0.1275,
            relheight = 0.072
        )   

        self.botao = Frame(                         # Determinando onde o frame botao ficará
            self,
            bg = self.corprincipal                  # Determinando a cor de fundo do frame
        )

        self.botao.place(                           # Determinando onde o frame botao ficará
            relx = 0.3,
            rely = 0.75,
            relwidth = 0.4,
            relheight = 0.1
        )     

    def widgetslogo(self):                                      # Widgets do frame logo
        self.profile = PhotoImage(file = 'myprofile\logo2.png') # Chamando a imagem (logo)
        self.img1 = Label(              
            self.logo,                                          # Mostrando que pertence ao frame logo
            image = self.profile,                               # Chamando a imagem
            bd = 0
        )
        self.img1.pack()

    def widgetstitulo(self):                                    # Widgets do frame titulo
        title = Label(self.titulo,                              # Mostrando que pertence ao frame titulo
            text='Contato',                                     # Texto que será inserido no frame
            font=('Poppins', 30, 'bold'),                       # Fonte usada no texto
            bg = self.corprincipal,                             # Cor backgroud do texto
            fg = self.cor1,                                     # Cor do texto
        )
        title.place(                                            # Determinando onde o texto ficará
            relx = 0.1
        )

    def widgetsinstaimg(self):                                  # Widgets do frame instaimg
        self.a = PhotoImage(file = 'myprofile\instagram.png')   # Chamando a imagem (instaimg)
        self.img2 = Label(
            self.instaimg,                                      # Mostrando que pertence ao frame instaimg
            image = self.a,                                     # Chamando a imagem
            bd = 0
        )
        self.img2.pack()

    def widgetsinsta(self):                                     # Widgets do frame insta
        insta = Label(self.insta,                               # Mostrando que pertence ao frame insta
            text='@joao1234',                                   # Texto que será inserido no frame
            font=('Poppins', 18, 'bold'),                       # Fonte usada no texto
            bg = self.corprincipal,                             # Cor backgroud do texto
            fg = self.cor1,                                     # Cor do texto
            justify=LEFT,                                       # Justifica o texto na esquerda
        )
        insta.pack(side = LEFT)                                 # "Empacotar" o texto a esquerda

    def widgetswhatsapp(self):                                  # Widgets do frame whatsapp
        whatsapp = Label(self.whatsapp,                         # Mostrando que pertence ao frame whatsapp
            text='(24) 9 9999-9999',                            # Texto que será inserido no frame
            font=('Poppins', 18, 'bold'),                       # Fonte usada no texto
            bg = self.corprincipal,                             # Cor backgroud do texto
            fg = self.cor1,                                     # Cor do texto
            justify=LEFT,                                       # Justifica o texto na esquerda
        )
        whatsapp.pack(side = LEFT)                              # "Empacotar" o texto a esquerda

    def widgetswhatsappimg(self):                               # Widgets do frame whatsappimg
        self.b = PhotoImage(file = r'myprofile\telefone.png')   # Chamando a imagem (whatsappimg)
        self.img3 = Label( 
            self.whatsappimg,                                   # Mostrando que pertence ao frame whatsappimg
            image = self.b,                                     # Chamando a imagem
            bd = 0
        )
        self.img3.pack()

    def widgetsbotao(self):                                     # Widgets do frame botao
        self.btn1 = Button(                                     # Criando botao
            self.botao,                                         # Mostrando que pertence ao frame botao
            text = 'Voltar',                                    # Texto inserido no botão
            bg = self.cor1,                                     # Cor de fundo do botão
            activebackground = self.cor1,                       # Cor de fundo do botão quando acionado
            font = ('Poppins', 19),                             # Fonte no texto do botão
            fg = self.corprincipal,                             # Cor do texto
            activeforeground = self.corprincipal,               # Cor de fundo do texto quando o botão estiver acionado
            command = self.onClose                              # Comando atribuido ao botão
        )
        self.btn1.pack()
    
    def onClose(self):                                          # Criando comando para o botao
        self.destroy()                                          # Fechar a janela
        self.frame_original.show()                              # Mostrar janela principal