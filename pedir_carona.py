import tkinter as tk

class pedir_carona:
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
        
        self.caronas = tk.Label(self.window)
        self.caronas.grid(row=1, column=1,columnspan=3, sticky="nsew")
        self.caronas.configure(text= "Caronas",font='Bodoni 100', bg='#E10022', fg='White')
        
        
        self.Logo = tk.Label(self.window)
        self.Logo.grid(row=2, column=1,columnspan=3, sticky="nsew")
        self.Logo.configure(text= "Insper",font='Bodoni 100', bg='#E10022', fg='White')
        
        self.bairro_de_saida = tk.Entry(self.window)
        self.bairro_de_saida.grid(row=4, column=2, sticky="ew")
        
        self.saida = tk.Label(self.window)
        self.saida.grid(row=4, column=1,columnspan=1, sticky="nsew")
        self.saida.configure(text= "Local de saída: ",font='Bodoni 24', bg='#E10022', fg='White')
        
        self.bairro_de_chegada = tk.Entry(self.window)
        self.bairro_de_chegada.grid(row=5, column=2, sticky="ew")
        
        self.chegada = tk.Label(self.window)
        self.chegada.grid(row=5, column=0,columnspan=2, sticky="nsew")
        self.chegada.configure(text= "Local de chegada: ",font='Bodoni 24', bg='#E10022', fg='White')
        
        
    def iniciar(self):
        self.window.mainloop()
        
teste = pedir_carona()
teste.iniciar()