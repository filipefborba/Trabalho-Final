import tkinter as tk


#Classe que faz a página de pedir carona
class pedir_carona:
    def __init__(self):
        #Gerando a janela
        self.window = tk.Tk()
        self.window.title("Caronas Insper")
        self.window.geometry("640x800")
        self.window.configure(background='#E10022')
        self.window.rowconfigure(0, minsize=100, weight=1)
        self.window.rowconfigure(1, minsize=100, weight=1)
        self.window.rowconfigure(2, minsize=100, weight=1)
        self.window.rowconfigure(3, minsize=200, weight=1)
        self.window.rowconfigure(4, minsize=100, weight=1)
        self.window.rowconfigure(5, minsize=100, weight=1)
        self.window.rowconfigure(6, minsize=50, weight=1)
        self.window.rowconfigure(7, minsize=50, weight=1)
        self.window.columnconfigure(0, minsize=20, weight=1)
        self.window.columnconfigure(1, minsize=200, weight=1)
        self.window.columnconfigure(2, minsize=200, weight=1)
        self.window.columnconfigure(3, minsize=200, weight=1)
        self.window.columnconfigure(4, minsize=20, weight=1)
        
##########################################################################        
#Entrada de dados cadastro
##########################################################################
        #Nome Completo
        self.nomeentrada = tk.Entry(self.window)
        self.nomeentrada.grid(row=5, column=2, sticky="ew")
        self.nomeentrada.bind('<Return>',self.clicou_confirmar)
        
        self.nomelabel = tk.Label(self.window)
        self.nomelabel.grid(row=5, column=0,columnspan=2, sticky="nsew")
        self.nomelabel.configure(text= "Nome completo: ",font='Bodoni 24', bg='#E10022', fg='White')

        #E-mail
        self.emailentrada = tk.Entry(self.window)
        self.emailentrada.grid(row=5, column=2, sticky="ew")
        self.emailentrada.bind('<Return>',self.clicou_confirmar)
        
        self.emaillabel = tk.Label(self.window)
        self.emailabel.grid(row=5, column=0,columnspan=2, sticky="nsew")
        self.emailabel.configure(text= "Local de chegada: ",font='Bodoni 24', bg='#E10022', fg='White')

        #Número de Celular
        self.celularentrada = tk.Entry(self.window)
        self.celularentrada.grid(row=5, column=2, sticky="ew")
        self.celularentrada.bind('<Return>',self.clicou_confirmar)
        
        self.celularlabel = tk.Label(self.window)
        self.celularlabel.grid(row=5, column=0,columnspan=2, sticky="nsew")
        self.celularlabel.configure(text= "Local de chegada: ",font='Bodoni 24', bg='#E10022', fg='White')

        #Usuário
        self.usuarioentrada = tk.Entry(self.window)
        self.usuarioentrada.grid(row=5, column=2, sticky="ew")
        self.nomeentrada.bind('<Return>',self.clicou_confirmar)
        
        self.nomelabel = tk.Label(self.window)
        self.nomelabel.grid(row=5, column=0,columnspan=2, sticky="nsew")
        self.nomelabel.configure(text= "Local de chegada: ",font='Bodoni 24', bg='#E10022', fg='White')

        #Senha
        self.nomeentrada = tk.Entry(self.window)
        self.nomeentrada.grid(row=5, column=2, sticky="ew")
        self.nomeentrada.bind('<Return>',self.clicou_confirmar)
        
        self.nomelabel = tk.Label(self.window)
        self.nomelabel.grid(row=5, column=0,columnspan=2, sticky="nsew")
        self.nomelabel.configure(text= "Local de chegada: ",font='Bodoni 24', bg='#E10022', fg='White')

        #Confirmar Senha
        self.nomeentrada = tk.Entry(self.window)
        self.nomeentrada.grid(row=5, column=2, sticky="ew")
        self.nomeentrada.bind('<Return>',self.clicou_confirmar)
        
        self.nomelabel = tk.Label(self.window)
        self.nomelabel.grid(row=5, column=0,columnspan=2, sticky="nsew")
        self.nomelabel.configure(text= "Local de chegada: ",font='Bodoni 24', bg='#E10022', fg='White')

##########################################################################        
#Fim da entrada de dados do cadastro
##########################################################################
        
        #Botão que confirma a ação do usuário
        self.confirmar = tk.Button(self.window)
        self.confirmar.configure(text='Confirmar')
        self.confirmar.grid(row=6, column=3,columnspan=1)
        self.confirmar.bind('<1>',self.clicou_confirmar)
        self.confirmar.bind('<Return>',self.clicou_confirmar)
        
        #Botão que leva o usuário a página anterior
        self.voltar_pagina_principal = tk.Button(self.window)
        self.voltar_pagina_principal.configure(text='Voltar')
        self.voltar_pagina_principal.grid(row=6, column=1,columnspan=1)
        self.voltar_pagina_principal.bind('<1>',self.clicou_voltar)
        
    def iniciar(self):
        self.window.mainloop()
        
    def clicou_confirmar(self,event):
        pass
        
    def clicou_voltar(self,event):
        pass
        
teste = pedir_carona()
teste.iniciar()