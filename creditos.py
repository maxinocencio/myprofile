from tkinter import *                               # Importanto a biblioteca tkinter

class Creditos(Toplevel):                           # Criando a segunda tela (Sobre mim)
    corprincipal = '#4594E5'                        # Cor principal (background) Azul
    cor1 = '#ffffff'                                # Cor secundaria (Textos e etc) Branco

    def __init__(self, original):                   # Método construtor
        self.frame_original = original
        Toplevel.__init__(self)

        self.config()                               # Chamando as configurações da janela
        self.frames()                               # Chamando todos os frames da segunda tela
        
        self.widgetstitulo()                        # Chamando os widgets do frame título   (Texto, Sobre Mim)
        self.widgetslogo()                          # Chamando os widgets do frame logo     (Imagem, logo)
        self.widgetscred()                          # Chamando os widgets do frame cred     (Texto, Creditos)
        self.widgetsbotao()                         # Chamando os widgets do frame botao   (Botão, Voltar)

    def config(self):                               # Configurações da janela 3
        self.title('Sobre Mim')                     # Título da janela
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
            bg = self.cor1                          # Determinando a cor de fundo do frame
        )

        self.logo.place(                            # Determinando onde o frame logo ficará
            relx = 0.11,
            rely = 0.08,
            relwidth = 0.1275,
            relheight = 0.072
        )

        self.cred = Frame(                          # Criando frame cred (creditos)
            self,
            bg = self.corprincipal                  # Determinando a cor de fundo do frame
        )

        self.cred.place(                            # Determinando onde o frame cred ficará
            relx = 0.1,
            rely = 0.25,
            relwidth = 0.75,
            relheight = 0.2
        )

        self.botao = Frame(                         # Criando frame botao
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
            text='Creditos',                                   # Texto que será inserido no frame
            font=('Poppins', 30, 'bold'),                       # Fonte usada no texto
            bg = self.corprincipal,                             # Cor backgroud do texto
            fg = self.cor1,                                     # Cor do texto
        )
        title.place(                                            # Determinando onde o texto ficará
            relx = 0.1
        )

    def widgetscred(self):                                      # Widgets do frame desc
        cred = Label(self.cred,

            text = 'Criado por: Max Inocêncio \nVersão 1 \n2021',   # Texto que será inserido no frame
            font=('Poppins', 14, 'bold'),                       # Fonte usada no texto
            bg = self.corprincipal,                             # Cor backgroud do texto
            fg = self.cor1,                                     # Cor do texto
            justify=LEFT,                                       # Justifica o texto na esquerda
        )
        cred.pack(side = LEFT)                                  # "Empacotar" o texto a esquerda

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