import tkinter as Tk

from random import randint

from distance import distance


canvas_width = 800
canvas_height = 480

master = Tk.Tk()

w = Tk.Canvas(master,
           width=canvas_width,
           height=canvas_height)
w.pack()

def circle(canvas, center_x, center_y, radius):
    return canvas.create_oval(
        center_x-radius,
        center_y-radius,
        center_x+radius,
        center_y+radius
    )

name = circle(w, 100, 100, 50)


class MoveArround(object):
    def __init__(self, canvas, tag_or_id, radius):
        self.canvas = canvas
        self.tag_or_id = tag_or_id
        self.radius = radius

    # top left
    def coords_left(self):
        return (
            self.canvas.coords(self.tag_or_id)[0],
            self.canvas.coords(self.tag_or_id)[1]
        )

    # top right
    def coords_right(self):
        return (
            self.canvas.coords(self.tag_or_id)[2],
            self.canvas.coords(self.tag_or_id)[3]
        )

    def animate_to(self, x, y):
        distance_to_left = distance(self.coords_left, (x, y))
        distance_to_right = distance(self.coords_right, (x, y))
        while True:
            pass


if __name__ == '__main__':
    master.mainloop()
