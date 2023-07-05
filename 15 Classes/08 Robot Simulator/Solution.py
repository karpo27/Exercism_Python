# Globals for the directions
# Change the values as you see fit
EAST = "E"
NORTH = "N"
WEST = "W"
SOUTH = "S"


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.coordinates = x_pos, y_pos

    def move(self, commands):
        directions = {
            NORTH: {'R': EAST, 'L': WEST, 'A': (0, 1)},
            SOUTH: {'R': WEST, 'L': EAST, 'A': (0, -1)},
            EAST: {'R': SOUTH, 'L': NORTH, 'A': (1, 0)},
            WEST: {'R': NORTH, 'L': SOUTH, 'A': (-1, 0)}
        }
        for command in commands:
            print(self.direction, self.coordinates)
            if command in ['R', 'L']:
                self.direction = directions[self.direction][command]
            else:
                self.coordinates = tuple(a + b for a, b in zip(self.coordinates, directions[self.direction][command]))
