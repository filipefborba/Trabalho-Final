import tkinter as tk


class Telas():
    
    def __init__(self):
        
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
        self.tela_inicial() 
        
        
####   
    def  tela_inicial(self):
        self.caronas = tk.Label(self.window)
        self.caronas.grid(row=1, column=1,columnspan=3, sticky="nsew")
        self.caronas.configure(text= "Caronas",font='Bodoni 100', bg='#E10022', fg='White')
        
        self.Logo = tk.Label(self.window)
        self.Logo.grid(row=2, column=1,columnspan=3, sticky="nsew")
        self.Logo.configure(text= "Insper",font='Bodoni 100', bg='#E10022', fg='White')

        self.Login = tk.Button(self.window)
        self.Login.grid(row=4, column=2, sticky="ew")
        self.Login.configure(text="Login", font='Arial 24')
        self.Login.bind('<1>',self.clicou_login)
        
        self.Cadastro = tk.Button(self.window)
        self.Cadastro.grid(row=5, column=2, sticky="ew")
        self.Cadastro.configure(text="Cadastrar-se", font='Arial 24')
        self.Cadastro.bind('<1>',self.clicou_cadastro)

   
    def clicou_cadastro(self,event):
        self.Tela_cadastro()
        
    def clicou_login(self,event):
        self.Tela_login()
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
    
    def Tela_cadastro(self):
        #Cada pessoa deve ser uma chave de um dicionário
        #Por isso criar dicionário no começo dessa função
        #A chave é o nome de uma pessoa e os valres estarão em uma lista em uma mesma ordem
        self.dic_pessoas = {}
        
        self.Usuário = tk.Label(self.window)
        self.Usuário.grid(row=4, column=1,columnspan=1, sticky="nsew")
        self.Usuário.configure(text= "Nome de usuário: ",font='Bodoni 24', bg='#E10022', fg='White')
        
        self.nome_de_usuario = tk.Entry(self.window)
        self.nome_de_usuario.grid(row=4, column=2, sticky="ew")
        
        self.Senha = tk.Label(self.window)
        self.Senha.grid(row=5, column=1,columnspan=1, sticky="nsew")
        self.Senha.configure(text= "Senha: ",font='Bodoni 24', bg='#E10022', fg='White')
        
        self.nova_senha = tk.Entry(self.window)
        self.nova_senha.grid(row=5, column=2, sticky="ew")


        self.dic_pessoas[self.nome_de_usuario]=self.nova_senha
        
        
        self.salvar_novo_cadastro = tk.Button(self.window)
        self.salvar_novo_cadastro.grid(row=6, column=3,columnspan=1)
        self.salvar_novo_cadastro.configure(text='salvar')
        self.salvar_novo_cadastro.bind('<1>',self.clicou_salvar)
                
    def clicou_salvar(self,event):
        self.novo_arquivo = open('cadastros.txt','a') #Arquivo onde as informações serão salvas
        self.novo_arquivo.write('\n{0}'.format(self.dic_pessoas)) #Escrevendo o login
        self.novo_arquivo.close() #Fechando o arquivo
        self.Tela_login()

 #   def tela_principal(self):
        
        

    def clicou_continuar_tela_principal(self,event):
        self.tela_principal()        
        
    def clicou_voltar_tela_inicial(self,event):
        self.tela_inicial()
    
    def iniciar(self):
        self.window.mainloop()

        
            
Caronas_Insper = Telas()
Caronas_Insper.iniciar()
