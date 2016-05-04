import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as tkm

class Telas():
    
    def __init__(self):
        #Cada pessoa deve ser uma chave de um dicionário
        #Por isso criar dicionário no começo dessa função
        #A chave é o nome de uma pessoa e os valres estarão em uma lista em uma mesma ordem
        self.dic_pessoas = {}
        
        self.bairros = ['','Vila Olímpia','Higienópolis','Morumbi','Jardins','Itaim','Jardim Boa Vista','Moema','Osasco','Itaquera','Alphaville','Pinheiros', 'Alto de Pinheiros']
        
        
        #Gerando a janela
        self.root = tk.Tk()
        self.root.title("Caronas Insper")
        self.root.geometry("640x800")
        self.root.rowconfigure(0, minsize=800)
        self.root.columnconfigure(0, minsize=640)
        self.root.grid()
        
        self.tela_inicial_frame() 
        
        
####   Telas:
    def tela_inicial_frame(self):
        
        self.tela_inicial = tk.Frame(self.root)
        self.tela_inicial.configure(bg='#E10022')
        
        self.tela_inicial.columnconfigure(0, minsize=213, weight=1)
        self.tela_inicial.columnconfigure(1, minsize=213, weight=1)
        self.tela_inicial.columnconfigure(2, minsize=213, weight=1)


        self.tela_inicial.rowconfigure(0, minsize=5, weight=1)
        self.tela_inicial.rowconfigure(1, minsize=60, weight=1)
        self.tela_inicial.rowconfigure(2, minsize=60, weight=1)
        self.tela_inicial.rowconfigure(3, minsize=205, weight=1)
        self.tela_inicial.rowconfigure(4, minsize=100, weight=1)
        self.tela_inicial.rowconfigure(5, minsize=45, weight=1)
        self.tela_inicial.rowconfigure(6, minsize=100, weight=1)
        self.tela_inicial.rowconfigure(7, minsize=205, weight=1)

        self.tela_inicial.grid(row=0, column=0, sticky="nsew")
        
        self.caronas = tk.Label(self.tela_inicial)
        self.caronas.grid(row=1, column=0,columnspan=3, sticky="nsew")
        self.caronas.configure(text= "Caronas",font='Bodoni 100', bg='#E10022', fg='White')
        
        self.Logo = tk.Label(self.tela_inicial)   
        self.Logo.grid(row=2, column=0,columnspan=3, sticky="nsew")
        self.Logo.configure(text= "Insper",font='Bodoni 100', bg='#E10022', fg='White')

        self.Login = tk.Button(self.tela_inicial)
        self.Login.grid(row=4, column=1, sticky="ew")
        self.Login.configure(text="Login", font='Arial 24')
        self.Login.bind('<1>',self.clicou_login)
        
        self.Cadastro = tk.Button(self.tela_inicial)
        self.Cadastro.grid(row=6, column=1, sticky="ew")
        self.Cadastro.configure(text="Cadastrar-se", font='Arial 24')
        self.Cadastro.bind('<1>',self.clicou_cadastro)

   
        
#######


    def Tela_login_frame(self):
        self.Tela_login = tk.Frame(self.root)
        self.Tela_login.configure(bg='#E10022')
        
        self.Tela_login.rowconfigure(0, minsize=50, weight=1)
        self.Tela_login.rowconfigure(1, minsize=50, weight=1)
        self.Tela_login.rowconfigure(2, minsize=100, weight=1)
        self.Tela_login.rowconfigure(3, minsize=100, weight=1)
        self.Tela_login.rowconfigure(4, minsize=100, weight=1)
        self.Tela_login.rowconfigure(5, minsize=100, weight=1)
        self.Tela_login.rowconfigure(6, minsize=100, weight=1)
        self.Tela_login.rowconfigure(7, minsize=100, weight=1)
        self.Tela_login.rowconfigure(8, minsize=50, weight=1)
        self.Tela_login.rowconfigure(9, minsize=50, weight=1)

        self.Tela_login.columnconfigure(0, minsize=20, weight=1)
        self.Tela_login.columnconfigure(1, minsize=200, weight=1)
        self.Tela_login.columnconfigure(2, minsize=200, weight=1)
        self.Tela_login.columnconfigure(3, minsize=200, weight=1)
        self.Tela_login.columnconfigure(4, minsize=20, weight=1)
        self.Tela_login.grid(row=0, column=0, sticky="nsew")
        
        self.caronas = tk.Label(self.Tela_login)
        self.caronas.grid(row=1, column=1,columnspan=3, sticky="nsew")
        self.caronas.configure(text= "Caronas",font='Bodoni 100', bg='#E10022', fg='White')
        
        self.Logo = tk.Label(self.Tela_login)
        self.Logo.grid(row=2, column=1,columnspan=3, sticky="nsew")
        self.Logo.configure(text= "Insper",font='Bodoni 100', bg='#E10022', fg='White')
        
        self.Usuário = tk.Label(self.Tela_login)
        self.Usuário.grid(row=4, column=1,columnspan=1, sticky="nsew")
        self.Usuário.configure(text= "Usuário: ",font='Bodoni 24', bg='#E10022', fg='White')
        
        self.entrada_usuario = tk.Entry(self.Tela_login)
        self.entrada_usuario.grid(row=4, column=2, sticky="ew")
        
        self.Senha = tk.Label(self.Tela_login)
        self.Senha.grid(row=5, column=1,columnspan=1, sticky="nsew")
        self.Senha.configure(text= "Senha: ",font='Bodoni 24', bg='#E10022', fg='White')
        
        self.entrada_senha = tk.Entry(self.Tela_login)
        self.entrada_senha.grid(row=5, column=2, sticky="ew")
        
        self.continuar_tela_principal = tk.Button(self.Tela_login)
        self.continuar_tela_principal.grid(row=6, column=3,columnspan=1)
        self.continuar_tela_principal.configure(text='Seguir')
        self.continuar_tela_principal.bind('<1>',self.clicou_continuar_tela_principal)
        
        self.voltar_tela_inicial = tk.Button(self.Tela_login)
        self.voltar_tela_inicial.grid(row=6, column=1,columnspan=1)
        self.voltar_tela_inicial.configure(text='Voltar')
        self.voltar_tela_inicial.bind('<1>',self.clicou_voltar_tela_inicial)
    
        
############# 
 
    
    def Tela_cadastro_frame(self):
        
        self.Tela_cadastro = tk.Frame(self.root)
        self.Tela_cadastro.configure(bg='#E10022')
        
        self.Tela_cadastro.rowconfigure(0, minsize=80, weight=1)
        self.Tela_cadastro.rowconfigure(1, minsize=80, weight=1)
        self.Tela_cadastro.rowconfigure(2, minsize=80, weight=1)
        self.Tela_cadastro.rowconfigure(3, minsize=80, weight=1)
        self.Tela_cadastro.rowconfigure(4, minsize=80, weight=1)
        self.Tela_cadastro.rowconfigure(5, minsize=80, weight=1)
        self.Tela_cadastro.rowconfigure(6, minsize=80, weight=1)
        self.Tela_cadastro.rowconfigure(7, minsize=80, weight=1)
        self.Tela_cadastro.rowconfigure(8, minsize=80, weight=1)
        self.Tela_cadastro.rowconfigure(9, minsize=80, weight=1)

        self.Tela_cadastro.columnconfigure(0, minsize=220, weight=1)
        self.Tela_cadastro.columnconfigure(1, minsize=200, weight=1)
        self.Tela_cadastro.columnconfigure(2, minsize=17, weight=1)

        self.Tela_cadastro.grid(row=0, column=0, sticky="nsew")
        
        self.caronas = tk.Label(self.Tela_cadastro)
        self.caronas.grid(row=0, column=0, columnspan=3, sticky="nsew")
        self.caronas.configure(text= "Caronas",font='Bodoni 50', bg='#E10022', fg='White')
        
        self.Logo = tk.Label(self.Tela_cadastro)   
        self.Logo.grid(row=1, column=0, columnspan=3, sticky="nsew")
        self.Logo.configure(text= "Insper",font='Bodoni 50', bg='#E10022', fg='White')

        
##########################################################################        
#Entrada de dados cadastro
##########################################################################

        #Nome Completo
        self.nome_entrada = tk.Entry(self.Tela_cadastro)
        self.nome_entrada.grid(row=2, column=1, sticky="ew")
        
        self.nome_label = tk.Label(self.Tela_cadastro)
        self.nome_label.grid(row=2, column=0, sticky="nsew")
        self.nome_label.configure(text= "Nome completo: ",font='Bodoni 24', bg='#E10022', fg='White')

        #E-mail
        self.email_entrada = tk.Entry(self.Tela_cadastro)
        self.email_entrada.grid(row=3, column=1, sticky="ew")
        
        self.email_label = tk.Label(self.Tela_cadastro)
        self.email_label.grid(row=3, column=0, sticky="nsew")
        self.email_label.configure(text= "E-mail: ",font='Bodoni 24', bg='#E10022', fg='White')

        #Número de Celular
        self.celular_entrada = tk.Entry(self.Tela_cadastro)
        self.celular_entrada.grid(row=4, column=1, sticky="ew")
        
        self.celular_label = tk.Label(self.Tela_cadastro)
        self.celular_label.grid(row=4, column=0, sticky="nsew")
        self.celular_label.configure(text= "Número de Celular*: ",font='Bodoni 24', bg='#E10022', fg='White')


        #Usuário
        self.usuario_entrada = tk.Entry(self.Tela_cadastro)
        self.usuario_entrada.grid(row=5, column=1, sticky="ew")
        
        self.usuario_label = tk.Label(self.Tela_cadastro)
        self.usuario_label.grid(row=5, column=0, sticky="nsew")
        self.usuario_label.configure(text= "Usuário: ",font='Bodoni 24', bg='#E10022', fg='White')

        #Senha
        self.senha_entrada = tk.Entry(self.Tela_cadastro)
        self.senha_entrada.grid(row=6, column=1, sticky="ew")
        
        self.senha_label = tk.Label(self.Tela_cadastro)
        self.senha_label.grid(row=6, column=0, sticky="nsew")
        self.senha_label.configure(text= "Senha: ",font='Bodoni 24', bg='#E10022', fg='White')

        #Confirmar Senha
        self.senha_confirma_entrada = tk.Entry(self.Tela_cadastro)
        self.senha_confirma_entrada.grid(row=7, column=1, sticky="ew")
        
        self.senha_confirma_label = tk.Label(self.Tela_cadastro)
        self.senha_confirma_label.grid(row=7, column=0, sticky="nsew")
        self.senha_confirma_label.configure(text= "Confirmar senha: ",font='Bodoni 24', bg='#E10022', fg='White')

        #Nota sobre o celular
        self.nota_label = tk.Label(self.Tela_cadastro)
        self.nota_label.grid(row=8, column=1, sticky="nsew")
        self.nota_label.configure(text= "*Mais importante do cadastro, digite apenas 9xxxx-xxxx",font='Bodoni 12', bg='#E10022', fg='White')

##########################################################################        
#Fim da entrada de dados do cadastro
##########################################################################
        
        self.salvar_novo_cadastro = tk.Button(self.Tela_cadastro)
        self.salvar_novo_cadastro.grid(row=8, column=3)
        self.salvar_novo_cadastro.configure(text='salvar')
        self.salvar_novo_cadastro.bind('<1>',self.clicou_salvar)
        
        self.voltar_tela_inicial = tk.Button(self.Tela_cadastro)
        self.voltar_tela_inicial.grid(row=8, column=0)
        self.voltar_tela_inicial.configure(text='Voltar')
        self.voltar_tela_inicial.bind('<1>',self.clicou_voltar_tela_inicial)

               
#########
               
    def tela_principal_frame(self):
        
        self.Tela_principal = tk.Frame(self.root)
        self.Tela_principal.configure(bg='#E10022')
        
        self.Tela_principal.rowconfigure(0, minsize=50, weight=1)
        self.Tela_principal.rowconfigure(1, minsize=50, weight=1)
        self.Tela_principal.rowconfigure(2, minsize=100, weight=1)
        self.Tela_principal.rowconfigure(3, minsize=100, weight=1)
        self.Tela_principal.rowconfigure(4, minsize=100, weight=1)
        self.Tela_principal.rowconfigure(5, minsize=100, weight=1)
        self.Tela_principal.rowconfigure(6, minsize=100, weight=1)
        self.Tela_principal.rowconfigure(7, minsize=100, weight=1)
        self.Tela_principal.rowconfigure(8, minsize=50, weight=1)
        self.Tela_principal.rowconfigure(9, minsize=50, weight=1)

        self.Tela_principal.columnconfigure(0, minsize=20, weight=1)
        self.Tela_principal.columnconfigure(1, minsize=200, weight=1)
        self.Tela_principal.columnconfigure(2, minsize=200, weight=1)
        self.Tela_principal.columnconfigure(3, minsize=200, weight=1)
        self.Tela_principal.columnconfigure(4, minsize=20, weight=1)
        self.Tela_principal.grid(row=0, column=0, sticky="nsew")
        
        
        
        self.caronas = tk.Label(self.Tela_principal)
        self.caronas.grid(row=1, column=1,columnspan=3, sticky="nsew")
        self.caronas.configure(text= "Caronas",font='Bodoni 100', bg='#E10022', fg='White')
        
        self.Logo = tk.Label(self.Tela_principal)
        self.Logo.grid(row=2, column=1,columnspan=3, sticky="nsew")
        self.Logo.configure(text= "Insper",font='Bodoni 100', bg='#E10022', fg='White')
        
        self.label = tk.Label(self.Tela_principal)
        self.label.grid(row=3, column=1,columnspan=3, sticky="nsew")
        self.label.configure(text= "O que deseja fazer? ",font='Bodoni 14', bg='#E10022', fg='White')
        
        self.pedir_carona = tk.Button(self.Tela_principal)
        self.pedir_carona.grid(row=4, column=1,columnspan=3)
        self.pedir_carona.configure(text= "Pedir Carona ",font='Bodoni 14')
        self.pedir_carona.bind('<1>',self.clicou_pedir)
        
        self.oferecer_carona = tk.Button(self.Tela_principal)
        self.oferecer_carona.grid(row=5, column=1,columnspan=3)
        self.oferecer_carona.configure(text= "Oferecer Carona ",font='Bodoni 14')
        self.oferecer_carona.bind('<1>',self.clicou_oferecer)
        
        self.alterar_perfil = tk.Button(self.Tela_principal)
        self.alterar_perfil.grid(row=6, column=1,columnspan=3)
        self.alterar_perfil.configure(text= "Alterar meu Perfil ",font='Bodoni 14')
        self.alterar_perfil.bind('<1>',self.clicou_alterar)


        #Botão que leva o usuário a página anterior
        self.voltar_pagina_principal = tk.Button(self.Tela_principal)
        self.voltar_pagina_principal.configure(text='Voltar')
        self.voltar_pagina_principal.grid(row=7, column=1,columnspan=1)
        self.voltar_pagina_principal.bind('<1>',self.clicou_voltar_login)


    def Tela_pedir_carona_frame(self):
        
        self.Tela_pedir_carona = tk.Frame(self.root)
        self.Tela_pedir_carona.configure(bg='#E10022')
        
        self.Tela_pedir_carona.rowconfigure(0, minsize=50, weight=1)
        self.Tela_pedir_carona.rowconfigure(1, minsize=50, weight=1)
        self.Tela_pedir_carona.rowconfigure(2, minsize=100, weight=1)
        self.Tela_pedir_carona.rowconfigure(3, minsize=100, weight=1)
        self.Tela_pedir_carona.rowconfigure(4, minsize=100, weight=1)
        self.Tela_pedir_carona.rowconfigure(5, minsize=100, weight=1)
        self.Tela_pedir_carona.rowconfigure(6, minsize=100, weight=1)
        self.Tela_pedir_carona.rowconfigure(7, minsize=100, weight=1)
        self.Tela_pedir_carona.rowconfigure(8, minsize=50, weight=1)
        self.Tela_pedir_carona.rowconfigure(9, minsize=50, weight=1)

        self.Tela_pedir_carona.columnconfigure(0, minsize=20, weight=1)
        self.Tela_pedir_carona.columnconfigure(1, minsize=200, weight=1)
        self.Tela_pedir_carona.columnconfigure(2, minsize=200, weight=1)
        self.Tela_pedir_carona.columnconfigure(3, minsize=200, weight=1)
        self.Tela_pedir_carona.columnconfigure(4, minsize=20, weight=1)
        self.Tela_pedir_carona.grid(row=0, column=0, sticky="nsew")
        
        
        self.caronas = tk.Label(self.Tela_pedir_carona)
        self.caronas.grid(row=1, column=1,columnspan=3, sticky="nsew")
        self.caronas.configure(text= "Caronas",font='Bodoni 100', bg='#E10022', fg='White')
        
        self.Logo = tk.Label(self.Tela_pedir_carona)
        self.Logo.grid(row=2, column=1,columnspan=3, sticky="nsew")
        self.Logo.configure(text= "Insper",font='Bodoni 100', bg='#E10022', fg='White')
        
        valor = tk.StringVar()
        valor.set(self.bairros[0])
        self.bairro_de_saida = ttk.OptionMenu(self.Tela_pedir_carona,valor,*self.bairros)
        self.bairro_de_saida.grid(row=4, column=2, sticky="ew")
        
        self.saida = tk.Label(self.Tela_pedir_carona)
        self.saida.grid(row=4, column=1,columnspan=1, sticky="nsew")
        self.saida.configure(text= "Local de saída: ",font='Bodoni 24', bg='#E10022', fg='White')
        
        #Espaço para o usuário escrever o destino
        valor = tk.StringVar()
        valor.set(self.bairros[0])
        self.bairro_de_chegada = ttk.OptionMenu(self.Tela_pedir_carona,valor,*self.bairros)
        self.bairro_de_chegada.grid(row=5, column=2, sticky="ew")
        
        self.chegada = tk.Label(self.Tela_pedir_carona)
        self.chegada.grid(row=5, column=0,columnspan=2, sticky="nsew")
        self.chegada.configure(text= "Local de chegada: ",font='Bodoni 24', bg='#E10022', fg='White')
        
        #Botão que confirma a ação do usuário
        self.confirmar = tk.Button(self.Tela_pedir_carona)
        self.confirmar.configure(text='Confirmar')
        self.confirmar.grid(row=6, column=3,columnspan=1)
        self.confirmar.bind('<1>',self.clicou_confirmar)
        self.confirmar.bind('<Return>',self.clicou_confirmar)
        
        #Botão que leva o usuário a página anterior
        self.voltar_pagina_principal = tk.Button(self.Tela_pedir_carona)
        self.voltar_pagina_principal.configure(text='Voltar')
        self.voltar_pagina_principal.grid(row=6, column=1,columnspan=1)
        self.voltar_pagina_principal.bind('<1>',self.clicou_voltar)
        
    def Tela_oferecer_carona_frame(self):
        
        self.Tela_oferecer_carona = tk.Frame(self.root)
        self.Tela_oferecer_carona.configure(bg='#E10022')
        
        self.Tela_oferecer_carona.rowconfigure(0, minsize=50, weight=1)
        self.Tela_oferecer_carona.rowconfigure(1, minsize=50, weight=1)
        self.Tela_oferecer_carona.rowconfigure(2, minsize=100, weight=1)
        self.Tela_oferecer_carona.rowconfigure(3, minsize=100, weight=1)
        self.Tela_oferecer_carona.rowconfigure(4, minsize=100, weight=1)
        self.Tela_oferecer_carona.rowconfigure(5, minsize=100, weight=1)
        self.Tela_oferecer_carona.rowconfigure(6, minsize=100, weight=1)
        self.Tela_oferecer_carona.rowconfigure(7, minsize=100, weight=1)
        self.Tela_oferecer_carona.rowconfigure(8, minsize=50, weight=1)
        self.Tela_oferecer_carona.rowconfigure(9, minsize=50, weight=1)

        self.Tela_oferecer_carona.columnconfigure(0, minsize=20, weight=1)
        self.Tela_oferecer_carona.columnconfigure(1, minsize=200, weight=1)
        self.Tela_oferecer_carona.columnconfigure(2, minsize=200, weight=1)
        self.Tela_oferecer_carona.columnconfigure(3, minsize=200, weight=1)
        self.Tela_oferecer_carona.columnconfigure(4, minsize=20, weight=1)
        self.Tela_oferecer_carona.grid(row=0, column=0, sticky="nsew")
        
        
        self.caronas = tk.Label(self.Tela_oferecer_carona)
        self.caronas.grid(row=1, column=1,columnspan=3, sticky="nsew")
        self.caronas.configure(text= "Caronas",font='Bodoni 100', bg='#E10022', fg='White')
        
        self.Logo = tk.Label(self.Tela_oferecer_carona)
        self.Logo.grid(row=2, column=1,columnspan=3, sticky="nsew")
        self.Logo.configure(text= "Insper",font='Bodoni 100', bg='#E10022', fg='White')
        
        #Espaço para o usuário escrever a saída
        valor = tk.StringVar()
        valor.set(self.bairros[0])
        self.bairro_de_saida = ttk.OptionMenu(self.Tela_oferecer_carona,valor,*self.bairros)
        self.bairro_de_saida.grid(row=4, column=2, sticky="ew")
        
        self.saida = tk.Label(self.Tela_oferecer_carona)
        self.saida.grid(row=4, column=1,columnspan=1, sticky="nsew")
        self.saida.configure(text= "Local de saída: ",font='Bodoni 24', bg='#E10022', fg='White')
        
        #Espaço para o usuário escrever o destino
        valor = tk.StringVar()
        valor.set(self.bairros[0])
        self.bairro_de_chegada = ttk.OptionMenu(self.Tela_oferecer_carona,valor,*self.bairros)
        self.bairro_de_chegada.grid(row=5, column=2, sticky="ew")
        
        self.chegada = tk.Label(self.Tela_oferecer_carona)
        self.chegada.grid(row=5, column=0,columnspan=2, sticky="nsew")
        self.chegada.configure(text= "Local de chegada: ",font='Bodoni 24', bg='#E10022', fg='White')
        
        #Botão que confirma a ação do usuário
        self.confirmar = tk.Button(self.Tela_oferecer_carona)
        self.confirmar.configure(text='Confirmar')
        self.confirmar.grid(row=6, column=3,columnspan=1)
        self.confirmar.bind('<1>',self.clicou_confirmar)
        self.confirmar.bind('<Return>',self.clicou_confirmar)
        
        #Botão que leva o usuário a página anterior
        self.voltar_pagina_principal = tk.Button(self.Tela_oferecer_carona)
        self.voltar_pagina_principal.configure(text='Voltar')
        self.voltar_pagina_principal.grid(row=6, column=1,columnspan=1)
        self.voltar_pagina_principal.bind('<1>',self.clicou_voltar)

        

####################     Função dos botões

    def clicou_cadastro(self,event):
        self.Tela_cadastro_frame() 
        
        
    def clicou_login(self,event):
        self.Tela_login_frame()

    def clicou_continuar_tela_principal(self,event):
#        cadastros = open('cadastros.txt','r')
#        cadastros.readline()
#        print (cadastros)
#        cadastros.close()
#
#        senha = self.dic_pessoas[self.entrada_usuario.get()]
#
#        if (self.entrada_usuario.get() in self.dic_pessoas) and senha[1]==self.entrada_senha.get():
#            self.tela_principal()
#        else:
#            print ('feio')
#            #tkm.showinfo(title='Erro',message='Usuário ou senha incorreto!')
        self.tela_principal_frame()

            
        
    def clicou_voltar_tela_inicial(self,event):
        self.tela_inicial_frame()
        
    def clicou_salvar(self,event):
    
        confirmando_cadastro = tkm.askyesno('Confirmando','Deseja confirmar as informações?')
        if confirmando_cadastro:
            #Nome no índice 0 da lista
            #Senha no índice 1 da lista
            #Celular no índice 2 da lista
            #E-mail no índice 3 da lista
            self.dic_pessoas[self.usuario_entrada.get()]=[self.nome_entrada.get(),self.senha_entrada.get(), self.celular_entrada.get(), self.email_entrada.get()]
            self.novo_arquivo = open('cadastros.txt','a') #Arquivo onde as informações serão salvas
            self.novo_arquivo.write('\n{0}'.format(self.dic_pessoas)) #Escrevendo o login
            self.novo_arquivo.close() #Fechando o arquivo
            self.Tela_login_frame()
        else:
            pass
        
    def clicou_pedir(self,event):
        self.Tela_pedir_carona_frame()
                
    def clicou_voltar(self,event):
        self.tela_principal_frame()
        
    def clicou_confirmar(self,event):
        pass

    def clicou_oferecer(self,event):
        self.Tela_oferecer_carona_frame()

    def clicou_alterar(self,event):
#        self.perfil()
        pass
    
    def clicou_voltar_login(self,event):
        self.Tela_login_frame()

        

        
    
########## iniciando o programa
    def iniciar(self):
        self.root.mainloop()

Caronas = Telas()
Caronas.iniciar()