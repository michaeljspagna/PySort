from tkinter import *
from tkinter import ttk
import random
from control_frame import Control_Frame
from data_visualizer import Data_Visualizer
root = Tk()
root.title('Sorting Algorithm Visualisation')
root.geometry('900x600')
root.config()
control_frame = Control_Frame(root)
root.mainloop()