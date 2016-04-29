import tkinter as tk


class Telas():
    
    def __init__(self):
        #Cada pessoa deve ser uma chave de um dicionário
        #Por isso criar dicionário no começo dessa função
        #A chave é o nome de uma pessoa e os valres estarão em uma lista em uma mesma ordem
        self.dic_pessoas = {}

        #Gerando a janela
        self.window = tk.Tk()
        self.window.title("Caronas Insper")
        self.window.geometry("640x800")
        self.window.configure(background='#E10022')

        self.window.rowconfigure(0, minsize=50, weight=1)
        self.window.rowconfigure(1, minsize=50, weight=1)
        self.window.rowconfigure(2, minsize=100, weight=1)
        self.window.rowconfigure(3, minsize=100, weight=1)
        self.window.rowconfigure(4, minsize=100, weight=1)
        self.window.rowconfigure(5, minsize=100, weight=1)
        self.window.rowconfigure(6, minsize=100, weight=1)
        self.window.rowconfigure(7, minsize=100, weight=1)
        self.window.rowconfigure(8, minsize=50, weight=1)
        self.window.rowconfigure(9, minsize=50, weight=1)

        self.window.columnconfigure(0, minsize=20, weight=1)
        self.window.columnconfigure(1, minsize=200, weight=1)
        self.window.columnconfigure(2, minsize=200, weight=1)
        self.window.columnconfigure(3, minsize=200, weight=1)
        self.window.columnconfigure(4, minsize=20, weight=1)
        self.tela_inicial() 
        

        
        
####   Telas:
    def  tela_inicial(self):
        self.caronas = tk.Label(self.window)
        self.caronas.grid(row=0, column=1,columnspan=3, sticky="nsew")
        self.caronas.configure(text= "Caronas",font='Bodoni 50', bg='#E10022', fg='White')
        
        self.Logo = tk.Label(self.window)
        self.Logo.grid(row=1, column=1,columnspan=3, sticky="nsew")
        self.Logo.configure(text= "Insper",font='Bodoni 50', bg='#E10022', fg='White')

        self.Login = tk.Button(self.window)
        self.Login.grid(row=4, column=2, sticky="ew")
        self.Login.configure(text="Login", font='Arial 24')
        self.Login.bind('<1>',self.clicou_login)
        
        self.Cadastro = tk.Button(self.window)
        self.Cadastro.grid(row=5, column=2, sticky="ew")
        self.Cadastro.configure(text="Cadastrar-se", font='Arial 24')
        self.Cadastro.bind('<1>',self.clicou_cadastro)

   
        
#######


    def Tela_login(self):
        self.Usuário = tk.Label(self.window)
        self.Usuário.grid(row=4, column=1,columnspan=1, sticky="nsew")
        self.Usuário.configure(text= "Usuário: ",font='Bodoni 24', bg='#E10022', fg='White')
        
        self.entrada_usuário = tk.Entry(self.window)
        self.entrada_usuário.grid(row=4, column=2, sticky="ew")
        
        self.Senha = tk.Label(self.window)
        self.Senha.grid(row=5, column=1,columnspan=1, sticky="nsew")
        self.Senha.configure(text= "Senha: ",font='Bodoni 24', bg='#E10022', fg='White')
        
        self.entrada_senha = tk.Entry(self.window)
        self.entrada_senha.grid(row=5, column=2, sticky="ew")
        
        self.continuar_tela_principal = tk.Button(self.window)
        self.continuar_tela_principal.grid(row=6, column=3,columnspan=1)
        self.continuar_tela_principal.configure(text='Seguir')
        self.continuar_tela_principal.bind('<1>',self.clicou_continuar_tela_principal)
        
        self.voltar_tela_inicial = tk.Button(self.window)
        self.voltar_tela_inicial.grid(row=6, column=1,columnspan=1)
        self.voltar_tela_inicial.configure(text='Voltar')
        self.voltar_tela_inicial.bind('<1>',self.clicou_voltar_tela_inicial)
    
        
############# 
 
    
    def Tela_cadastro(self):
        
##########################################################################        
#Entrada de dados cadastro
##########################################################################

        #Nome Completo
        self.nome_entrada = tk.Entry(self.window)
        self.nome_entrada.grid(row=2, column=2, sticky="ew")
        
        self.nome_label = tk.Label(self.window)
        self.nome_label.grid(row=2, column=1,columnspan=1, sticky="nsew")
        self.nome_label.configure(text= "Nome completo: ",font='Bodoni 24', bg='#E10022', fg='White')

        #E-mail
        self.email_entrada = tk.Entry(self.window)
        self.email_entrada.grid(row=3, column=2, sticky="ew")
        
        self.email_label = tk.Label(self.window)
        self.email_label.grid(row=3, column=1,columnspan=1, sticky="nsew")
        self.email_label.configure(text= "E-mail: ",font='Bodoni 24', bg='#E10022', fg='White')

        #Número de Celular
        self.celular_entrada = tk.Entry(self.window)
        self.celular_entrada.grid(row=4, column=2, sticky="ew")
        
        self.celular_label = tk.Label(self.window)
        self.celular_label.grid(row=4, column=1,columnspan=1, sticky="nsew")
        self.celular_label.configure(text= "Número de Celular*: ",font='Bodoni 24', bg='#E10022', fg='White')


        #Usuário
        self.usuario_entrada = tk.Entry(self.window)
        self.usuario_entrada.grid(row=5, column=2, sticky="ew")
        
        self.usuario_label = tk.Label(self.window)
        self.usuario_label.grid(row=5, column=1,columnspan=1, sticky="nsew")
        self.usuario_label.configure(text= "Usuário: ",font='Bodoni 24', bg='#E10022', fg='White')

        #Senha
        self.senha_entrada = tk.Entry(self.window)
        self.senha_entrada.grid(row=6, column=2, sticky="ew")
        
        self.senha_label = tk.Label(self.window)
        self.senha_label.grid(row=6, column=1,columnspan=1, sticky="nsew")
        self.senha_label.configure(text= "Senha: ",font='Bodoni 24', bg='#E10022', fg='White')

        #Confirmar Senha
        self.senha_confirma_entrada = tk.Entry(self.window)
        self.senha_confirma_entrada.grid(row=7, column=2, sticky="ew")
        
        self.senha_confirma_label = tk.Label(self.window)
        self.senha_confirma_label.grid(row=7, column=1,columnspan=1, sticky="nsew")
        self.senha_confirma_label.configure(text= "Confirmar senha: ",font='Bodoni 24', bg='#E10022', fg='White')

        #Nota sobre o celular
        self.nota_label = tk.Label(self.window)
        self.nota_label.grid(row=8, column=1,columnspan=3, sticky="nsew")
        self.nota_label.configure(text= "*Mais importante do cadastro, digite apenas 9xxxx-xxxx",font='Bodoni 12', bg='#E10022', fg='White')

##########################################################################        
#Fim da entrada de dados do cadastro
##########################################################################
        
        self.salvar_novo_cadastro = tk.Button(self.window)
        self.salvar_novo_cadastro.grid(row=9, column=3,columnspan=1)
        self.salvar_novo_cadastro.configure(text='salvar')
        self.salvar_novo_cadastro.bind('<1>',self.clicou_salvar)
        
        self.voltar_tela_inicial = tk.Button(self.window)
        self.voltar_tela_inicial.grid(row=9, column=1,columnspan=1)
        self.voltar_tela_inicial.configure(text='Voltar')
        self.voltar_tela_inicial.bind('<1>',self.clicou_voltar_tela_inicial)

               
#########
               
    def tela_principal(self):
        
        self.caronas = tk.Label(self.window)
        self.caronas.grid(row=1, column=1,columnspan=3, sticky="nsew")
        self.caronas.configure(text= "Caronas",font='Bodoni 100', bg='#E10022', fg='White')
        
        self.Logo = tk.Label(self.window)
        self.Logo.grid(row=2, column=1,columnspan=3, sticky="nsew")
        self.Logo.configure(text= "Insper",font='Bodoni 100', bg='#E10022', fg='White')
        
        self.label = tk.Label(self.window)
        self.label.grid(row=3, column=1,columnspan=3, sticky="nsew")
        self.label.configure(text= "O que deseja fazer? ",font='Bodoni 14', bg='#E10022', fg='White')
        
        self.pedir_carona = tk.Button(self.window)
        self.pedir_carona.grid(row=4, column=1,columnspan=3, sticky="nsew")
        self.pedir_carona.configure(text= "Pedir Carona ",font='Bodoni 14')
        self.pedir_carona.bind('<1>',self.clicou_pedir)
        
        self.oferecer_carona = tk.Button(self.window)
        self.oferecer_carona.grid(row=5, column=1,columnspan=3, sticky="nsew")
        self.oferecer_carona.configure(text= "Oferecer Carona ",font='Bodoni 14')
        self.oferecer_carona.bind('<1>',self.clicou_oferecer)
        
        self.alterar_perfil = tk.Button(self.window)
        self.alterar_perfil.grid(row=6, column=1,columnspan=3, sticky="nsew")
        self.alterar_perfil.configure(text= "Alterar meu Perfil ",font='Bodoni 14')
        self.alterar_perfil.bind('<1>',self.clicou_alterar)

    def Tela_pedir_carona(self):
        self.caronas = tk.Label(self.window)
        self.caronas.grid(row=1, column=1,columnspan=3, sticky="nsew")
        self.caronas.configure(text= "Caronas",font='Bodoni 100', bg='#E10022', fg='White')
        
        self.Logo = tk.Label(self.window)
        self.Logo.grid(row=2, column=1,columnspan=3, sticky="nsew")
        self.Logo.configure(text= "Insper",font='Bodoni 100', bg='#E10022', fg='White')
        
        #Espaço para o usuário escrever a saída
        self.bairro_de_saida = tk.Entry(self.window)
        self.bairro_de_saida.grid(row=4, column=2, sticky="ew")
        self.bairro_de_saida.bind('<Return>',self.clicou_confirmar)
        
        self.saida = tk.Label(self.window)
        self.saida.grid(row=4, column=1,columnspan=1, sticky="nsew")
        self.saida.configure(text= "Local de saída: ",font='Bodoni 24', bg='#E10022', fg='White')
        
        #Espaço para o usuário escrever o destino
        self.bairro_de_chegada = tk.Entry(self.window)
        self.bairro_de_chegada.grid(row=5, column=2, sticky="ew")
        self.bairro_de_chegada.bind('<Return>',self.clicou_confirmar)
        
        self.chegada = tk.Label(self.window)
        self.chegada.grid(row=5, column=0,columnspan=2, sticky="nsew")
        self.chegada.configure(text= "Local de chegada: ",font='Bodoni 24', bg='#E10022', fg='White')
        
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

#########
        
    def Tela_oferecer_carona(self):
        self.caronas = tk.Label(self.window)
        self.caronas.grid(row=1, column=1,columnspan=3, sticky="nsew")
        self.caronas.configure(text= "Caronas",font='Bodoni 100', bg='#E10022', fg='White')
        
        self.Logo = tk.Label(self.window)
        self.Logo.grid(row=2, column=1,columnspan=3, sticky="nsew")
        self.Logo.configure(text= "Insper",font='Bodoni 100', bg='#E10022', fg='White')
        
        #Espaço para o usuário escrever a saída
        self.bairro_de_saida = tk.Entry(self.window)
        self.bairro_de_saida.grid(row=4, column=2, sticky="ew")
        self.bairro_de_saida.bind('<Return>',self.clicou_confirmar)
        
        self.saida = tk.Label(self.window)
        self.saida.grid(row=4, column=1,columnspan=1, sticky="nsew")
        self.saida.configure(text= "Local de saída: ",font='Bodoni 24', bg='#E10022', fg='White')
        
        #Espaço para o usuário escrever o destino
        self.bairro_de_chegada = tk.Entry(self.window)
        self.bairro_de_chegada.grid(row=5, column=2, sticky="ew")
        self.bairro_de_chegada.bind('<Return>',self.clicou_confirmar)
        
        self.chegada = tk.Label(self.window)
        self.chegada.grid(row=5, column=0,columnspan=2, sticky="nsew")
        self.chegada.configure(text= "Local de chegada: ",font='Bodoni 24', bg='#E10022', fg='White')
        
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

        

####################     Função dos botões

    def clicou_cadastro(self,event):
        self.Tela_cadastro() 
        
        
    def clicou_login(self,event):
        self.Tela_login()

    def clicou_continuar_tela_principal(self,event):
        self.tela_principal()        
        
    def clicou_voltar_tela_inicial(self,event):
        self.tela_inicial()
        
    def clicou_salvar(self,event):

        #Nome no índice 0 da lista
        #Senha no índice 1 da lista
        #Celular no índice 2 da lista
        #E-mail no índice 3 da lista
        self.dic_pessoas[self.usuario_entrada.get()]=[self.nome_entrada.get(),self.senha_entrada.get(), self.celular_entrada.get(), self.email_entrada.get()]
        self.novo_arquivo = open('cadastros.txt','a') #Arquivo onde as informações serão salvas
        self.novo_arquivo.write('\n{0}'.format(self.dic_pessoas)) #Escrevendo o login
        self.novo_arquivo.close() #Fechando o arquivo
        self.Tela_login()
        
    def clicou_pedir(self,event):
        self.Tela_pedir_carona()
                
    def clicou_voltar(self,event):
        self.tela_principal()
        
    def clicou_confirmar(self,event):
        pass

    def clicou_oferecer(self,event):
        self.Tela_oferecer_carona()

    def clicou_alterar(self,event):
#        self.perfil()
        pass
    
########## iniciando o programa
    def iniciar(self):
        self.window.mainloop()

Caronas = Telas()
Caronas.iniciar()