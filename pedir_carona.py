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
        
    def iniciar(self):
        self.window.mainloop()
        
    def clicou_confirmar(self,event):
        pass
        
    def clicou_voltar(self,event):
        pass
        
teste = pedir_carona()
teste.iniciar()