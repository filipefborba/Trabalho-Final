import firecall
import tkinter as tk


class TestApp:
    def __init__(self):
        self.button_pressed = False
        self.fb = firecall.Firebase("https://popping-torch-5753.firebaseio.com/")
        self.watch = None
        self.device_id = ""
        self.other_id = ""
        
        self.root = tk.Tk()
        self.root.title("Test IoT")
        self.root.geometry("300x300")
        self.root.rowconfigure(0, minsize=300)
        self.root.columnconfigure(0, minsize=300)
        self.root.grid()
        
        front_screen = tk.Frame(self.root)
        front_screen.rowconfigure(0, minsize=125)
        front_screen.rowconfigure(1, minsize=125)
        front_screen.rowconfigure(2, minsize=50)
        front_screen.columnconfigure(0, minsize=50)
        front_screen.columnconfigure(1, minsize=250)
        front_screen.grid(row=0, column=0, sticky="nsew")
        
        label_id = tk.Label(front_screen)
        label_id.configure(text="My id:")
        label_id.grid(row=0, column=0, sticky="nsew")
        
        self.entry_id = tk.Entry(front_screen)
        self.entry_id.grid(row=0, column=1, sticky="ew", padx=10)
        
        label_other = tk.Label(front_screen)
        label_other.configure(text="Other id: ")
        label_other.grid(row=1, column=0, sticky="nsew")
        
        self.entry_other = tk.Entry(front_screen)
        self.entry_other.grid(row=1, column=1, sticky="ew", padx=10)
        
        button_start = tk.Button(front_screen)
        button_start.configure(text="Start")
        button_start.configure(command=self.on_button_start_pressed)
        button_start.grid(row=2, column=0, columnspan=2)
        
        self.main_screen = tk.Frame(self.root)
        self.main_screen.rowconfigure(0, minsize=150)
        self.main_screen.rowconfigure(1, minsize=150)
        self.main_screen.columnconfigure(0, minsize=300)
        self.main_screen.grid(row=0, column=0, sticky="nsew")
        
        self.toggle_button = tk.Button(self.main_screen)
        self.toggle_button.configure(text="Open")
        self.toggle_button.configure(relief="raised")
        self.toggle_button.configure(command=self.on_toggle_button_pressed)
        self.toggle_button.grid(row=0, column=0, sticky="nsew")
        
        self.led_label = tk.Label(self.main_screen)
        self.led_label.configure(text="Off")
        self.led_label.configure(bg="gray")
        self.led_label.grid(row=1, column=0, sticky="nsew")
        
        front_screen.tkraise()

    def on_button_start_pressed(self):
        self.device_id = self.entry_id.get()
        self.other_id = self.entry_other.get()        
        if self.device_id == "" or self.other_id == "":
            return
            
        self.init_main_screen()

    def init_main_screen(self):
        self.watch = self.fb.onChange(point="/" + self.other_id, 
                                      frequency=1,
                                      callback=self.on_led_change)        
        self.main_screen.tkraise()

    def on_toggle_button_pressed(self):
        self.button_pressed = not self.button_pressed
        if self.button_pressed:
            self.toggle_button.configure(text="Pressed")
            self.toggle_button.configure(relief="sunken")
            self.fb.put(point="/" + self.device_id, data="Pressed")
        else:
            self.toggle_button.configure(text="Open")
            self.toggle_button.configure(relief="raised")
            self.fb.put(point="/" + self.device_id, data="Open")

    def on_led_change(self, data):
        print("on_led_change, data = {0}".format(data.decode()))

        if data.decode() == "\"Open\"":
            self.led_label.configure(text="Off")
            self.led_label.configure(bg="gray")
        elif data.decode() == "\"Pressed\"":
            self.led_label.configure(text="On")
            self.led_label.configure(bg="green")            

    def on_closing(self):
        if self.watch:
            self.watch.stop()
        self.root.quit()

    def start(self):
        self.root.protocol('WM_DELETE_WINDOW', self.on_closing)        
        self.root.mainloop()
        
app = TestApp()
app.start()