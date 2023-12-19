from typing import Any
from point import Point
from vector2 import vector2

def intersect(building_a, building_b) -> bool:
    # Check if the two buildings intersect in the x-axis
    for c in building_b.corners:
        x_intersect = building_a.corners[0].x <= c.x <= building_a.corners[1].x
        y_intersect = building_a.corners[1].y <= c.y <= building_a.corners[2].y
        if y_intersect and x_intersect:
            print(building_a.corners, building_b.corners)
            return True
    # If there's an overlap in both x and y dimensions, the buildings intersect
    return False

class shape2:
    def __init__(self, a, b, sp = Point(0, 0), skalar_a = 1, skalar_b = 1) -> None:
        self.a = a
        self.vector_a = vector2(a * skalar_a)
        self.b = b
        self.vector_b = vector2(b * skalar_b)
        self.sp = sp

    def __repr__(self) -> str:
        print(f"E: x-> = {self.sp} + {self.skalar_a} * {self.a} + {self.skalar_b} * {self.b}")

def punktprobe(point, area):
    #area needs to be defined by a 2 dimensional vector area. Meaning: 2 Spannvektoren, ein Stützvektor
    
    pass

def intersect2(b, bb, DIFF = 50) -> bool:
    a = vector2(b.corners[0], b.corners[1])
    b = vector2(b.corners[0], b.corners[3])
    sp = vector2(b.corners[0])
    area = square2(a, b, sp)
    for c in bb.corners:
        punktprobe(c, area)



def get_corners(building, DIFF = 50) -> Point:
    points = []
    points.append(Point(building.x - DIFF, building.y + DIFF))
    points.append(Point(building.x + DIFF, building.y + DIFF))
    points.append(Point(building.x + DIFF, building.y - DIFF))
    points.append(Point(building.x - DIFF, building.y - DIFF))
    return points
