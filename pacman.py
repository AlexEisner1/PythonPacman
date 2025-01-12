from directions import Directions
class Pacman:

    def __init__(self, x, y, width, height, maxH, minH, maxW, minW, direction, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.maxH = maxH
        self.maxW = maxW
        self.minH = minH
        self.minW = minW
        self.direction = direction
    def move(self, direction):
        if direction == "left":
            if self.x > self.minW + self.width:
                self.x -= self.speed
        elif direction == "right":
            if self.x < self.maxW - self.width:
                self.x += self.speed
        elif direction == "up":
            if self.y > self.minH + self.height:   
                self.y -= self.speed
        elif direction == "down":
            if self.y < self.maxH - self.height:
                self.y += self.speed
    def set_direction(self, direction):
        self.direction = direction
        
    def update(self):
        if self.direction == Directions.LEFT:
            if self.x > self.minW + self.width:
                self.x -= self.speed
        elif self.direction == Directions.RIGHT:
            if self.x < self.maxW - self.width:
                self.x += self.speed
        elif self.direction == Directions.UP:
            if self.y > self.minH + self.height:   
                self.y -= self.speed
        elif self.direction == Directions.DOWN:
            if self.y < self.maxH - self.height:
                self.y += self.speed