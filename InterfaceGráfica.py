import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as tkm
from firebase import firebase
import smtplib

class Telas():
    
    def __init__(self):
        #Listas com bairros disponiveis para carona, horários de saída e lugares disponiveis no carro
        self.bairros = sorted(['','Cerqueira César','Vila Leopoldina','Vila Olímpia','Higienópolis','Morumbi','Jardins','Itaim','Jardim Paulista','Moema','Osasco','Itaquera','Alphaville','Pinheiros', 'Alto de Pinheiros', 'Jardim Paulistano', 'Jardim Europa', 'Paraíso','Perdizes','Campo Belo','Consolação','Aclimação','Chácara Inglesa','Chácara Klabin','Butantã'])
        self.horarios = ['','6h00','6h30','7h00','7h30','8h00','8h30','9h00','9h30','10h00','10h30','11h00','11h30','12h00','12h30','13h00','13h30','14h00','14h30','15h00','16h00','16h30','17h00','17h30','18h00','18h30','19h00','19h30','20h00','20h30','21h00','21h30','22h00','22h30','23h00']
        self.lugares = ['','1','2','3','4']        
        
        #Gerando a janela
        self.root = tk.Tk()
        self.root.title("Caronas Insper")
        self.root.geometry("600x600")
        self.root.rowconfigure(0, minsize=600)
        self.root.columnconfigure(0, minsize=600)
        self.root.resizable(width=False, height=False)
        self.root.grid()
        
        self.tela_inicial_frame()
        
        
####   Telas:
    def tela_inicial_frame(self):
        
        self.tela_inicial = tk.Frame(self.root)
        self.tela_inicial.configure(bg='#E10022')
        
        self.tela_inicial.columnconfigure(0, minsize=100, weight=1)
        self.tela_inicial.columnconfigure(1, minsize=100, weight=1)
        self.tela_inicial.columnconfigure(2, minsize=100, weight=1)


        self.tela_inicial.rowconfigure(0, minsize=5, weight=1)
        self.tela_inicial.rowconfigure(1, minsize=30, weight=1)
        self.tela_inicial.rowconfigure(2, minsize=30, weight=1)
        self.tela_inicial.rowconfigure(3, minsize=100, weight=1)
        self.tela_inicial.rowconfigure(4, minsize=50, weight=1)
        self.tela_inicial.rowconfigure(5, minsize=50, weight=1)
        self.tela_inicial.rowconfigure(6, minsize=50, weight=1)
        self.tela_inicial.rowconfigure(7, minsize=50, weight=1)
        self.tela_inicial.rowconfigure(8, minsize=50, weight=1)


        self.tela_inicial.grid(row=0, column=0, sticky="nsew")
        
        self.caronas = tk.Label(self.tela_inicial)
        self.caronas.grid(row=1, column=0,columnspan=3, sticky="nsew")
        self.caronas.configure(text= "Caronas",font='Bodoni 75', bg='#E10022', fg='White')
        
        self.Logo = tk.Label(self.tela_inicial)   
        self.Logo.grid(row=2, column=0,columnspan=3, sticky="nsew")
        self.Logo.configure(text= "Insper",font='Bodoni 75', bg='#E10022', fg='White')

        self.Login = tk.Button(self.tela_inicial)
        self.Login.grid(row=4, column=1, sticky="ew")
        self.Login.configure(text="Login", font='Arial 20')
        self.Login.bind('<1>',self.clicou_login)
        
        self.Cadastro = tk.Button(self.tela_inicial)
        self.Cadastro.grid(row=5, column=1, sticky="ew")
        self.Cadastro.configure(text="Cadastrar-se", font='Arial 20')
        self.Cadastro.bind('<1>',self.clicou_cadastro)
        
        self.sobre_nós = tk.Button(self.tela_inicial)
        self.sobre_nós.grid(row=6, column=1, sticky="ew")
        self.sobre_nós.configure(text="Sobre", font='Arial 20')
        self.sobre_nós.bind('<1>',self.clicou_sobre_nós)
        
        self.contato = tk.Button(self.tela_inicial)
        self.contato.grid(row=7, column=1, sticky="ew")
        self.contato.configure(text="Contato", font='Arial 20')
        self.contato.bind('<1>',self.clicou_contato)

   
        
#######
    

    def Tela_login_frame(self):
        self.Tela_login = tk.Frame(self.root)
        self.Tela_login.configure(bg='#E10022')
        
        self.Tela_login.rowconfigure(0, minsize=25, weight=1)
        self.Tela_login.rowconfigure(1, minsize=25, weight=1)
        self.Tela_login.rowconfigure(2, minsize=50, weight=1)
        self.Tela_login.rowconfigure(3, minsize=50, weight=1)
        self.Tela_login.rowconfigure(4, minsize=50, weight=1)
        self.Tela_login.rowconfigure(5, minsize=50, weight=1)
        self.Tela_login.rowconfigure(6, minsize=50, weight=1)
        self.Tela_login.rowconfigure(7, minsize=50, weight=1)
        self.Tela_login.rowconfigure(8, minsize=25, weight=1)
        self.Tela_login.rowconfigure(9, minsize=25, weight=1)

        self.Tela_login.columnconfigure(0, minsize=10, weight=1)
        self.Tela_login.columnconfigure(1, minsize=100, weight=1)
        self.Tela_login.columnconfigure(2, minsize=100, weight=1)
        self.Tela_login.columnconfigure(3, minsize=100, weight=1)
        self.Tela_login.columnconfigure(4, minsize=10, weight=1)
        self.Tela_login.grid(row=0, column=0, sticky="nsew")
        
        self.caronas = tk.Label(self.Tela_login)
        self.caronas.grid(row=1, column=1,columnspan=3, sticky="nsew")
        self.caronas.configure(text= "Caronas",font='Bodoni 75', bg='#E10022', fg='White')
        
        self.Logo = tk.Label(self.Tela_login)
        self.Logo.grid(row=2, column=1,columnspan=3, sticky="nsew")
        self.Logo.configure(text= "Insper",font='Bodoni 75', bg='#E10022', fg='White')
        
        self.Usuário = tk.Label(self.Tela_login)
        self.Usuário.grid(row=4, column=1,columnspan=1, sticky="nsew")
        self.Usuário.configure(text= "Usuário: ",font='Bodoni 20', bg='#E10022', fg='White')
        
        self.entrada_usuario = tk.Entry(self.Tela_login)
        self.entrada_usuario.grid(row=4, column=2, sticky="ew")
        self.entrada_usuario.bind('<Return>',self.clicou_continuar_tela_principal)
        
        self.Senha = tk.Label(self.Tela_login)
        self.Senha.grid(row=5, column=1,columnspan=1, sticky="nsew")
        self.Senha.configure(text= "Senha: ",font='Bodoni 20', bg='#E10022', fg='White')
        
        self.entrada_senha = tk.Entry(self.Tela_login)
        self.entrada_senha.grid(row=5, column=2, sticky="ew")
        self.entrada_senha.configure(show='*')
        self.entrada_senha.bind('<Return>',self.clicou_continuar_tela_principal)
        
        self.continuar_tela_principal = tk.Button(self.Tela_login)
        self.continuar_tela_principal.grid(row=6, column=3,columnspan=1)
        self.continuar_tela_principal.configure(text='Seguir')
        self.continuar_tela_principal.bind('<1>',self.clicou_continuar_tela_principal)
        self.continuar_tela_principal.bind('<Return>',self.clicou_continuar_tela_principal)
        
        self.voltar_tela_inicial = tk.Button(self.Tela_login)
        self.voltar_tela_inicial.grid(row=6, column=1,columnspan=1)
        self.voltar_tela_inicial.configure(text='Voltar')
        self.voltar_tela_inicial.bind('<1>',self.clicou_voltar_tela_inicial)
        self.voltar_tela_inicial.bind('<Return>',self.clicou_voltar_tela_inicial)
    
        
#############    
 
    
    def Tela_cadastro_frame(self):
        
        self.Tela_cadastro = tk.Frame(self.root)
        self.Tela_cadastro.configure(bg='#E10022')
        
        self.Tela_cadastro.rowconfigure(0, minsize=40, weight=1)
        self.Tela_cadastro.rowconfigure(1, minsize=40, weight=1)
        self.Tela_cadastro.rowconfigure(2, minsize=40, weight=1)
        self.Tela_cadastro.rowconfigure(3, minsize=40, weight=1)
        self.Tela_cadastro.rowconfigure(4, minsize=40, weight=1)
        self.Tela_cadastro.rowconfigure(5, minsize=40, weight=1)
        self.Tela_cadastro.rowconfigure(6, minsize=40, weight=1)
        self.Tela_cadastro.rowconfigure(7, minsize=40, weight=1)
        self.Tela_cadastro.rowconfigure(8, minsize=40, weight=1)
        self.Tela_cadastro.rowconfigure(9, minsize=40, weight=1)

        self.Tela_cadastro.columnconfigure(0, minsize=110, weight=1)
        self.Tela_cadastro.columnconfigure(1, minsize=100, weight=1)
        self.Tela_cadastro.columnconfigure(2, minsize=8, weight=1)

        self.Tela_cadastro.grid(row=0, column=0, sticky="nsew")
        
        self.caronas = tk.Label(self.Tela_cadastro)
        self.caronas.grid(row=0, column=0, columnspan=3, sticky="nsew")
        self.caronas.configure(text= "Caronas",font='Bodoni 25', bg='#E10022', fg='White')
        
        self.Logo = tk.Label(self.Tela_cadastro)   
        self.Logo.grid(row=1, column=0, columnspan=3, sticky="nsew")
        self.Logo.configure(text= "Insper",font='Bodoni 25', bg='#E10022', fg='White')

        
##########################################################################        
#Entrada de dados cadastro
##########################################################################

        #Nome Completo
        self.nome_entrada = tk.Entry(self.Tela_cadastro)
        self.nome_entrada.grid(row=2, column=1, sticky="ew")
        
        self.nome_label = tk.Label(self.Tela_cadastro)
        self.nome_label.grid(row=2, column=0, sticky="nsew")
        self.nome_label.configure(text= "Nome completo: ",font='Bodoni 12', bg='#E10022', fg='White')

        #E-mail
        self.email_entrada = tk.Entry(self.Tela_cadastro)
        self.email_entrada.grid(row=3, column=1, sticky="ew")
        
        self.email_label = tk.Label(self.Tela_cadastro)
        self.email_label.grid(row=3, column=0, sticky="nsew")
        self.email_label.configure(text= "E-mail: ",font='Bodoni 12', bg='#E10022', fg='White')

        #Número de Celular
        numero = tk.StringVar()
        numero.set('() 9')
        self.celular_entrada = tk.Entry(self.Tela_cadastro, textvariable = numero)
        self.celular_entrada.grid(row=4, column=1, sticky="ew")
        
        self.celular_label = tk.Label(self.Tela_cadastro)
        self.celular_label.grid(row=4, column=0, sticky="nsew")
        self.celular_label.configure(text= "Número de Celular*: ",font='Bodoni 12', bg='#E10022', fg='White')


        #Usuário
        self.usuario_entrada = tk.Entry(self.Tela_cadastro)
        self.usuario_entrada.grid(row=5, column=1, sticky="ew")
        
        self.usuario_label = tk.Label(self.Tela_cadastro)
        self.usuario_label.grid(row=5, column=0, sticky="nsew")
        self.usuario_label.configure(text= "Usuário: ",font='Bodoni 12', bg='#E10022', fg='White')

        #Senha
        self.senha_entrada = tk.Entry(self.Tela_cadastro)
        self.senha_entrada.grid(row=6, column=1, sticky="ew")
        self.senha_entrada.configure(show='*')
        
        self.senha_label = tk.Label(self.Tela_cadastro)
        self.senha_label.grid(row=6, column=0, sticky="nsew")
        self.senha_label.configure(text= "Senha: ",font='Bodoni 12', bg='#E10022', fg='White')

        #Confirmar Senha
        self.senha_confirma_entrada = tk.Entry(self.Tela_cadastro)
        self.senha_confirma_entrada.grid(row=7, column=1, sticky="ew")
        self.senha_confirma_entrada.configure(show='*')
        
        self.senha_confirma_label = tk.Label(self.Tela_cadastro)
        self.senha_confirma_label.grid(row=7, column=0, sticky="nsew")
        self.senha_confirma_label.configure(text= "Confirmar senha: ",font='Bodoni 12', bg='#E10022', fg='White')

        #Nota sobre o celular
        self.nota_label = tk.Label(self.Tela_cadastro)
        self.nota_label.grid(row=8, column=1, sticky="nsew")
        self.nota_label.configure(text= "*Mais importante do cadastro, digite apenas 9xxxx-xxxx",font='Bodoni 12', bg='#E10022', fg='White')

##########################################################################        
#Fim da entrada de dados do cadastro
##########################################################################
        
        self.salvar_novo_cadastro = tk.Button(self.Tela_cadastro)
        self.salvar_novo_cadastro.grid(row=8, column=2)
        self.salvar_novo_cadastro.configure(text='salvar')
        self.salvar_novo_cadastro.bind('<1>',self.clicou_salvar)
        
        self.voltar_tela_inicial = tk.Button(self.Tela_cadastro)
        self.voltar_tela_inicial.grid(row=8, column=0)
        self.voltar_tela_inicial.configure(text='Voltar')
        self.voltar_tela_inicial.bind('<1>',self.clicou_voltar_tela_inicial)

######

    def tela_criadores(self):
        
        self.Tela_cadastro = tk.Frame(self.root)
        self.Tela_cadastro.configure(bg='#E10022')
        
        self.Tela_cadastro.rowconfigure(0, minsize=40, weight=1)
        self.Tela_cadastro.rowconfigure(1, minsize=40, weight=1)
        self.Tela_cadastro.rowconfigure(2, minsize=40, weight=1)
        self.Tela_cadastro.rowconfigure(3, minsize=40, weight=1)
        self.Tela_cadastro.rowconfigure(4, minsize=40, weight=1)
        self.Tela_cadastro.rowconfigure(5, minsize=40, weight=1)
        self.Tela_cadastro.rowconfigure(6, minsize=40, weight=1)
        self.Tela_cadastro.rowconfigure(7, minsize=40, weight=1)
        self.Tela_cadastro.rowconfigure(8, minsize=40, weight=1)
        self.Tela_cadastro.rowconfigure(9, minsize=40, weight=1)

        self.Tela_cadastro.columnconfigure(0, minsize=110, weight=1)
        self.Tela_cadastro.columnconfigure(1, minsize=100, weight=1)
        self.Tela_cadastro.columnconfigure(2, minsize=8, weight=1)

        self.Tela_cadastro.grid(row=0, column=0, sticky="nsew")
        
        self.projeto = tk.Label(self.Tela_cadastro)
        self.projeto.grid(row=0, column=0, columnspan=3, sticky="nsew")
        self.projeto.configure(text= "O Projeto",font='Bodoni 25', bg='#E10022', fg='White')
        
        self.descricao = tk.Label(self.Tela_cadastro)
        self.descricao.grid(row=1, column=0, columnspan=3, sticky="nsew")
        self.descricao.configure(text= "Descrição do projeto aqui........",font='Bodoni 10', bg='#E10022', fg='White')
        
        self.quemsomos = tk.Label(self.Tela_cadastro)
        self.quemsomos.grid(row=2, column=0, columnspan=3, sticky="nsew")
        self.quemsomos.configure(text= "Quem Somos?",font='Bodoni 25', bg='#E10022', fg='White')
        
        self.deco = tk.Label(self.Tela_cadastro)
        self.deco.grid(row=3, column=0, sticky="nsw")
        self.deco.configure(text= "André Ejzenmesser",font='Bodoni 25', bg='#E10022', fg='White')
        
        self.borba = tk.Label(self.Tela_cadastro)
        self.borba.grid(row=5, column=0, sticky="nsw")
        self.borba.configure(text= "Filipe Borba",font='Bodoni 25', bg='#E10022', fg='White')

        self.noto = tk.Label(self.Tela_cadastro)
        self.noto.grid(row=7, column=0, sticky="nsw")
        self.noto.configure(text= "Luca Noto",font='Bodoni 25', bg='#E10022', fg='White')
        
        self.sair = tk.Button(self.Tela_cadastro)
        self.sair.grid(row=9, column=2)
        self.sair.configure(text="Sair")
        self.sair.bind('<1>',self.clicou_voltar_tela_inicial)

  
###############################

      
    def tela_contato(self):
        
        self.Tela_cadastro = tk.Frame(self.root)
        self.Tela_cadastro.configure(bg='#E10022')
        
        self.Tela_cadastro.rowconfigure(0, minsize=40, weight=1)
        self.Tela_cadastro.rowconfigure(1, minsize=40, weight=1)
        self.Tela_cadastro.rowconfigure(2, minsize=40, weight=1)
        self.Tela_cadastro.rowconfigure(3, minsize=40, weight=1)
        self.Tela_cadastro.rowconfigure(4, minsize=40, weight=1)
        self.Tela_cadastro.rowconfigure(5, minsize=40, weight=1)
        self.Tela_cadastro.rowconfigure(6, minsize=40, weight=1)
        self.Tela_cadastro.rowconfigure(7, minsize=40, weight=1)
        self.Tela_cadastro.rowconfigure(8, minsize=40, weight=1)
        self.Tela_cadastro.rowconfigure(9, minsize=40, weight=1)

        self.Tela_cadastro.columnconfigure(0, minsize=110, weight=1)
        self.Tela_cadastro.columnconfigure(1, minsize=100, weight=1)
        self.Tela_cadastro.columnconfigure(2, minsize=8, weight=1)

        self.Tela_cadastro.grid(row=0, column=0, sticky="nsew")
        
        
               
#########
               
    def tela_principal_frame(self):
        
        self.Tela_principal = tk.Frame(self.root)
        self.Tela_principal.configure(bg='#E10022')
        
        self.Tela_principal.rowconfigure(0, minsize=50, weight=1)
        self.Tela_principal.rowconfigure(1, minsize=50, weight=1)
        self.Tela_principal.rowconfigure(2, minsize=25, weight=1)
        self.Tela_principal.rowconfigure(3, minsize=35, weight=1)
        self.Tela_principal.rowconfigure(4, minsize=35, weight=1)
        self.Tela_principal.rowconfigure(5, minsize=25, weight=1)
        self.Tela_principal.rowconfigure(6, minsize=15, weight=1)

        self.Tela_principal.columnconfigure(0, minsize=10, weight=1)
        self.Tela_principal.columnconfigure(1, minsize=100, weight=1)
        self.Tela_principal.columnconfigure(2, minsize=100, weight=1)
        self.Tela_principal.columnconfigure(3, minsize=100, weight=1)

        self.Tela_principal.grid(row=0, column=0, sticky="nsew")
            
        
        self.caronas = tk.Label(self.Tela_principal)
        self.caronas.grid(row=0, column=1,columnspan=3, sticky="nsew")
        self.caronas.configure(text= "Caronas",font='Bodoni 75', bg='#E10022', fg='White')
        
        self.Logo = tk.Label(self.Tela_principal)
        self.Logo.grid(row=1, column=1,columnspan=3, sticky="nsew")
        self.Logo.configure(text= "Insper",font='Bodoni 75', bg='#E10022', fg='White')
        
        
        self.label = tk.Label(self.Tela_principal)
        self.label.grid(row=2, column=2,columnspan=1, sticky="nsew")
        self.label.configure(text= "O que deseja fazer? ",font='Bodoni 12', bg='#E10022', fg='White')
        
        self.pedir_carona = tk.Button(self.Tela_principal)
        self.pedir_carona.grid(row=3, column=1,columnspan=1)
        self.pedir_carona.configure(text= "Pedir Carona ")
        self.pedir_carona.bind('<1>',self.clicou_pedir)
        
        self.oferecer_carona = tk.Button(self.Tela_principal)
        self.oferecer_carona.grid(row=3, column=2,columnspan=1)
        self.oferecer_carona.configure(text= "Oferecer Carona ")
        self.oferecer_carona.bind('<1>',self.clicou_oferecer)
        
        self.alterar_perfil = tk.Button(self.Tela_principal)
        self.alterar_perfil.grid(row=4, column=1,columnspan=1)
        self.alterar_perfil.configure(text= "Alterar meu Perfil ")
        self.alterar_perfil.bind('<1>',self.clicou_alterar)
                
        self.cancelar_pedido_carona = tk.Button(self.Tela_principal)
        self.cancelar_pedido_carona.grid(row=3, column=3)
        self.cancelar_pedido_carona.configure(text='Cancelar Pedido')
        self.cancelar_pedido_carona.bind('<1>',self.cancelar_pedido)

        self.cancelar_oferta_carona = tk.Button(self.Tela_principal)
        self.cancelar_oferta_carona.grid(row=4, column=3)
        self.cancelar_oferta_carona.configure(text='Cancelar Oferta')
        self.cancelar_oferta_carona.bind('<1>',self.cancelar_oferta)



        #Botão que leva o usuário a página anterior
        self.voltar_pagina_principal = tk.Button(self.Tela_principal)
        self.voltar_pagina_principal.configure(text='Log Out')
        self.voltar_pagina_principal.grid(row=5, column=1,columnspan=1)
        self.voltar_pagina_principal.bind('<1>',self.clicou_voltar_tela_inicial)


    def Tela_pedir_carona_frame(self):
        
        self.Tela_pedir_carona = tk.Frame(self.root)
        self.Tela_pedir_carona.configure(bg='#E10022')
        
        self.Tela_pedir_carona.rowconfigure(0, minsize=25, weight=1)
        self.Tela_pedir_carona.rowconfigure(1, minsize=25, weight=1)
        self.Tela_pedir_carona.rowconfigure(2, minsize=50, weight=1)
        self.Tela_pedir_carona.rowconfigure(3, minsize=50, weight=1)
        self.Tela_pedir_carona.rowconfigure(4, minsize=50, weight=1)
        self.Tela_pedir_carona.rowconfigure(5, minsize=50, weight=1)
        self.Tela_pedir_carona.rowconfigure(6, minsize=50, weight=1)
        self.Tela_pedir_carona.rowconfigure(7, minsize=50, weight=1)
        self.Tela_pedir_carona.rowconfigure(8, minsize=25, weight=1)
        self.Tela_pedir_carona.rowconfigure(9, minsize=25, weight=1)

        self.Tela_pedir_carona.columnconfigure(0, minsize=10, weight=1)
        self.Tela_pedir_carona.columnconfigure(1, minsize=100, weight=1)
        self.Tela_pedir_carona.columnconfigure(2, minsize=100, weight=1)
        self.Tela_pedir_carona.columnconfigure(3, minsize=100, weight=1)
        self.Tela_pedir_carona.columnconfigure(4, minsize=10, weight=1)
        
        
        self.Tela_pedir_carona.grid(row=0, column=0, sticky="nsew")
        
        
        self.caronas = tk.Label(self.Tela_pedir_carona)
        self.caronas.grid(row=1, column=1,columnspan=3, sticky="nsew")
        self.caronas.configure(text= "Pedir",font='Bodoni 50', bg='#E10022', fg='White')
        
        self.Logo = tk.Label(self.Tela_pedir_carona)
        self.Logo.grid(row=2, column=1,columnspan=3, sticky="nsew")
        self.Logo.configure(text= "Caronas",font='Bodoni 50', bg='#E10022', fg='White')
        
        self.lugares_pedido = tk.StringVar()
        self.lugares_pedido.set(self.lugares[0])
        self.Lugares = ttk.OptionMenu(self.Tela_pedir_carona,self.lugares_pedido,*self.lugares)
        self.Lugares.grid(row=6, column=2, sticky="ew")
        
        self.label_lugares = tk.Label(self.Tela_pedir_carona)
        self.label_lugares.grid(row=6, column=1,columnspan=1, sticky="nsew")
        self.label_lugares.configure(text= "Lugares Necessários: ",font='Bodoni 12', bg='#E10022', fg='White')
        
        self.hora_pedido = tk.StringVar()
        self.hora_pedido.set(self.horarios[0])
        self.Horários = ttk.OptionMenu(self.Tela_pedir_carona,self.hora_pedido,*self.horarios)
        self.Horários.grid(row=3, column=2, sticky="ew")
        
        self.label_horários = tk.Label(self.Tela_pedir_carona)
        self.label_horários.grid(row=3, column=1,columnspan=1, sticky="nsew")
        self.label_horários.configure(text= "Horários: ",font='Bodoni 12', bg='#E10022', fg='White')
        
        
        self.bairro_saida_pedido = tk.StringVar()
        self.bairro_saida_pedido.set(self.bairros[0])
        self.bairro_de_saida = ttk.OptionMenu(self.Tela_pedir_carona,self.bairro_saida_pedido,*self.bairros)
        self.bairro_de_saida.grid(row=4, column=2, sticky="ew")
        
        self.saida = tk.Label(self.Tela_pedir_carona)
        self.saida.grid(row=4, column=1,columnspan=1, sticky="nsew")
        self.saida.configure(text= "Local de saída: ",font='Bodoni 12', bg='#E10022', fg='White')
        
        #Espaço para o usuário escrever o destino
        self.bairro_chegada_pedido = tk.StringVar()
        self.bairro_chegada_pedido.set(self.bairros[0])
        self.bairro_de_chegada = ttk.OptionMenu(self.Tela_pedir_carona,self.bairro_chegada_pedido,*self.bairros)
        self.bairro_de_chegada.grid(row=5, column=2, sticky="ew")
        
        self.chegada = tk.Label(self.Tela_pedir_carona)
        self.chegada.grid(row=5, column=0,columnspan=2, sticky="nsew")
        self.chegada.configure(text= "Local de chegada: ",font='Bodoni 12', bg='#E10022', fg='White')
        
        #Botão que confirma a ação do usuário
        self.confirmar = tk.Button(self.Tela_pedir_carona)
        self.confirmar.configure(text='Confirmar')
        self.confirmar.grid(row=7, column=3,columnspan=1)
        self.confirmar.bind('<1>',self.clicou_confirmar_pedido)
        self.confirmar.bind('<Return>',self.clicou_confirmar_pedido)
        
        #Botão que leva o usuário a página anterior
        self.voltar_pagina_principal = tk.Button(self.Tela_pedir_carona)
        self.voltar_pagina_principal.configure(text='Voltar')
        self.voltar_pagina_principal.grid(row=7, column=1,columnspan=1)
        self.voltar_pagina_principal.bind('<1>',self.clicou_voltar)
        
    def Tela_oferecer_carona_frame(self):
        
        self.Tela_oferecer_carona = tk.Frame(self.root)
        self.Tela_oferecer_carona.configure(bg='#E10022')
        
        self.Tela_oferecer_carona.rowconfigure(0, minsize=25, weight=1)
        self.Tela_oferecer_carona.rowconfigure(1, minsize=25, weight=1)
        self.Tela_oferecer_carona.rowconfigure(2, minsize=50, weight=1)
        self.Tela_oferecer_carona.rowconfigure(3, minsize=50, weight=1)
        self.Tela_oferecer_carona.rowconfigure(4, minsize=50, weight=1)
        self.Tela_oferecer_carona.rowconfigure(5, minsize=50, weight=1)
        self.Tela_oferecer_carona.rowconfigure(6, minsize=50, weight=1)
        self.Tela_oferecer_carona.rowconfigure(7, minsize=50, weight=1)
        self.Tela_oferecer_carona.rowconfigure(8, minsize=25, weight=1)
        self.Tela_oferecer_carona.rowconfigure(9, minsize=25, weight=1)

        self.Tela_oferecer_carona.columnconfigure(0, minsize=10, weight=1)
        self.Tela_oferecer_carona.columnconfigure(1, minsize=100, weight=1)
        self.Tela_oferecer_carona.columnconfigure(2, minsize=100, weight=1)
        self.Tela_oferecer_carona.columnconfigure(3, minsize=100, weight=1)
        self.Tela_oferecer_carona.columnconfigure(4, minsize=10, weight=1)
        self.Tela_oferecer_carona.grid(row=0, column=0, sticky="nsew")
        
        
        self.caronas = tk.Label(self.Tela_oferecer_carona)
        self.caronas.grid(row=1, column=1,columnspan=3, sticky="nsew")
        self.caronas.configure(text= "Oferecer",font='Bodoni 50', bg='#E10022', fg='White')
        
        self.Logo = tk.Label(self.Tela_oferecer_carona)
        self.Logo.grid(row=2, column=1,columnspan=3, sticky="nsew")
        self.Logo.configure(text= "Caronas",font='Bodoni 50', bg='#E10022', fg='White')
        
        self.horarios_oferecer = tk.StringVar()
        self.horarios_oferecer.set(self.horarios[0])
        self.Horários = ttk.OptionMenu(self.Tela_oferecer_carona,self.horarios_oferecer,*self.horarios)
        self.Horários.grid(row=3, column=2, sticky="ew")
        
        self.label_horários = tk.Label(self.Tela_oferecer_carona)
        self.label_horários.grid(row=3, column=1,columnspan=1, sticky="nsew")
        self.label_horários.configure(text= "Horários: ",font='Bodoni 12', bg='#E10022', fg='White')
        
        self.lugares_oferecer = tk.StringVar()
        self.lugares_oferecer.set(self.lugares[0])
        self.Lugares = ttk.OptionMenu(self.Tela_oferecer_carona,self.lugares_oferecer,*self.lugares)
        self.Lugares.grid(row=6, column=2, sticky="ew")
        
        self.label_lugares = tk.Label(self.Tela_oferecer_carona)
        self.label_lugares.grid(row=6, column=1,columnspan=1, sticky="nsew")
        self.label_lugares.configure(text= "Lugares Disponíveis: ",font='Bodoni 12', bg='#E10022', fg='White')
        
        #Espaço para o usuário escrever a saída
        self.bairro_saida_oferta = tk.StringVar()
        self.bairro_saida_oferta.set(self.bairros[0])
        self.bairro_de_saida = ttk.OptionMenu(self.Tela_oferecer_carona,self.bairro_saida_oferta,*self.bairros)
        self.bairro_de_saida.grid(row=4, column=2, sticky="ew")
        
        self.saida = tk.Label(self.Tela_oferecer_carona)
        self.saida.grid(row=4, column=1,columnspan=1, sticky="nsew")
        self.saida.configure(text= "Local de saída: ",font='Bodoni 12', bg='#E10022', fg='White')
        
        #Espaço para o usuário escrever o destino
        self.bairro_chegada_oferta = tk.StringVar()
        self.bairro_chegada_oferta.set(self.bairros[0])
        self.bairro_de_chegada = ttk.OptionMenu(self.Tela_oferecer_carona,self.bairro_chegada_oferta,*self.bairros)
        self.bairro_de_chegada.grid(row=5, column=2, sticky="ew")
        
        self.chegada = tk.Label(self.Tela_oferecer_carona)
        self.chegada.grid(row=5, column=0,columnspan=2, sticky="nsew")
        self.chegada.configure(text= "Local de chegada: ",font='Bodoni 12', bg='#E10022', fg='White')
        
        #Botão que confirma a ação do usuário
        self.confirmar = tk.Button(self.Tela_oferecer_carona)
        self.confirmar.configure(text='Confirmar')
        self.confirmar.grid(row=7, column=3,columnspan=1)
        self.confirmar.bind('<1>',self.clicou_confirmar_oferta)
        self.confirmar.bind('<Return>',self.clicou_confirmar_oferta)
        
        #Botão que leva o usuário a página anterior
        self.voltar_pagina_principal = tk.Button(self.Tela_oferecer_carona)
        self.voltar_pagina_principal.configure(text='Voltar')
        self.voltar_pagina_principal.grid(row=7, column=1,columnspan=1)
        self.voltar_pagina_principal.bind('<1>',self.clicou_voltar)
        
        
    def Tela_ler_perfil_label(self):
        self.tela_ler_perfil = tk.Frame(self.root)
        self.tela_ler_perfil.configure(bg='#E10022')
        
        self.tela_ler_perfil.rowconfigure(0, minsize=40, weight=1)
        self.tela_ler_perfil.rowconfigure(1, minsize=40, weight=1)
        self.tela_ler_perfil.rowconfigure(2, minsize=40, weight=1)
        self.tela_ler_perfil.rowconfigure(3, minsize=40, weight=1)
        self.tela_ler_perfil.rowconfigure(4, minsize=40, weight=1)
        self.tela_ler_perfil.rowconfigure(5, minsize=40, weight=1)
        self.tela_ler_perfil.rowconfigure(6, minsize=40, weight=1)
        self.tela_ler_perfil.rowconfigure(7, minsize=40, weight=1)
        self.tela_ler_perfil.rowconfigure(8, minsize=40, weight=1)
        self.tela_ler_perfil.rowconfigure(9, minsize=40, weight=1)

        self.tela_ler_perfil.columnconfigure(0, minsize=110, weight=1)
        self.tela_ler_perfil.columnconfigure(1, minsize=100, weight=1)
        self.tela_ler_perfil.columnconfigure(2, minsize=8, weight=1)

        
        self.tela_ler_perfil.grid(row=0, column=0, sticky="nsew")
        
        dados = firebase.FirebaseApplication('https://caronas.firebaseio.com/Users/')
        

#######################################################

        #Nome Completo

        nome = tk.StringVar()
        nome.set(dados.get(self.usuarios, 'Nome'))
        self.nome_entrada = tk.Entry(self.tela_ler_perfil, textvariable = nome)
        self.nome_entrada.grid(row=2, column=1, sticky="ew")
        
        self.nome_label = tk.Label(self.tela_ler_perfil)
        self.nome_label.grid(row=2, column=0, sticky="nsew")
        self.nome_label.configure(text= "Nome completo: ",font='Bodoni 12', bg='#E10022', fg='White')

        #E-mail
        email = tk.StringVar()
        email.set (dados.get(self.usuarios, 'email'))
        self.email_entrada = tk.Entry(self.tela_ler_perfil, textvariable = email)
        self.email_entrada.grid(row=3, column=1, sticky="ew")
        
        self.email_label = tk.Label(self.tela_ler_perfil)
        self.email_label.grid(row=3, column=0, sticky="nsew")
        self.email_label.configure(text= "E-mail: ",font='Bodoni 12', bg='#E10022', fg='White')

        #Número de Celular
        numero = tk.StringVar()
        numero.set (dados.get(self.usuarios, 'telefone'))
        self.celular_entrada = tk.Entry(self.tela_ler_perfil, textvariable = numero)
        self.celular_entrada.grid(row=4, column=1, sticky="ew")
        
        self.celular_label = tk.Label(self.tela_ler_perfil)
        self.celular_label.grid(row=4, column=0, sticky="nsew")
        self.celular_label.configure(text= "Número de Celular*: ",font='Bodoni 12', bg='#E10022', fg='White')


        #Usuário
        user = tk.StringVar()
        user.set (self.usuarios)
        self.usuario_entrada = tk.Entry(self.tela_ler_perfil, textvariable =user)
        self.usuario_entrada.configure(state = "disabled")
        self.usuario_entrada.grid(row=5, column=1, sticky="ew")
        
        self.usuario_label = tk.Label(self.tela_ler_perfil)
        self.usuario_label.grid(row=5, column=0, sticky="nsew")
        self.usuario_label.configure(text= "Usuário: ",font='Bodoni 12', bg='#E10022', fg='White')

        #Senha
        senha = tk.StringVar()
        senha.set (dados.get(self.usuarios, 'senha'))
        self.senha_entrada = tk.Entry(self.tela_ler_perfil, textvariable = senha)
        self.senha_entrada.grid(row=6, column=1, sticky="ew")
        self.senha_entrada.configure(show='*')
        
        self.senha_label = tk.Label(self.tela_ler_perfil)
        self.senha_label.grid(row=6, column=0, sticky="nsew")
        self.senha_label.configure(text= "Senha: ",font='Bodoni 12', bg='#E10022', fg='White')

        #Confirmar Senha
        senha = tk.StringVar()
        senha.set (dados.get(self.usuarios, 'senha'))
        self.senha_confirma_entrada = tk.Entry(self.tela_ler_perfil, textvariable = senha)
        self.senha_confirma_entrada.grid(row=7, column=1, sticky="ew")
        self.senha_confirma_entrada.configure(show='*')
        
        self.senha_confirma_label = tk.Label(self.tela_ler_perfil)
        self.senha_confirma_label.grid(row=7, column=0, sticky="nsew")
        self.senha_confirma_label.configure(text= "Confirmar senha: ",font='Bodoni 12', bg='#E10022', fg='White')

        #Nota sobre o celular
        self.nota_label = tk.Label(self.tela_ler_perfil)
        self.nota_label.grid(row=8, column=1, sticky="nsew")
        self.nota_label.configure(text= "*Mais importante do cadastro, digite apenas 9xxxx-xxxx",font='Bodoni 12', bg='#E10022', fg='White')

#######################################################
        
        self.salvar_cadastro = tk.Button(self.tela_ler_perfil)
        self.salvar_cadastro.grid(row=8, column=2)
        self.salvar_cadastro.configure(text='salvar')
        self.salvar_cadastro.bind('<1>',self.clicou_salvar_alteracoes)
        
        self.voltar_tela_inicial = tk.Button(self.tela_ler_perfil)
        self.voltar_tela_inicial.grid(row=8, column=0)
        self.voltar_tela_inicial.configure(text='Voltar')
        self.voltar_tela_inicial.bind('<1>',self.clicou_voltar)
                
                
####################     Função dos botões

    def clicou_cadastro(self,event):
        self.Tela_cadastro_frame() 
        
    def clicou_login(self,event):
        self.Tela_login_frame()

    def clicou_continuar_tela_principal(self,event):
        self.usuarios = self.entrada_usuario.get()
        
        fb = firebase.FirebaseApplication('https://caronas.firebaseio.com')
        pessoas = fb.get('/Users', None)
        
        if self.usuarios in pessoas:
            
            fb2 = firebase.FirebaseApplication('https://caronas.firebaseio.com/Users/')
            self.senha_pra_conferir = fb2.get(self.usuarios, 'senha')
            
            if self.senha_pra_conferir == self.entrada_senha.get():
                self.nome_completo = fb2.get(self.usuarios, 'Nome')
                self.telefone = fb2.get(self.usuarios, 'telefone')
                self.email = fb2.get(self.usuarios, 'email')
                self.tela_principal_frame()       
            else:
               tkm.showinfo('Erro','Senha inválida')
            
        else:
            tkm.showinfo('Erro','Usuário Inexistente')       
        
    def clicou_voltar_tela_inicial(self,event):
        self.tela_inicial_frame()  

    #Salvar informações do cadastro    
    def clicou_salvar(self,event):
        fb = firebase.FirebaseApplication('https://caronas.firebaseio.com', None)
        cadastros = fb.get('Users', None)
        
        if not self.usuario_entrada.get() in cadastros:
            if self.senha_entrada.get() == self.senha_confirma_entrada.get() and self.nome_entrada.get() != '' and self.email_entrada.get() != '' and self.celular_entrada.get() != '' and self.celular_entrada.get() != '() 9' and self.usuario_entrada.get() != '':
                
                confirmando_cadastro = tkm.askyesno('Confirmando','Deseja salvar as informações?')
                
                if confirmando_cadastro:
                    
                    fb = firebase.FirebaseApplication('https://caronas.firebaseio.com')
                    dicionario = {'Nome': self.nome_entrada.get(),'email': self.email_entrada.get(), 'telefone': self.celular_entrada.get(), 'senha': self.senha_entrada.get()}
                    fb.put('Users', self.usuario_entrada.get(), dicionario)
                    self.Tela_login_frame()
                                        
            else:
                tkm.showinfo('Erro','Campos incompletos ou senhas não combinadas!')
        else:
            tkm.showinfo('Erro','Usuário já existente!')
        
    def clicou_pedir(self,event):
        self.Tela_pedir_carona_frame()
                
    def clicou_voltar(self,event):
        self.tela_principal_frame()
        
    def clicou_confirmar_pedido(self,event):
        confirmando_pedido = tkm.askyesno('Confirmando','Deseja confirmar pedido?')
            
        if confirmando_pedido:
            fb = firebase.FirebaseApplication('https://caronas.firebaseio.com', None)
            dicionario = {'Horário': self.hora_pedido.get(),'Local de Saída': self.bairro_saida_pedido.get(), 'Local de Chegada': self.bairro_chegada_pedido.get(), 'Lugares Necessários': self.lugares_pedido.get()}
            fb.put('/Pedidos', self.usuarios, dicionario)
            
            ofertas = fb.get('Ofertas', None)
            
            fb2 = firebase.FirebaseApplication('https://caronas.firebaseio.com/Pedidos/')
            fb3 = firebase.FirebaseApplication('https://caronas.firebaseio.com/Ofertas/')
            fb4 = firebase.FirebaseApplication('https://caronas.firebaseio.com/Users/')

            lugar_saida_pedido = fb2.get(self.usuarios, 'Local de Saída')
            lugar_chegada_pedido = fb2.get(self.usuarios, 'Local de Chegada')
            horario_pedido = fb2.get(self.usuarios, 'Horário')
            lugares_necessarios_pedido = fb2.get(self.usuarios, 'Lugares Necessários')
            
            for motorista in ofertas:
                lugar_saida_oferta = fb3.get(motorista, 'Local de Saída')
                lugar_chegada_oferta = fb3.get(motorista, 'Local de Chegada')
                horario_oferta = fb3.get(motorista, 'Horário')
                lugares_necessarios_oferta = fb3.get(motorista, 'Lugares Necessários')
                
                if lugar_saida_pedido == lugar_saida_oferta and lugar_chegada_pedido == lugar_chegada_oferta and lugares_necessarios_pedido <= lugares_necessarios_oferta and horario_pedido == horario_oferta:
                    nome = fb4.get(motorista,'Nome')
                    celular = fb4.get(motorista, 'telefone')
                    email = fb4.get(motorista, 'email')
                                        
                    fromaddr = 'lucarn@al.insper.edu.br'
                    toaddrs = self.email
    
                    msg = 'Seu carona é: {0}\nSeu telefone é: {1}\nSeu email é: {2}\n\nEntre em contato com seu carona para combinarem melhor!\nObrigado por escolher o Caronas Insper!\nA equipe agradece!!'.format(nome, celular, email).encode('UTF-8')
                    
                    server = smtplib.SMTP('insper.edu.br')
                    server.set_debuglevel(1)
                    server.sendmail(fromaddr, toaddrs, msg)
                    server.quit()
                    
                    fromaddr = 'lucarn@al.insper.edu.br'
                    toaddrs = email
    
                    msg = 'Seu carona é: {0}\nSeu telefone é: {1}\nSeu email é: {2}\n\nEntre em contato com seu carona para marcarem melhor!\nObrigado por escolher o Caronas Insper!\nA equipe agradece!!'.format(self.nome_completo, self.telefone, self.email).encode('UTF-8')
                    
                    server = smtplib.SMTP('insper.edu.br')
                    server.set_debuglevel(1)
                    server.sendmail(fromaddr, toaddrs, msg)
                    server.quit()
                    
                    fb.delete('/Pedidos', self.usuarios)
                    fb.delete('/Ofertas', motorista)
                    
                    tkm.showinfo('Carona','As informações de seu carona estão no seu email!')
                    break
            else:
                tkm.showinfo('Carona', 'Não existem caronas no momento. Quando exister alguém, você será notificado por email!')
                                
            self.tela_principal_frame()

    def clicou_confirmar_oferta(self,event):
        confirmando_oferta = tkm.askyesno('Confirmando','Deseja confirmar oferta?')
            
        if confirmando_oferta:
            fb = firebase.FirebaseApplication('https://caronas.firebaseio.com', None)
            dicionario = {'Horário': self.horarios_oferecer.get(),'Local de Saída': self.bairro_saida_oferta.get(), 'Local de Chegada': self.bairro_chegada_oferta.get(), 'Lugares Necessários': self.lugares_oferecer.get()}
            fb.put('/Ofertas', self.usuarios, dicionario)

            pedidos = fb.get('Pedidos', None)
            
            fb2 = firebase.FirebaseApplication('https://caronas.firebaseio.com/Pedidos/')
            fb3 = firebase.FirebaseApplication('https://caronas.firebaseio.com/Ofertas/')
            fb4 = firebase.FirebaseApplication('https://caronas.firebaseio.com/Users/')


            lugar_saida_oferta = fb3.get(self.usuarios, 'Local de Saída')
            lugar_chegada_oferta = fb3.get(self.usuarios, 'Local de Chegada')
            horario_oferta = fb3.get(self.usuarios, 'Horário')
            lugares_necessarios_oferta = fb3.get(self.usuarios, 'Lugares Necessários')
            
            for passageiro in pedidos:
                lugar_saida_pedido = fb2.get(passageiro, 'Local de Saída')
                lugar_chegada_pedido = fb2.get(passageiro, 'Local de Chegada')
                horario_pedido = fb2.get(passageiro, 'Horário')
                lugares_necessarios_pedido = fb2.get(passageiro, 'Lugares Necessários')

                if lugar_saida_oferta == lugar_saida_pedido and lugar_chegada_oferta == lugar_chegada_pedido and lugares_necessarios_oferta >= lugares_necessarios_pedido and horario_oferta == horario_pedido:                    
                    nome = fb4.get(passageiro,'Nome')
                    celular = fb4.get(passageiro, 'telefone')
                    email = fb4.get(passageiro, 'email')
                                        
                    fromaddr = 'lucarn@al.insper.edu.br'
                    toaddrs = self.email

                    msg = 'O seu carona é: {0}\nSeu telefone é: {1}\nSeu email é: {2}\n\nEntre em contato com seu carona para marcarem melhor!\nObrigado por escolher o Caronas Insper!\nA equipe agradece!!'.format(nome, celular, email).encode('UTF-8')
                    
                    server = smtplib.SMTP('insper.edu.br')
                    server.set_debuglevel(1)
                    server.sendmail(fromaddr, toaddrs, msg)
                    server.quit()
                    
                    fromaddr = 'lucarn@al.insper.edu.br'
                    toaddrs = email

                    msg = 'Seu carona é: {0}\nSeu telefone é: {1}\nSeu email é: {2}\n\nEntre em contato com seu carona para combinarem melhor!\nObrigado por escolher o Caronas Insper!\nA equipe agradece!!'.format(self.nome_completo, self.telefone, self.email).encode('UTF-8')
                    
                    server = smtplib.SMTP('insper.edu.br')
                    server.set_debuglevel(1)
                    server.sendmail(fromaddr, toaddrs, msg)
                    server.quit()
                    
                    fb.delete('/Pedidos', passageiro)
                    fb.delete('/Ofertas', self.usuarios)
                    
                    tkm.showinfo('Carona', 'As informações de seu carona estão no seu email!')
                    break
            else:
                tkm.showinfo('Carona', 'Não existem caronas no momento. Quando exister alguém, você será notificado por email!')
        
            self.tela_principal_frame()

    #Função que leva para a tela de oferecer carona
    def clicou_oferecer(self,event):
        self.Tela_oferecer_carona_frame()

    #Função que leva a tela de alterar perfil
    def clicou_alterar(self,event):
        self.Tela_ler_perfil_label()
    
    #Função que faz log out
    def clicou_voltar_login(self,event):
        self.Tela_login_frame()
                                
    #Função que cancela as caronas pedidas
    def cancelar_pedido(self,event):
        fb = firebase.FirebaseApplication('https://caronas.firebaseio.com')
        pedidos = fb.get('/Pedidos', None)
        
        if self.usuarios in pedidos:
            cancelamento = tkm.askyesno('Cancelamento','Deseja cancelar seu pedido?')
            if cancelamento:
                fb.delete('Pedidos', self.usuarios)
                tkm.showinfo('Cancelamento','Pedido cancelado com sucesso!')
       
        else:
            tkm.showinfo('Cancelamento', 'Não existe um pedido de carona')

    #Função que cancela a oferta de carona
    def cancelar_oferta(self,event):
        fb = firebase.FirebaseApplication('https://caronas.firebaseio.com')
        ofertas = fb.get('/Ofertas', None)
        
        if self.usuarios in ofertas:
            cancelamento = tkm.askyesno('Cancelamento','Deseja cancelar sua oferta?')
            if cancelamento:
                fb.delete('Ofertas', self.usuarios)
                tkm.showinfo('Cancelamento','Oferta cancelada com sucesso!')   
        else:
            tkm.showinfo('Cancelamento', 'Não existe oferta de carona')
            
    def clicou_salvar_alteracoes(self,event):
        if self.senha_entrada.get() == self.senha_confirma_entrada.get(): 
            
            confirmando_cadastro = tkm.askyesno('Confirmando','Deseja confirmar as informações?')
            
            if confirmando_cadastro:
                
                fb = firebase.FirebaseApplication('https://caronas.firebaseio.com')
                dicionario = {'Nome': self.nome_entrada.get(),'email': self.email_entrada.get(), 'telefone': self.celular_entrada.get(), 'senha': self.senha_entrada.get()}
                fb.put('Users', self.usuario_entrada.get(), dicionario)
                
                fb2 = firebase.FirebaseApplication('https://caronas.firebaseio.com/Users/')
                self.nome_completo = fb2.get(self.usuarios, 'Nome')
                self.telefone = fb2.get(self.usuarios, 'telefone')
                self.email = fb2.get(self.usuarios, 'email')
                
                self.tela_principal_frame()
                                    
        else:
            tkm.showinfo('Erro','Senhas não combinadas!')
        
    def clicou_sobre_nós(self,event):
        self.tela_criadores()
        
    def clicou_contato(self,event):
        self.tela_contato()


########## iniciando o programa
    def iniciar(self):
        self.root.mainloop()

Caronas = Telas()
Caronas.iniciar()