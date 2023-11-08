from point import Point

# uses pythagorean theorem to findd the diagonal length of the square, so that the longest distance, in which another point could intercept, can be found.
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

def get_corners(building, DIFF = 50) -> Point:
    points = []
    points.append(Point(building.x - DIFF, building.y + DIFF))
    points.append(Point(building.x + DIFF, building.y + DIFF))
    points.append(Point(building.x + DIFF, building.y - DIFF))
    points.append(Point(building.x - DIFF, building.y - DIFF))
    return points
