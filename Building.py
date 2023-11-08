from calc import get_corners

DIFF = 50

class Building:
    def __init__(self, canvas, x, y) -> None:
        self.fill_color = "blue"
        self.x = x
        self.y = y
        self.corners = get_corners(self, DIFF)
   #     self.furthest_DIFF = furthest_DIFF(self)
        canvas.create_rectangle(x-DIFF, y-DIFF, x + DIFF,y + DIFF, fill=self.fill_color, outline="")
    
    def redraw(self, canvas):
        canvas.create_rectangle(self.x-DIFF, self.y-DIFF, self.x + DIFF,self.y + DIFF , fill=self.fill_color, outline="")