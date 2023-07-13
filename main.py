from tkinter import *
import time


class GUI():
    def __init__(self):
        self.root = Tk()
        self.root.geometry('1280x720')
        # self.root.resizable(False, False)

        self.canvas = Canvas(self.root, width=768, height=640, bg='red')
        self.canvas.place(x=472, y=40)

        self.code_field = Text(self.root, width=43, height=35)
        self.code_field.place(x=40, y=40)

        self.run_code_button = Button(
            self.root, text='Run Code', width=23, height=4,)
        self.run_code_button.place(x=40, y=635)


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


class Layer():
    def __init__(self, map: list[list[Block]]):
        self.map = map


class Field:
    def __init__(self, gui: GUI, data: list[Layer]):
        self.gui = gui
        self.data = data
        self.blocks: list[list[Block]] = []


g = GUI()
b0 = Block(0, 0, image='textures/al1.png', gui=g)
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

g.root.mainloop()
