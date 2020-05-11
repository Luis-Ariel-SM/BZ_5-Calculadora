from tkinter import *
from tkinter import ttk

import calculator

class MainApp (Tk):
    def __init__ (self): # Construyendo la clase MainApp
        Tk.__init__(self) # llamando a la inicializacion propia de tkinter para que funcione en MainApp
        self.title ('Calculadora')
        self.geometry ('272x300')
        self.pack_propagate(False)

        c = calculator.Controlador (self)
        c.pack (side = TOP, fill = BOTH)

    
    def start(self):
        self.mainloop()


if __name__ == '__main__':
    app = MainApp()
    app.start()
