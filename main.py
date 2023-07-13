from tkinter import *
import time
import json


class GUI():
    def __init__(self):
        self.root = Tk()
        self.root.geometry('1280x720')
        self.root.resizable(False, False)

        self.canvas = Canvas(self.root, width=768, height=640, bg='red')
        self.canvas.place(x=472, y=40)

        self.code_field = Text(self.root, width=43, height=35)
        self.code_field.place(x=40, y=40)

        self.run_code_button = Button(
            self.root, text='Run Code', width=23, height=4,)
        self.run_code_button.place(x=40, y=635)

        self.field = Field(self)

    def mainloop(self):
        self.root.mainloop()


class Coords:
    def __init__(self, x1=0, y1=0, x2=64, y2=64):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


class Sprite:
    def __init__(self,  col, row, image, gui: GUI):
        self.col = col
        self.row = row
        self.x = row * 64
        self.y = col * 64
        self.image = PhotoImage(file=image)
        self.gui = gui
        self.coordinates = Coords(self.x, self.y, self.x + 64, self.y + 64)
        self.create_sprite()

    def create_sprite(self):
        self.id = self.gui.canvas.create_image(
            self.x, self.y, image=self.image, anchor='nw')

    def coords(self):
        return self.coordinates


class Block(Sprite):
    def __init__(self, col, row, image, gui: GUI):
        super().__init__(col, row, image, gui)


class LowerLayer():
    def __init__(self, gui: GUI):
        # Вскрываем файл map.txt -> и создаем объекты на canvas
        self.gui = gui
        self.id = self.gui.canvas.create_rectangle(
            20, 20, 200, 200, fill='blue')
        pass


class UpperLayer():
    def __init__(self, gui: GUI):
        # Вскрываем файл map.txt -> и создаем объекты на canvas
        self.gui = gui
        self.id = self.gui.canvas.create_rectangle(
            50, 50, 250, 250, fill='green')
        pass


class Field:
    def __init__(self, gui: GUI):
        self.gui = gui
        self.data = []

        self.data.append(LowerLayer(self.gui))
        self.data.append(UpperLayer(self.gui))


app = GUI()
app.mainloop()
'''b0 = Block(0, 0, image='textures/al1.png', gui=g)
b1 = Block(0, 1, image='textures/al1.png', gui=g)
b2 = Block(0, 2, image='textures/al1.png', gui=g)
b3 = Block(1, 0, image='textures/al1.png', gui=g)
b4 = Block(1, 1, image='textures/al1.png', gui=g)
b5 = Block(1, 2, image='textures/al1.png', gui=g)
b6 = Block(2, 0, image='textures/al1.png', gui=g)
b7 = Block(2, 1, image='textures/al1.png', gui=g)
b8 = Block(2, 2, image='textures/al1.png', gui=g)
l1 = Layer(map=[[b0, b1, b2],
                [b3, b4, b5],
                [b6, b7, b8],])
'''
