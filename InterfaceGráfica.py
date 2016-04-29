import tkinter as tk


class Tela_inicial():
    
    def __init__(self):
        
        self.window = tk.Tk()
        self.window.title("Caronas Insper")
        self.window.geometry("640x800")
        self.window.configure(background='#E10022')
        self.window.rowconfigure(0, minsize=50, weight=1)
        self.window.rowconfigure(1, minsize=50, weight=1)
        self.window.rowconfigure(2, minsize=50, weight=1)
        self.window.rowconfigure(3, minsize=50, weight=1)
        self.window.rowconfigure(4, minsize=50, weight=1)
        self.window.rowconfigure(5, minsize=50, weight=1)
        self.window.rowconfigure(6, minsize=50, weight=1)
        self.window.rowconfigure(7, minsize=50, weight=1)
        self.window.rowconfigure(8, minsize=50, weight=1)
        self.window.rowconfigure(9, minsize=50, weight=1)
        self.window.rowconfigure(10, minsize=50, weight=1)
        self.window.rowconfigure(11, minsize=50, weight=1)
        self.window.rowconfigure(12, minsize=50, weight=1)
        self.window.rowconfigure(13, minsize=50, weight=1)
        self.window.rowconfigure(14, minsize=50, weight=1)
        self.window.rowconfigure(15, minsize=50, weight=1)
        
        self.window.columnconfigure(0, minsize=20, weight=1)
        self.window.columnconfigure(1, minsize=50, weight=1)
        self.window.columnconfigure(2, minsize=50, weight=1)
        self.window.columnconfigure(3, minsize=50, weight=1)
        self.window.columnconfigure(4, minsize=50, weight=1)
        self.window.columnconfigure(5, minsize=50, weight=1)
        self.window.columnconfigure(6, minsize=50, weight=1)
        self.window.columnconfigure(7, minsize=50, weight=1)
        self.window.columnconfigure(8, minsize=50, weight=1)
        self.window.columnconfigure(9, minsize=50, weight=1)
        self.window.columnconfigure(10, minsize=50, weight=1)
        self.window.columnconfigure(11, minsize=50, weight=1)
        self.window.columnconfigure(12, minsize=50, weight=1)
        self.window.columnconfigure(13, minsize=20, weight=1)
        
        
        
        self.caronas = tk.Label(self.window)
        self.caronas.grid(row=1, column=3,columnspan=8, rowspan=2, sticky="nsew")
        self.caronas.configure(text= "Caronas",font='Bodoni 100', bg='#E10022', fg='White')
        
        self.Logo = tk.Label(self.window)
        self.Logo.grid(row=3, column=4,columnspan=6, rowspan=2 ,sticky="nsew")
        self.Logo.configure(text= "Insper",font='Bodoni 100', bg='#E10022', fg='White')

        self.Login = tk.Button(self.window)
        self.Login.grid(row=11, column=5,columnspan=4, sticky="ew")
        self.Login.configure(text="Login", font='Arial 24')
        self.Login.bind('<1>',self.tela_login)
        
        self.Cadastro = tk.Button(self.window)
        self.Cadastro.grid(row=12, column=5,columnspan=4, sticky="ew")
        self.Cadastro.configure(text="Cadastrar-se", font='Arial 24')
        self.Cadastro.bind('<1>',self.tela_cadastro)


   
    

    def tela_login(self, event):

        self.Usuário = tk.Label(self.window)
        self.Usuário.grid(row=11, column=3, columnspan=2, sticky="nsew")
        self.Usuário.configure(text= "Usuário: ",font='Bodoni 13', bg='#E10022', fg='White')
        
        self.entrada_usuário = tk.Entry(self.window)
        self.entrada_usuário.grid(row=11, column=3, columnspan=4, sticky="ew")
        
        self.Senha = tk.Label(self.window)
        self.Senha.grid(row=12, column=3,columnspan=2, sticky="nsew")
        self.Senha.configure(text= "Senha: ",font='Bodoni 13', bg='#E10022', fg='White')
        
        self.entrada_senha = tk.Entry(self.window)
        self.entrada_senha.grid(row=12, column=3, columnspan=4, sticky="ew")
        
    
    def tela_cadastro(self, event):
        #Cada pessoa deve ser uma chave de um dicionário
        #Por isso criar dicionário no começo dessa função
        #A chave é o nome de uma pessoa e os valres estarão em uma lista em uma mesma ordem
        self.dic_pessoas = {}
        
        self.Usuário = tk.Label(self.window)
        self.Usuário.grid(row=11, column=3, columnspan=3, sticky="nsew")
        self.Usuário.configure(text= "Nome de Usuário: ",font='Bodoni 13', bg='#E10022', fg='White')
        
        self.nome_de_usuario = tk.Entry(self.window)
        self.nome_de_usuario.grid(row=11, column=6, columnspan=4, sticky="ew")
        
        self.Senha = tk.Label(self.window)
        self.Senha.grid(row=12, column=3, columnspan=3, sticky="nsew")
        self.Senha.configure(text= " Sua Senha: ",font='Bodoni 13', bg='#E10022', fg='White')
        
        self.nova_senha = tk.Entry(self.window)
        self.nova_senha.grid(row=12, column=6, columnspan=4, sticky="ew")

        self.dic_pessoas[self.nome_de_usuario]=self.nova_senha
        
        self.salvar_novo_cadastro = tk.Button(self.window)
        self.salvar_novo_cadastro.grid(row=14, column=10,columnspan=1)
        self.salvar_novo_cadastro.configure(text='salvar')
        self.salvar_novo_cadastro.bind('<1>',self.clicou_salvar)
        
#        self.novo_arquivo = open('cadastros.txt','a') #Arquivo onde as informações serão salvas
#        self.novo_arquivo.write('\n{0}'.format(self.dic_pessoas)) #Escrevendo o login
#        self.novo_arquivo.close() #Fechando o arquivo
        
    def clicou_salvar(self,event):
        self.novo_arquivo = open('cadastros.txt','a') #Arquivo onde as informações serão salvas
        self.novo_arquivo.write('\n{0}'.format(self.dic_pessoas)) #Escrevendo o login
        self.novo_arquivo.close() #Fechando o arquivo
        self.Tela_login()
        
    def iniciar(self):
        self.window.mainloop()

        
            
Caronas_Insper = Tela_inicial()
Caronas_Insper.iniciar()
