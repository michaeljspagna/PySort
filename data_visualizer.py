from tkinter import *
from tkinter import ttk
import random

class Data_Visualizer(Canvas):
    
    CANVAS_WIDTH = 900
    CANVAS_HEIGHT = 400
    RECTANGLE_HEIGHT = 340
    RECTANGLE_SPACING = 10
    RECTANGLE_OFFSET = 15
    
    def __init__(self, parent, init_size):
        Canvas.__init__(self, parent, width=self.CANVAS_WIDTH, height=self.CANVAS_HEIGHT, bg='white')
        self.parent = parent
        self.grid(row=1, column=0, padx=10, pady=80)
        self.set_array(init_size)
        self.visualize(["#363636" for x in self.array])

    def visualize(self, color_arrray):
        self.delete("all")
        self.normalize_array()
        rectangle_width = self.CANVAS_WIDTH / (len(self.normalized_array) + 1)
        for index, height in enumerate(self.normalized_array):
            x1, y1 = self._get_top_left_cord(index, height, rectangle_width)
            x2, y2 = self._get_bottom_right_coord(index, rectangle_width)
            self.create_rectangle(x1, y1, x2, y2, fill=color_arrray[index])
            self.create_text(x1 + (rectangle_width / 3), y1, anchor=SW, text=str(self.array[index]), font=("Purisa", int(rectangle_width/3)))
        self.parent.update()
        
    def set_array(self, size):
        self.array = list(range(1, size + 1))
        self.normalize_array()
        
    def normalize_array(self):
        self.normalized_array = [ i / max(self.array) for i in self.array]
        
    def shuffle_array(self):
        random.shuffle(self.array)
        self.normalize_array()
        
    def _get_top_left_cord(self, index, height, rectangle_width):
        x = (index * rectangle_width) + self.RECTANGLE_OFFSET + self.RECTANGLE_SPACING
        y = self.CANVAS_HEIGHT - (height * self.RECTANGLE_HEIGHT)
        return (x,y)
        
    def _get_bottom_right_coord(self, index, rectangle_width):
        x = (index + 1) * rectangle_width + self.RECTANGLE_OFFSET
        y = self.CANVAS_HEIGHT
        return (x,y)
    
    