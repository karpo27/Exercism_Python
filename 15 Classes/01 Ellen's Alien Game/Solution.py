class Alien:
    total_aliens_created = 0
    
    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3
        Alien.total_aliens_created += 1
        
    def hit(self):
        self.health -= 1

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def teleport(self, new_x_coordinate, new_y_coordinate):
        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate

    def collision_detection(self, other_object):
        pass


def new_aliens_collection(*args):
    result = []
    for i in range(len(args)):
        for j in range(len(args[i])):
            result.append(Alien(args[i][j][0], args[i][j][1]))

    return result
    
