from point import Point

class Kara:
    def __init__(self, position = (0, 0)):
        self.position = position
        self.orientation = "Forwards"
    
    def move(self):
        match self.orientation:
            case "Forwards":
                self.position = (1, 0)


kara = Kara()
kara.move()
print(kara)


name = "Kara"
position = (0, 0)
orientation = "Forwards"


kara_position = (0, 0)
kara_orientation = "Forwards"
def kara_move():
    kara_position += (1, 0)

kara2_position = (0, 0)
kara2_orientation = "Forwards"
def kara2_move():
    kara2_position += (1, 0)

kara3_position = (0, 0)
kara3_orientation = "Forwards"
def kara3_move():
    kara3_position += (1, 0)
