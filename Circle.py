import turtle as t

class Circle:
    def __init__(self, x=0, y=0, radius=15, strokecolor='black', 
                 fillcolor='white', tag='unfilled'):
        self.pen = t.getpen()
        self.x = x
        self.y = y
        self.radius = radius
        self.strokecolor = strokecolor
        self.fillcolor = fillcolor
        self.tag = tag

    def draw(self):
        self.pen.speed(0)
        self.pen.penup()
        self.pen.goto(self.x, self.y - self.radius)
        self.pen.pendown()
        self.pen.color(self.strokecolor, self.fillcolor)
        self.pen.begin_fill()
        self.pen.circle(self.radius)
        self.pen.end_fill()
        self.pen.penup()

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y

    def get_color(self):
        return self.fillcolor

    def set_color(self, new_color):
        self.fillcolor = new_color

    def get_tag(self):
        return self.tag

    def set_tag(self, new_tag):
        self.tag = new_tag

    def is_clicked(self, x, y):
        clicked = False
        if self.x - self.radius < x < self.x + self.radius and \
          self.y - self.radius < y < self.y + self.radius:
            clicked = True
            return clicked
        else:
            return clicked