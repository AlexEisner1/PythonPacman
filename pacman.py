class Pacman:
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
    def move(self, direction):
        if direction == "left":
            self.x -= self.speed
        if direction == "right":
            self.x += self.speed
        if direction == "up":
            self.y -= self.speed
        if direction == "down":
            self.y += self.speed