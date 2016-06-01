import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as tkm
from firebase import firebase
import smtplib
from validate_email import validate_email
import tkinter.scrolledtext as tkst

class Telas():
    
    def __init__(self):
        #Listas com bairros disponiveis para carona, horários de saída e lugares disponiveis no carro
        self.bairros = sorted(['','Cerqueira César','Vila Leopoldina','Vila Olímpia','Higienópolis','Morumbi','Jardins','Itaim','Jardim Paulista','Moema','Osasco','Itaquera','Alphaville','Pinheiros', 'Alto de Pinheiros', 'Jardim Paulistano', 'Jardim Europa', 'Paraíso','Perdizes','Campo Belo','Consolação','Aclimação','Chácara Inglesa','Chácara Klabin','Butantã'])
        self.horarios = ['','6h00','6h30','7h00','7h30','8h00','8h30','9h00','9h30','10h00','10h30','11h00','11h30','12h00','12h30','13h00','13h30','14h00','14h30','15h00','16h00','16h30','17h00','17h30','18h00','18h30','19h00','19h30','20h00','20h30','21h00','21h30','22h00','22h30','23h00']
        self.lugares = ['','1','2','3','4']
        self.dia_lista = ['','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
        self.mes_lista = ['','1','2','3','4','5','6','7','8','9','10','11','12']
        
        #Gerando a janela
        self.root = tk.Tk()
        self.root.title("Caronas Insper")
        self.root.geometry("600x600")
        self.root.rowconfigure(0, minsize=600)
        self.root.columnconfigure(0, minsize=600)
        self.root.resizable(width=False, height=False)
        self.root.grid()
        
        self.tela_inicial_frame()
        
        
####   TELAS  #######################################################

    def tela_inicial_frame(self):
        
        #Configurações do Frame
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
        
        #Título
        caronas = tk.Label(self.tela_inicial)
        caronas.grid(row=1, column=0,columnspan=3, sticky="nsew")
        caronas.configure(text= "Caronas",font='Bodoni 75', bg='#E10022', fg='White')
        
        Logo = tk.Label(self.tela_inicial)   
        Logo.grid(row=2, column=0,columnspan=3, sticky="nsew")
        Logo.configure(text= "Insper",font='Bodoni 75', bg='#E10022', fg='White')

  #Botões
  			#Login
        self.Login = tk.Button(self.tela_inicial)
        self.Login.grid(row=4, column=1, sticky="ew")
        self.Login.configure(text="Login", font='Arial 20')
        self.Login.bind('<1>',self.clicou_login)
        
        #Cadastro
        self.Cadastro = tk.Button(self.tela_inicial)
        self.Cadastro.grid(row=5, column=1, sticky="ew")
        self.Cadastro.configure(text="Cadastrar-se", font='Arial 20')
        self.Cadastro.bind('<1>',self.clicou_cadastro)
        
        #Sobre Nós
        self.sobre_nós = tk.Button(self.tela_inicial)
        self.sobre_nós.grid(row=6, column=1, sticky="ew")
        self.sobre_nós.configure(text="Sobre", font='Arial 20')
        self.sobre_nós.bind('<1>',self.clicou_sobre_nós)
        
        #Contato
        self.contato = tk.Button(self.tela_inicial)
        self.contato.grid(row=7, column=1, sticky="ew")
        self.contato.configure(text="Contato", font='Arial 20')
        self.contato.bind('<1>',self.clicou_contato)

####################################################################    

    def Tela_login_frame(self):
      
        #Configurações do Frame
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
        
        
        #Título
        caronas = tk.Label(self.Tela_login)
        caronas.grid(row=1, column=1,columnspan=3, sticky="nsew")
        caronas.configure(text= "Caronas",font='Bodoni 75', bg='#E10022', fg='White')
        
        Logo = tk.Label(self.Tela_login)
        Logo.grid(row=2, column=1,columnspan=3, sticky="nsew")
        Logo.configure(text= "Insper",font='Bodoni 75', bg='#E10022', fg='White')
        
        #Usuário
        Usuário = tk.Label(self.Tela_login)
        Usuário.grid(row=4, column=1,columnspan=1, sticky="nsew")
        Usuário.configure(text= "Usuário: ",font='Bodoni 20', bg='#E10022', fg='White')
        
        self.entrada_usuario = tk.Entry(self.Tela_login)
        self.entrada_usuario.grid(row=4, column=2, sticky="ew")
        self.entrada_usuario.bind('<Return>',self.clicou_continuar_tela_principal)
        
        #Senha
        Senha = tk.Label(self.Tela_login)
        Senha.grid(row=5, column=1,columnspan=1, sticky="nsew")
        Senha.configure(text= "Senha: ",font='Bodoni 20', bg='#E10022', fg='White')
        
        self.entrada_senha = tk.Entry(self.Tela_login)
        self.entrada_senha.grid(row=5, column=2, sticky="ew")
        self.entrada_senha.configure(show='*')
        self.entrada_senha.bind('<Return>',self.clicou_continuar_tela_principal)
        
    #Botões
    		#Seguir
        self.continuar_tela_principal = tk.Button(self.Tela_login)
        self.continuar_tela_principal.grid(row=6, column=3,columnspan=1)
        self.continuar_tela_principal.configure(text='Seguir')
        self.continuar_tela_principal.bind('<1>',self.clicou_continuar_tela_principal)
        self.continuar_tela_principal.bind('<Return>',self.clicou_continuar_tela_principal)
        
        #Voltar
        self.voltar_tela_inicial = tk.Button(self.Tela_login)
        self.voltar_tela_inicial.grid(row=6, column=1,columnspan=1)
        self.voltar_tela_inicial.configure(text='Voltar')
        self.voltar_tela_inicial.bind('<1>',self.clicou_voltar_tela_inicial)
        self.voltar_tela_inicial.bind('<Return>',self.clicou_voltar_tela_inicial)
    
        
####################################################################    
 
    
    def Tela_cadastro_frame(self):
        
        #Configurações do Frame
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
        
        
        #Título
        self.caronas = tk.Label(self.Tela_cadastro)
        self.caronas.grid(row=0, column=0, columnspan=3, sticky="nsew")
        self.caronas.configure(text= "Caronas",font='Bodoni 25', bg='#E10022', fg='White')
        
        self.Logo = tk.Label(self.Tela_cadastro)   
        self.Logo.grid(row=1, column=0, columnspan=3, sticky="nsew")
        self.Logo.configure(text= "Insper",font='Bodoni 25', bg='#E10022', fg='White')

        
        
	#Entrada de dados cadastro
        #Nome Completo
        nome_label = tk.Label(self.Tela_cadastro)
        nome_label.grid(row=2, column=0, sticky="nsew")
        nome_label.configure(text= "Nome completo: ",font='Bodoni 12', bg='#E10022', fg='White')

        self.nome_entrada = tk.Entry(self.Tela_cadastro)
        self.nome_entrada.grid(row=2, column=1, sticky="ew")
        
      
        #E-mail
        email_label = tk.Label(self.Tela_cadastro)
        email_label.grid(row=3, column=0, sticky="nsew")
        email_label.configure(text= "E-mail: ",font='Bodoni 12', bg='#E10022', fg='White')

        self.email_entrada = tk.Entry(self.Tela_cadastro)
        self.email_entrada.grid(row=3, column=1, sticky="ew")
        
        
        #Número de Celular
        celular_label = tk.Label(self.Tela_cadastro)
        celular_label.grid(row=4, column=0, sticky="nsew")
        celular_label.configure(text= "Número de Celular*: ",font='Bodoni 12', bg='#E10022', fg='White')

        numero = tk.StringVar()
        numero.set('() 9')
        self.celular_entrada = tk.Entry(self.Tela_cadastro, textvariable = numero)
        self.celular_entrada.grid(row=4, column=1, sticky="ew")
        

        #Usuário
        usuario_label = tk.Label(self.Tela_cadastro)
        usuario_label.grid(row=5, column=0, sticky="nsew")
        usuario_label.configure(text= "Usuário: ",font='Bodoni 12', bg='#E10022', fg='White')

        self.usuario_entrada = tk.Entry(self.Tela_cadastro)
        self.usuario_entrada.grid(row=5, column=1, sticky="ew")
        
        
        #Senha
        senha_label = tk.Label(self.Tela_cadastro)
        senha_label.grid(row=6, column=0, sticky="nsew")
        senha_label.configure(text= "Senha: ",font='Bodoni 12', bg='#E10022', fg='White')

        self.senha_entrada = tk.Entry(self.Tela_cadastro)
        self.senha_entrada.grid(row=6, column=1, sticky="ew")
        self.senha_entrada.configure(show='*')
        
        
        #Confirmar Senha
        senha_confirma_label = tk.Label(self.Tela_cadastro)
        senha_confirma_label.grid(row=7, column=0, sticky="nsew")
        senha_confirma_label.configure(text= "Confirmar senha: ",font='Bodoni 12', bg='#E10022', fg='White')
        
        self.senha_confirma_entrada = tk.Entry(self.Tela_cadastro)
        self.senha_confirma_entrada.grid(row=7, column=1, sticky="ew")
        self.senha_confirma_entrada.configure(show='*')
        
        
        #Nota sobre o celular
        nota_label = tk.Label(self.Tela_cadastro)
        nota_label.grid(row=8, column=1, sticky="nsew")
        nota_label.configure(text= "*Mais importante do cadastro, digite apenas 9xxxx-xxxx",font='Bodoni 12', bg='#E10022', fg='White')

        

        
  #Botões
  	   #Salvar
        self.salvar_novo_cadastro = tk.Button(self.Tela_cadastro)
        self.salvar_novo_cadastro.grid(row=8, column=2)
        self.salvar_novo_cadastro.configure(text='salvar')
        self.salvar_novo_cadastro.bind('<1>',self.clicou_salvar)
        
        #Voltar
        self.voltar_tela_inicial = tk.Button(self.Tela_cadastro)
        self.voltar_tela_inicial.grid(row=8, column=0)
        self.voltar_tela_inicial.configure(text='Voltar')
        self.voltar_tela_inicial.bind('<1>',self.clicou_voltar_tela_inicial)

####################################################################

    def tela_criadores_frame(self):
        
        #Configurações do Frame
        self.tela_criadores = tk.Frame(self.root)
        self.tela_criadores.configure(bg='#E10022')
        
        self.tela_criadores.rowconfigure(0, minsize=40, weight=1)
        self.tela_criadores.rowconfigure(1, minsize=40, weight=1)
        self.tela_criadores.rowconfigure(2, minsize=40, weight=1)
        self.tela_criadores.rowconfigure(3, minsize=40, weight=1)
        self.tela_criadores.rowconfigure(4, minsize=40, weight=1)
        self.tela_criadores.rowconfigure(5, minsize=40, weight=1)
        self.tela_criadores.rowconfigure(6, minsize=40, weight=1)
        self.tela_criadores.rowconfigure(7, minsize=40, weight=1)
        self.tela_criadores.rowconfigure(8, minsize=40, weight=1)
        self.tela_criadores.rowconfigure(9, minsize=40, weight=1)

        self.tela_criadores.columnconfigure(0, minsize=50, weight=1)
        self.tela_criadores.columnconfigure(1, minsize=50, weight=1)
        self.tela_criadores.columnconfigure(2, minsize=50, weight=1)
        
        self.tela_criadores.grid(row=0, column=0, sticky="nsew")
        
        #Textos
        Sobre = 'Olá! Obrigado por utilizar nosso aplicativo!\n\nEste é um projeto desenvolvido para a disciplina Design de Softwares do 1º Semestre do Insper (Instituto de Ensino e Pesquisa).\n\nQuando surgiu a ideia de desenvolver este aplicativo, tinhamos como objetivo ajudar e incentivar os alunos do Insper a pegar caronas uns com os outros, diminuindo os carros nas ruas e estabelecendo novas amizades.'
        TextoBorba = ' Engenharia de Computação, apaixonado por tecnologia e jogos, membro do GAS Insper, Chief Executive Officer (CEO) e co-fundador do Caronas Insper.'       
        TextoDeco = 'Engenharia Mecatrônica, 18 anos, aluno do Insper, gosto muito de eletrônica e tecnologia. CEO e FUNDADOR do aplicativo Caronas Insper e LIDER (haha) do grupo. O único Corithiano do Grupo'         
        TextoNoto = 'Engenharia Mecânica, Palmeirense apaixonado , interessado em lógica, matemática e ciência. Membro do Diretório Acadêmico do Insper, Chief Marketing Officer (CMO) e co-fundador do Caronas Insper.  '
        
        
        #Descrição
        projeto = tk.Label(self.tela_criadores)
        projeto.grid(row=1, column=0, columnspan=3, sticky="nsew")
        projeto.configure(text= "O Projeto",font='Bodoni 25', bg='#E10022', fg='White')
        
        self.descricao = tkst.ScrolledText(self.tela_criadores, height = 4,width  = 70, wrap   = 'word')
        self.descricao.grid(row=2, column=0,columnspan=3,  sticky="ns")
        self.descricao.insert('insert', Sobre)
        self.descricao.configure(font='Bodoni 10', bg='white', fg='black', state='disabled')

    #Info Criadores    
        quemsomos = tk.Label(self.tela_criadores)
        quemsomos.grid(row=4, column=0, columnspan=3, sticky="nsew")
        quemsomos.configure(text= "Quem Somos?",font='Bodoni 25', bg='#E10022', fg='White')
        
        
        #Borba
        borba = tk.Label(self.tela_criadores)
        borba.grid(row=5, column=0, sticky="ns")
        borba.configure(text= "Filipe Borba",font='Bodoni 25', bg='#E10022', fg='White')


        self.texto_borba = tkst.ScrolledText(self.tela_criadores, height = 15,width  = 20, wrap   = 'word')
        self.texto_borba.grid(row=6, column=0,  sticky="ns")
        self.texto_borba.insert('insert', TextoBorba)
        self.texto_borba.configure(font='Bodoni 10', bg='white', fg='black', state='disabled')

        #Deco
        deco = tk.Label(self.tela_criadores)
        deco.grid(row=5, column=1, sticky="ns")
        deco.configure(text= "André Ejzenmesser",font='Bodoni 25', bg='#E10022', fg='White')
        
        self.texto_deco = tkst.ScrolledText(self.tela_criadores, height = 15,width  = 20, wrap   = 'word')
        self.texto_deco.grid(row=6, column=1,  sticky="ns")
        self.texto_deco.insert('insert', TextoDeco)
        self.texto_deco.configure(font='Bodoni 10', bg='white', fg='black', state='disabled')

        
        #Noto
        noto = tk.Label(self.tela_criadores)
        noto.grid(row=5, column=2, sticky="ns")
        noto.configure(text= "Luca Noto",font='Bodoni 25', bg='#E10022', fg='White')
        
        self.texto_noto = tkst.ScrolledText(self.tela_criadores, height = 15,width  = 20, wrap   = 'word')
        self.texto_noto.grid(row=6, column=2,  sticky="ns")
        self.texto_noto.insert('insert', TextoNoto)
        self.texto_noto.configure(font='Bodoni 10', bg='white', fg='black', state='disabled')

  
  #Botões
  	   #Sair
        self.sair = tk.Button(self.tela_criadores)
        self.sair.grid(row=9, column=2)
        self.sair.configure(text="Sair")
        self.sair.bind('<1>',self.clicou_voltar_tela_inicial)

  
####################################################################

      
    def tela_contato_frame(self):
        
        #Configurações do Frame
        self.tela_contato = tk.Frame(self.root)
        self.tela_contato.configure(bg='#E10022')
        
        self.tela_contato.rowconfigure(0, minsize=40, weight=1)
        self.tela_contato.rowconfigure(1, minsize=40, weight=1)
        self.tela_contato.rowconfigure(2, minsize=40, weight=1)
        self.tela_contato.rowconfigure(3, minsize=40, weight=1)
        self.tela_contato.rowconfigure(4, minsize=40, weight=1)
        self.tela_contato.rowconfigure(5, minsize=40, weight=1)
        self.tela_contato.rowconfigure(6, minsize=40, weight=1)
        self.tela_contato.rowconfigure(7, minsize=40, weight=1)
        self.tela_contato.rowconfigure(8, minsize=40, weight=1)
        self.tela_contato.rowconfigure(9, minsize=40, weight=1)

        self.tela_contato.columnconfigure(0, minsize=110, weight=1)
        self.tela_contato.columnconfigure(1, minsize=100, weight=1)
        self.tela_contato.columnconfigure(2, minsize=8, weight=1)

        self.tela_contato.grid(row=0, column=0, sticky="nsew")

        #Título
        label_contato = tk.Label(self.tela_contato)
        label_contato.grid(row=0, column=0, columnspan=3, sticky="nsew")
        label_contato.configure(text="Contato",font='Bodoni 40', bg='#E10022', fg='White')
        label_contato.bind('<1>',self.clicou_voltar_tela_inicial)
        
        #Email
        label_meu_email = tk.Label(self.tela_contato)
        label_meu_email.grid(row=4, column=0, sticky="nsw")
        label_meu_email.configure(text="Seu E-mail: ",font='Bodoni 25', bg='#E10022', fg='White')
        label_meu_email.bind('<1>',self.clicou_voltar_tela_inicial)
        
        self.meu_email = tk.Entry(self.tela_contato)
        self.meu_email.grid(row=4, column=1, sticky="ew")
        
        #Mensagem
        label_reclamacao = tk.Label(self.tela_contato)
        label_reclamacao.grid(row=5, column=0, sticky="nsw")
        label_reclamacao.configure(text="Sua Mensagem:",font='Bodoni 25', bg='#E10022', fg='White')
        label_reclamacao.bind('<1>',self.clicou_voltar_tela_inicial)
        
        self.reclamacao = tk.Text(self.tela_contato)
        self.reclamacao.configure(width = 40, height =10)
        self.reclamacao.grid(row=6, column=1, sticky="nsew")
        
        #Botões
        self.enviar = tk.Button(self.tela_contato)
        self.enviar.grid(row=8, column=2)
        self.enviar.configure(text="Enviar")
        self.enviar.bind('<1>',self.enviar_contato)

        self.sair = tk.Button(self.tela_contato)
        self.sair.grid(row=9, column=0)
        self.sair.configure(text="Sair")
        self.sair.bind('<1>',self.clicou_voltar_tela_inicial)

        
####################################################################
               
  
    def tela_principal_frame(self):
      
        #Configurações do Frame
        self.Tela_principal = tk.Frame(self.root)
        self.Tela_principal.configure(bg='#E10022')
        
        self.Tela_principal.rowconfigure(0, minsize=50, weight=1)
        self.Tela_principal.rowconfigure(1, minsize=50, weight=1)
        self.Tela_principal.rowconfigure(2, minsize=25, weight=1)
        self.Tela_principal.rowconfigure(3, minsize=35, weight=1)
        self.Tela_principal.rowconfigure(4, minsize=35, weight=1)
        self.Tela_principal.rowconfigure(5, minsize=25, weight=1)
        self.Tela_principal.rowconfigure(6, minsize=15, weight=1)

        self.Tela_principal.columnconfigure(0, minsize=100, weight=1)
        self.Tela_principal.columnconfigure(1, minsize=100, weight=1)
        self.Tela_principal.columnconfigure(2, minsize=100, weight=1)

        self.Tela_principal.grid(row=0, column=0, sticky="nsew")
            
        #Título
        caronas = tk.Label(self.Tela_principal)
        caronas.grid(row=0, column=0,columnspan=3, sticky="nsew")
        caronas.configure(text= "Caronas",font='Bodoni 75', bg='#E10022', fg='White')
        
        Logo = tk.Label(self.Tela_principal)
        Logo.grid(row=1, column=0,columnspan=3, sticky="nsew")
        Logo.configure(text= "Insper",font='Bodoni 75', bg='#E10022', fg='White')
        
        #Mensagem 'O que deseja fazer?'
        label = tk.Label(self.Tela_principal)
        label.grid(row=2, column=1,columnspan=1, sticky="nsew")
        label.configure(text= "O que deseja fazer? ",font='Bodoni 12', bg='#E10022', fg='White')
        
        #Botões
        self.pedir_carona = tk.Button(self.Tela_principal)
        self.pedir_carona.grid(row=3, column=0,columnspan=1)
        self.pedir_carona.configure(text= "Pedir Carona ")
        self.pedir_carona.bind('<1>',self.clicou_pedir)
        
        self.oferecer_carona = tk.Button(self.Tela_principal)
        self.oferecer_carona.grid(row=4, column=0,columnspan=1)
        self.oferecer_carona.configure(text= "Oferecer Carona ")
        self.oferecer_carona.bind('<1>',self.clicou_oferecer)
        
        self.alterar_perfil = tk.Button(self.Tela_principal)
        self.alterar_perfil.grid(row=3, column=2,columnspan=1)
        self.alterar_perfil.configure(text= "Alterar meu Perfil ")
        self.alterar_perfil.bind('<1>',self.clicou_alterar)
                
        self.cancelar_pedido_carona = tk.Button(self.Tela_principal)
        self.cancelar_pedido_carona.grid(row=3, column=1)
        self.cancelar_pedido_carona.configure(text='Cancelar Pedido')
        self.cancelar_pedido_carona.bind('<1>',self.cancelar_pedido)

        self.cancelar_oferta_carona = tk.Button(self.Tela_principal)
        self.cancelar_oferta_carona.grid(row=4, column=1)
        self.cancelar_oferta_carona.configure(text='Cancelar Oferta')
        self.cancelar_oferta_carona.bind('<1>',self.cancelar_oferta)

        self.voltar_pagina_principal = tk.Button(self.Tela_principal)
        self.voltar_pagina_principal.configure(text='Log Out')
        self.voltar_pagina_principal.grid(row=4, column=2,columnspan=1)
        self.voltar_pagina_principal.bind('<1>',self.clicou_voltar_tela_inicial)


####################################################################
        
        
    def Tela_pedir_carona_frame(self):
        
        #Configurações do Frame
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
        

        #Título
        caronas = tk.Label(self.Tela_pedir_carona)
        caronas.grid(row=0, column=1,columnspan=3, sticky="nsew")
        caronas.configure(text= "Pedir",font='Bodoni 50', bg='#E10022', fg='White')
        
        Logo = tk.Label(self.Tela_pedir_carona)
        Logo.grid(row=1, column=1,columnspan=3, sticky="nsew")
        Logo.configure(text= "Caronas",font='Bodoni 50', bg='#E10022', fg='White')
        
        #Horários
        label_horários = tk.Label(self.Tela_pedir_carona)
        label_horários.grid(row=2, column=1, sticky="nsew")
        label_horários.configure(text= "Horários: ",font='Bodoni 12', bg='#E10022', fg='White')
        
        self.hora_pedido = tk.StringVar()
        self.hora_pedido.set(self.horarios[0])
        self.Horários = ttk.OptionMenu(self.Tela_pedir_carona,self.hora_pedido,*self.horarios)
        self.Horários.grid(row=2, column=2, sticky="ew")
        
        
        #Data
        data = tk.Label(self.Tela_pedir_carona)
        data.grid(row=3, column=1, sticky="nsew")
        data.configure(text= "Dia e Mês: ",font='Bodoni 12', bg='#E10022', fg='White')
        
        self.dia_pedido = tk.StringVar()
        self.dia_pedido.set(self.dia_lista[0])
        self.dia= ttk.OptionMenu(self.Tela_pedir_carona,self.dia_pedido,*self.dia_lista)
        self.dia.grid(row=3, column=2, sticky="w")
        
        self.mes_pedido = tk.StringVar()
        self.mes_pedido.set(self.mes_lista[0])
        self.dia= ttk.OptionMenu(self.Tela_pedir_carona,self.mes_pedido,*self.mes_lista)
        self.dia.grid(row=3, column=3, sticky="w")
        
        
	  #Saída        
        saida = tk.Label(self.Tela_pedir_carona)
        saida.grid(row=4, column=1, sticky="nsew")
        saida.configure(text= "Local de Partida: ",font='Bodoni 12', bg='#E10022', fg='White')
        
        self.bairro_saida_pedido = tk.StringVar()
        self.bairro_saida_pedido.set(self.bairros[0])
        self.bairro_de_saida = ttk.OptionMenu(self.Tela_pedir_carona,self.bairro_saida_pedido,*self.bairros)
        self.bairro_de_saida.grid(row=4, column=2, sticky="ew")
        
      
        #Destino
        chegada = tk.Label(self.Tela_pedir_carona)
        chegada.grid(row=5, column=1, sticky="nsew")
        chegada.configure(text= "Local de Destino: ",font='Bodoni 12', bg='#E10022', fg='White')
        
        self.bairro_chegada_pedido = tk.StringVar()
        self.bairro_chegada_pedido.set(self.bairros[0])
        self.bairro_de_chegada = ttk.OptionMenu(self.Tela_pedir_carona,self.bairro_chegada_pedido,*self.bairros)
        self.bairro_de_chegada.grid(row=5, column=2, sticky="ew")
        
        
        #Lugares
        label_lugares = tk.Label(self.Tela_pedir_carona)
        label_lugares.grid(row=6, column=1, sticky="nsew")
        label_lugares.configure(text= "Lugares Necessários: ",font='Bodoni 12', bg='#E10022', fg='White')

        self.lugares_pedido = tk.StringVar()
        self.lugares_pedido.set(self.lugares[0])
        self.Lugares = ttk.OptionMenu(self.Tela_pedir_carona,self.lugares_pedido,*self.lugares)
        self.Lugares.grid(row=6, column=2, sticky="ew")
        
      
        
  #Botões
  
        #Voltar
        self.voltar_pagina_principal = tk.Button(self.Tela_pedir_carona)
        self.voltar_pagina_principal.configure(text='Voltar')
        self.voltar_pagina_principal.grid(row=7, column=1)
        self.voltar_pagina_principal.bind('<1>',self.clicou_voltar)
        
  	  #Confirmar
        self.confirmar = tk.Button(self.Tela_pedir_carona)
        self.confirmar.configure(text='Confirmar')
        self.confirmar.grid(row=7, column=3)
        self.confirmar.bind('<1>',self.clicou_confirmar_pedido)
        self.confirmar.bind('<Return>',self.clicou_confirmar_pedido)
        
      
####################################################################

        
    def Tela_oferecer_carona_frame(self):
        
        #Configurações do Frame
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
        
        #Título
        caronas = tk.Label(self.Tela_oferecer_carona)
        caronas.grid(row=0, column=1,columnspan=3, sticky="nsew")
        caronas.configure(text= "Oferecer",font='Bodoni 50', bg='#E10022', fg='White')
        
        Logo = tk.Label(self.Tela_oferecer_carona)
        Logo.grid(row=1, column=1,columnspan=3, sticky="nsew")
        Logo.configure(text= "Caronas",font='Bodoni 50', bg='#E10022', fg='White')

        #Horários
        label_horários = tk.Label(self.Tela_oferecer_carona)
        label_horários.grid(row=2, column=1, sticky="nsew")
        label_horários.configure(text= "Horários: ",font='Bodoni 12', bg='#E10022', fg='White')
        
        self.horarios_oferecer = tk.StringVar()
        self.horarios_oferecer.set(self.horarios[0])
        self.Horários = ttk.OptionMenu(self.Tela_oferecer_carona,self.horarios_oferecer,*self.horarios)
        self.Horários.grid(row=2, column=2, sticky="ew")
          
        
        #Data
        data = tk.Label(self.Tela_oferecer_carona)
        data.grid(row=3, column=1, sticky="nsew")
        data.configure(text= "Dia e Mês: ",font='Bodoni 12', bg='#E10022', fg='White')
        
        self.dia_oferecido = tk.StringVar()
        self.dia_oferecido.set(self.dia_lista[0])
        self.dia= ttk.OptionMenu(self.Tela_oferecer_carona,self.dia_oferecido,*self.dia_lista)
        self.dia.grid(row=3, column=2, sticky="w")
        
        self.mes_oferecido = tk.StringVar()
        self.mes_oferecido.set(self.mes_lista[0])
        self.dia= ttk.OptionMenu(self.Tela_oferecer_carona,self.mes_oferecido,*self.mes_lista)
        self.dia.grid(row=3, column=3, sticky="w")
        
        
        #Saída
        saida = tk.Label(self.Tela_oferecer_carona)
        saida.grid(row=4, column=1, sticky="nsew")
        saida.configure(text= "Local de Partida: ",font='Bodoni 12', bg='#E10022', fg='White')

        self.bairro_saida_oferta = tk.StringVar()
        self.bairro_saida_oferta.set(self.bairros[0])
        self.bairro_de_saida = ttk.OptionMenu(self.Tela_oferecer_carona,self.bairro_saida_oferta,*self.bairros)
        self.bairro_de_saida.grid(row=4, column=2, sticky="ew")
        
        
        #Destino  
        chegada = tk.Label(self.Tela_oferecer_carona)
        chegada.grid(row=5, column=1, sticky="nsew")
        chegada.configure(text= "Local de Chegada: ",font='Bodoni 12', bg='#E10022', fg='White')
        
        self.bairro_chegada_oferta = tk.StringVar()
        self.bairro_chegada_oferta.set(self.bairros[0])
        self.bairro_de_chegada = ttk.OptionMenu(self.Tela_oferecer_carona,self.bairro_chegada_oferta,*self.bairros)
        self.bairro_de_chegada.grid(row=5, column=2, sticky="ew")
        
        
        #Lugares
        label_lugares = tk.Label(self.Tela_oferecer_carona)
        label_lugares.grid(row=6, column=1, sticky="nsew")
        label_lugares.configure(text= "Lugares Disponíveis: ",font='Bodoni 12', bg='#E10022', fg='White')
        
        self.lugares_oferecer = tk.StringVar()
        self.lugares_oferecer.set(self.lugares[0])
        self.Lugares = ttk.OptionMenu(self.Tela_oferecer_carona,self.lugares_oferecer,*self.lugares)
        self.Lugares.grid(row=6, column=2, sticky="ew")
        

    #Botões
        #Voltar
        self.voltar_pagina_principal = tk.Button(self.Tela_oferecer_carona)
        self.voltar_pagina_principal.configure(text='Voltar')
        self.voltar_pagina_principal.grid(row=7, column=1)
        self.voltar_pagina_principal.bind('<1>',self.clicou_voltar)
        
        #Confirmar
        self.confirmar = tk.Button(self.Tela_oferecer_carona)
        self.confirmar.configure(text='Confirmar')
        self.confirmar.grid(row=7, column=3)
        self.confirmar.bind('<1>',self.clicou_confirmar_oferta)
        self.confirmar.bind('<Return>',self.clicou_confirmar_oferta)
                
        
####################################################################


    def Tela_ler_perfil_frame(self):
      
      	#Configurações do Frame
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
        
        #Acessando o Firebase
        dados = firebase.FirebaseApplication('https://caronas.firebaseio.com/Users/')
        


        #Nome
        nome_label = tk.Label(self.tela_ler_perfil)
        nome_label.grid(row=2, column=0, sticky="nsew")
        nome_label.configure(text= "Nome completo: ",font='Bodoni 12', bg='#E10022', fg='White')
        
        nome = tk.StringVar()
        nome.set(dados.get(self.usuarios, 'Nome'))
        self.nome_entrada = tk.Entry(self.tela_ler_perfil, textvariable = nome)
        self.nome_entrada.grid(row=2, column=1, sticky="ew")
        
        
        #Email
        email_label = tk.Label(self.tela_ler_perfil)
        email_label.grid(row=3, column=0, sticky="nsew")
        email_label.configure(text= "E-mail: ",font='Bodoni 12', bg='#E10022', fg='White')

        email = tk.StringVar()
        email.set (dados.get(self.usuarios, 'email'))
        self.email_entrada = tk.Entry(self.tela_ler_perfil, textvariable = email)
        self.email_entrada.grid(row=3, column=1, sticky="ew")
        
        
        #Celular
        celular_label = tk.Label(self.tela_ler_perfil)
        celular_label.grid(row=4, column=0, sticky="nsew")
        celular_label.configure(text= "Número de Celular*: ",font='Bodoni 12', bg='#E10022', fg='White')
        
        numero = tk.StringVar()
        numero.set (dados.get(self.usuarios, 'telefone'))
        self.celular_entrada = tk.Entry(self.tela_ler_perfil, textvariable = numero)
        self.celular_entrada.grid(row=4, column=1, sticky="ew")
        

        #Nome de Usuário
        usuario_label = tk.Label(self.tela_ler_perfil)
        usuario_label.grid(row=5, column=0, sticky="nsew")
        usuario_label.configure(text= "Usuário: ",font='Bodoni 12', bg='#E10022', fg='White')
        
        user = tk.StringVar()
        user.set (self.usuarios)
        self.usuario_entrada = tk.Entry(self.tela_ler_perfil, textvariable =user)
        self.usuario_entrada.configure(state = "disabled")
        self.usuario_entrada.grid(row=5, column=1, sticky="ew")

        #Senha
        senha_label = tk.Label(self.tela_ler_perfil)
        senha_label.grid(row=6, column=0, sticky="nsew")
        senha_label.configure(text= "Senha: ",font='Bodoni 12', bg='#E10022', fg='White')

        senha = tk.StringVar()
        senha.set (dados.get(self.usuarios, 'senha'))
        self.senha_entrada = tk.Entry(self.tela_ler_perfil, textvariable = senha)
        self.senha_entrada.grid(row=6, column=1, sticky="ew")
        self.senha_entrada.configure(show='*')
        
        
        #Confirma Senha
        senha_confirma_label = tk.Label(self.tela_ler_perfil)
        senha_confirma_label.grid(row=7, column=0, sticky="nsew")
        senha_confirma_label.configure(text= "Confirmar senha: ",font='Bodoni 12', bg='#E10022', fg='White')

        senha = tk.StringVar()
        senha.set (dados.get(self.usuarios, 'senha'))
        self.senha_confirma_entrada = tk.Entry(self.tela_ler_perfil, textvariable = senha)
        self.senha_confirma_entrada.grid(row=7, column=1, sticky="ew")
        self.senha_confirma_entrada.configure(show='*')
        
           
        #Nota sobre o celular
        nota_label = tk.Label(self.tela_ler_perfil)
        nota_label.grid(row=8, column=1, sticky="nsew")
        nota_label.configure(text= "*Mais importante do cadastro, digite apenas 9xxxx-xxxx",font='Bodoni 12', bg='#E10022', fg='White')


    #Botões
    		#Salvar
        self.salvar_cadastro = tk.Button(self.tela_ler_perfil)
        self.salvar_cadastro.grid(row=8, column=2)
        self.salvar_cadastro.configure(text='salvar')
        self.salvar_cadastro.bind('<1>',self.clicou_salvar_alteracoes)
        
        #Voltar
        self.voltar_tela_inicial = tk.Button(self.tela_ler_perfil)
        self.voltar_tela_inicial.grid(row=8, column=0)
        self.voltar_tela_inicial.configure(text='Voltar')
        self.voltar_tela_inicial.bind('<1>',self.clicou_voltar)
                
                
####################     Função dos botões

    #Leva para a página de Cadastro    
    def clicou_cadastro(self,event):
        self.Tela_cadastro_frame() 
        
    #Leva para a página de Login    
    def clicou_login(self,event):
        self.Tela_login_frame()

    #Leva para a Página Principal    
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
        
    #Leva de volta para a página inicial 
    def clicou_voltar_tela_inicial(self,event):
        self.tela_inicial_frame()  

    #Salvar informações do cadastro    
    def clicou_salvar(self,event):
        fb = firebase.FirebaseApplication('https://caronas.firebaseio.com', None)
        cadastros = fb.get('Users', None)
        
        if not self.usuario_entrada.get() in cadastros:
            
            validando_email = validate_email(self.email_entrada.get())
            
            if self.senha_entrada.get() == self.senha_confirma_entrada.get() and self.nome_entrada.get() != '' and validando_email == True and self.celular_entrada.get() != '' and self.celular_entrada.get() != '() 9' and self.usuario_entrada.get() != '':
                
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
        
    #Função que leva a tela pedir carona
    def clicou_pedir(self,event):
        self.Tela_pedir_carona_frame()
                
    #Função que leva para a tela principal de volta
    def clicou_voltar(self,event):
        self.tela_principal_frame()
        
    #Função que confirma o pedido e verifica se já existem motorista em espera
    def clicou_confirmar_pedido(self,event):
        confirmando_pedido = tkm.askyesno('Confirmando','Deseja confirmar pedido?') #Confirma que a pessoa quer solicitar carona
            
        if confirmando_pedido:
          	#Adicionando ao firebase caso não ache motoristas dispóniveis
            fb = firebase.FirebaseApplication('https://caronas.firebaseio.com', None)
            dicionario = {'Horário': self.hora_pedido.get(),'Local de Partida': self.bairro_saida_pedido.get(), 'Local de Destino': self.bairro_chegada_pedido.get(), 'Lugares Necessários': self.lugares_pedido.get(), 'Dia': self.dia_pedido.get(), 'Mês': self.mes_pedido.get()}
            fb.put('/Pedidos', self.usuarios, dicionario)
            
            ofertas = fb.get('Ofertas', None)
            
            fb2 = firebase.FirebaseApplication('https://caronas.firebaseio.com/Pedidos/')
            fb3 = firebase.FirebaseApplication('https://caronas.firebaseio.com/Ofertas/')
            fb4 = firebase.FirebaseApplication('https://caronas.firebaseio.com/Users/')

            #Salvando as informações de passageiro para fazer comparações futuras
            lugar_saida_pedido = fb2.get(self.usuarios, 'Local de Partida')
            lugar_chegada_pedido = fb2.get(self.usuarios, 'Local de Destino')
            horario_pedido = fb2.get(self.usuarios, 'Horário')
            dia_pedido = fb2.get(self.usuarios, 'Dia')
            mes_pedido = fb2.get(self.usuarios, 'Mês')
            lugares_necessarios_pedido = fb2.get(self.usuarios, 'Lugares Necessários')
            
            for motorista in ofertas: #Procurando um motorista no dicionario ofertas
                if motorista == self.usuarios: #Caso o motorista seja também o passageiro, passa direto
                    continue
      					
                #Salvando as informações de motorista para fazer comparaçõeo futuras
                lugar_saida_oferta = fb3.get(motorista, 'Local de Partida')
                lugar_chegada_oferta = fb3.get(motorista, 'Local de Destino')
                horario_oferta = fb3.get(motorista, 'Horário')
                dia_oferta = fb3.get(motorista, 'Dia')
                mes_oferta = fb3.get(motorista, 'Mês')
                lugares_necessarios_oferta = fb3.get(motorista, 'Lugares Necessários')

                if lugares_necessarios_oferta != None:
                    lgno = int (lugares_necessarios_oferta) #lugares ofertados transformado em número inteiro
                else:
                    continue

                lgnp = int (lugares_necessarios_pedido) #lugares pedidos transformado em número inteiro
                
                #Fazendo as comparações para dar match
                if lugar_saida_pedido == lugar_saida_oferta and lugar_chegada_pedido == lugar_chegada_oferta and lgnp <= lgno and horario_pedido == horario_oferta and dia_pedido == dia_oferta and mes_pedido == mes_oferta:
                    #Salvando nome, telefone e email do motorista para poder enviar email para ele
                    nome = fb4.get(motorista,'Nome')
                    celular = fb4.get(motorista, 'telefone')
                    email = fb4.get(motorista, 'email')
                    
                    #Mandando email para o passageiro de confirmação de carona
                    fromaddr = 'lucarn@al.insper.edu.br'
                    toaddrs = self.email
    
                    msg = 'Seu carona é: {0}\nSeu telefone é: {1}\nSeu email é: {2}\n\nEntre em contato com seu carona para combinarem melhor!\nObrigado por escolher o Caronas Insper!\nA equipe agradece!!'.format(nome, celular, email).encode('UTF-8')
                    
                    server = smtplib.SMTP('insper.edu.br')
                    server.set_debuglevel(1)
                    server.sendmail(fromaddr, toaddrs, msg)
                    server.quit()
                    
  									#Mandando email para o motorista de confirmação de carona
                    fromaddr = 'lucarn@al.insper.edu.br'
                    toaddrs = email
    
                    msg = 'Seu carona é: {0}\nSeu telefone é: {1}\nSeu email é: {2}\n\nEntre em contato com seu carona para marcarem melhor!\nObrigado por escolher o Caronas Insper!\nA equipe agradece!!'.format(self.nome_completo, self.telefone, self.email).encode('UTF-8')
                    
                    server = smtplib.SMTP('insper.edu.br')
                    server.set_debuglevel(1)
                    server.sendmail(fromaddr, toaddrs, msg)
                    server.quit()

                    lgno -= lgnp #Subtraindo o total de lugares disponíveis no carro do motorista
                    
                    fb.delete('/Pedidos', self.usuarios) #Apagando o passageiro do dicionário pedidos

                    if lgno > 0: #Verifica se ainda existem lugares no carro do motorista, caso seja verdade, atualiza o valor
                        dicionario_motorista = {'Horário': horario_oferta,'Local de Partida': lugar_saida_oferta, 'Local de Destino': lugar_chegada_oferta, 'Lugares Necessários': lgno, 'Dia': dia_oferta, 'Mês': mes_oferta}
                        fb.put('/Ofertas', motorista, dicionario_motorista)
                    else:
                        fb.delete('/Ofertas', motorista) #Apaga o motorista do dicionário de ofertas caso não tenha mais lugares em seu carro
                    
                    tkm.showinfo('Carona','As informações de seu carona estão no seu email!') #Mensagem de confirmação de carona
                    break
            else:
                tkm.showinfo('Carona', 'Não existem caronas no momento. Quando exister alguém, você será notificado por email!') #Mensagem de que não existem motoristas no momento
                                
            self.tela_principal_frame() #Volta para a tela principal
	
  
    #Função que confirma a oferta de alguém e verifica se já existem passageiros em espera
    def clicou_confirmar_oferta(self,event):
        confirmando_oferta = tkm.askyesno('Confirmando','Deseja confirmar oferta?') #Confirma que a pessoa quer oferecer carona
            
        if confirmando_oferta:
          	#Salvando as informações de oferta no dicionário ofertas para caso não existam passageiros no momento
            fb = firebase.FirebaseApplication('https://caronas.firebaseio.com', None)
            dicionario = {'Horário': self.horarios_oferecer.get(),'Local de Partida': self.bairro_saida_oferta.get(), 'Local de Destino': self.bairro_chegada_oferta.get(), 'Lugares Necessários': self.lugares_oferecer.get(), 'Dia': self.dia_oferecido.get(), 'Mês': self.mes_oferecido.get()}
            fb.put('/Ofertas', self.usuarios, dicionario)

            pedidos = fb.get('Pedidos', None)
            
            fb2 = firebase.FirebaseApplication('https://caronas.firebaseio.com/Pedidos/')
            fb3 = firebase.FirebaseApplication('https://caronas.firebaseio.com/Ofertas/')
            fb4 = firebase.FirebaseApplication('https://caronas.firebaseio.com/Users/')

						#Salvando as informações de motorista para fazer comparaçõeo futuras
            lugar_saida_oferta = fb3.get(self.usuarios, 'Local de Partida')
            lugar_chegada_oferta = fb3.get(self.usuarios, 'Local de Destino')
            horario_oferta = fb3.get(self.usuarios, 'Horário')
            dia_oferta = fb3.get(self.usuarios, 'Dia')
            mes_oferta = fb3.get(self.usuarios, 'Mês')
            lugares_necessarios_oferta = fb3.get(self.usuarios, 'Lugares Necessários')
            
            lgno = int (lugares_necessarios_oferta) #lugares ofertados transformado em número inteiro

            for passageiro in pedidos:
                if passageiro == self.usuarios: #Caso o passageiro seja também o motorista, passa direto
                  	continue
                    
                #Salvando as informações de passageiro para fazer comparaçõeo futuras
                lugar_saida_pedido = fb2.get(passageiro, 'Local de Partida')
                lugar_chegada_pedido = fb2.get(passageiro, 'Local de Destino')
                horario_pedido = fb2.get(passageiro, 'Horário')
                dia_pedido = fb2.get(passageiro, 'Dia')
                mes_pedido = fb2.get(passageiro, 'Mês')
                lugares_necessarios_pedido = fb2.get(passageiro, 'Lugares Necessários')

                if lugares_necessarios_pedido != None: #Caso existam lugares disponíveis
                    lgnp = int (lugares_necessarios_pedido) #lugares pedidos transformado em número inteiro
                else:
                    continue
								
                #Fazendo as comparações para dar match
                if dia_oferta == dia_pedido and mes_oferta == mes_pedido and lugar_saida_oferta == lugar_saida_pedido and lugar_chegada_oferta == lugar_chegada_pedido and lgno >= lgnp and horario_oferta == horario_pedido:                    
                    #Salvando as informações do passageiro para mandar email confirmando carona
                    nome = fb4.get(passageiro,'Nome')
                    celular = fb4.get(passageiro, 'telefone')
                    email = fb4.get(passageiro, 'email')
                         
                    #Mandando email para o motorista  
                    fromaddr = 'lucarn@al.insper.edu.br'
                    toaddrs = self.email

                    msg = 'O seu carona é: {0}\nSeu telefone é: {1}\nSeu email é: {2}\n\nEntre em contato com seu carona para marcarem melhor!\nObrigado por escolher o Caronas Insper!\nA equipe agradece!!'.format(nome, celular, email).encode('UTF-8')
                    
                    server = smtplib.SMTP('insper.edu.br')
                    server.set_debuglevel(1)
                    server.sendmail(fromaddr, toaddrs, msg)
                    server.quit()
                    
  									#Mandando email para o carona
                    fromaddr = 'lucarn@al.insper.edu.br'
                    toaddrs = email

                    msg = 'Seu carona é: {0}\nSeu telefone é: {1}\nSeu email é: {2}\n\nEntre em contato com seu carona para combinarem melhor!\nObrigado por escolher o Caronas Insper!\nA equipe agradece!!'.format(self.nome_completo, self.telefone, self.email).encode('UTF-8')
                    
                    server = smtplib.SMTP('insper.edu.br')
                    server.set_debuglevel(1)
                    server.sendmail(fromaddr, toaddrs, msg)
                    server.quit()

                    lgno -= lgnp #Subtraindo a quantidade de lugares disponíveis no carro do motorista
                    
                    fb.delete('/Pedidos', passageiro) #Apaga o passageiro do dicionário pedidos

                    if lgno > 0: #Verifica se ainda existem lugares disponíveis no carro do motorista, caso exista, o valor é atualizado
                        dicionario['Lugares Necessários'] = lgno
                        fb.put('/Ofertas', self.usuarios, dicionario)
              					#Aparece mensagem que confirmou carona
                        tkm.showinfo('Carona', 'As informações de seu carona estão no seu email! Aguarde alguns instantes para verificarmos se há outra carona!')

                    else:
                        fb.delete('/Ofertas', self.usuarios)
                        #Aparece mensagem confirmando carona
                        tkm.showinfo('Carona', 'As informações de seu carona estão no seu email!')
                        break

            else:
                tkm.showinfo('Carona', 'Não existem caronas no momento. Caso exista alguém, você será notificado por email!') #Mensagem caso não existam passageiros no momento
        
            self.tela_principal_frame() #Volta para a tela principal

    #Função que leva para a tela de oferecer carona
    def clicou_oferecer(self,event):
        self.Tela_oferecer_carona_frame()

    #Função que leva a tela de alterar perfil
    def clicou_alterar(self,event):
        self.Tela_ler_perfil_frame()
        
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
            
    #Atualiza as informações de um cadastro
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
    
    #Leva para a tela sobre os criadores e o projeto
    def clicou_sobre_nós(self,event):
        self.tela_criadores_frame()
    
    #Leva para a tela de mandar email
    def clicou_contato(self,event):
        self.tela_contato_frame()

    #Enviando email de reclamações para os desenvolvedores
    def enviar_contato(self,event):
        validando_email = validate_email(self.meu_email.get()) #Verificando se o email é email
        
        if validando_email == True:
            fromaddr = self.meu_email.get() #Pegando o email colocado pela pessoa e usando como 
            toaddrs = 'caronas.insper@gmail.com' #Email de reclamações do caronas
            
            msg = self.reclamacao.get("1.0",'end-1c') #Pegando mensagem enviada pela pessoa
            
            server = smtplib.SMTP('insper.edu.br')
            server.set_debuglevel(1)
            server.sendmail(fromaddr, toaddrs, msg)
            server.quit()
		            
            tkm.showinfo('Confirmação', 'Email enviado com sucesso! Retornaremos sua mensagem o mais rápido possível!') #Mensagem de envio confirmado
            self.tela_inicial_frame() #Voltando para a tela inicial
        
        else:
            tkm.showinfo('Erro', 'Email inválido!') #Mensagem de erro caso o email seja inválido
          

########## iniciando o programa
    def iniciar(self):
        self.root.mainloop()

Caronas = Telas()
Caronas.iniciar()
