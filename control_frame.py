from tkinter import *
from tkinter import ttk
from data_visualizer import Data_Visualizer
class Control_Frame(Frame):
    
    def __init__(self, parent):
        Frame.__init__(self, parent, width= 900, height=200, bg='snow3')
        self.parent = parent
        self.grid(row=0, column=0, padx=10, pady=5)
        self._add_algo_dropdown()
        self._add_size_scale()
        self._add_sort_button()
        self._add_randomize_button()
        self._init_data_visualizer()
        
    def _add_algo_dropdown(self):
        self.algorithm = StringVar()
        Label(self, text="Algorithm: ", bg='snow3').grid(row=0, column=0, padx=5, pady=5, sticky=W)
        self.algMenu = ttk.Combobox(self, textvariable=self.algorithm, values=['Bubble Sort', 'Merge Sort'])
        self.algMenu.grid(row=0, column=1, padx=5, pady=5)
        self.algMenu.current(0)
    
    def _add_size_scale(self):
        self.size = IntVar()
        Label(self, text="Select Size", bg='snow3').grid(row=0, column=3, padx=5, pady=5, sticky=E)
        Scale(self, from_=5, to=30, bg='snow3', variable=self.size, orient=HORIZONTAL, length=200, command=self.resize_array).grid(row=0, column=4, padx=5, pady=5, sticky=E)
    def _add_sort_button(self):
        Button(self, text="Sort", command=self.shuffle, bg='snow3').grid(row=1, column=0, padx=5, pady=5, sticky=W)
    def _add_randomize_button(self):
        Button(self, text="Shuffle", command=self.shuffle, bg='snow3').grid(row=1, column=4, padx=5, pady=5, sticky=E)
        
    def _init_data_visualizer(self):
        self.data_visualizer = Data_Visualizer(self.parent, self.size.get())
        
    def get_algorithm(self):
        return self.algorithm.get()
    
    def resize_array(self, value):
        self.data_visualizer.set_array(int(value))
        self.data_visualizer.visualize()
        
    def shuffle(self):
        self.data_visualizer.shuffle_array()
        self.data_visualizer.visualize()