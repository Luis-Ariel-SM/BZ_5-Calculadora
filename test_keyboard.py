import unittest
import tkinterTestCase
import calculator

from tkinter import *
from tkinter import ttk

class TestDisplay (tkinterTestCase.TkTestCase):

    def setUp (self):
        self.k = calculator.Keyboard (self.root)
        self.k.pack()
        self.k.wait_visibility()

    def tearDown(self):
        self.k.update()
        self.k.destroy()
    
    def test_render_Ok (self):
        self.assertEqual (self.k.winfo_height(), 250)
        self.assertEqual (self.k.winfo_width(), 272)
        for btn in self.k.children.values():
            self.assertIsInstance(btn, calculator.CalcButton)
        self.assertEqual(18,len(self.k.children), 18)
    
    def test_render_roman_Ok(self):
        teclado_romano = calculator.Keyboard(self.root, 'R')
        teclado_romano.pack()
        teclado_romano.wait_visibility()

        self.assertEqual (teclado_romano.winfo_height(), 250)
        self.assertEqual (teclado_romano.winfo_width(), 272)
        for btn in teclado_romano.children.values():
            self.assertIsInstance(btn, calculator.CalcButton)
        self.assertEqual(len(teclado_romano.children), 13)

        teclado_romano.update()
        teclado_romano.destroy()
      
if __name__ == '__main__':
    unittest.main()