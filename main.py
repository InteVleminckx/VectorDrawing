import pygame as pygame
import sys
import math

PI = 3.14159265359

pygame.init()
WINDOW = pygame.display.set_mode((700, 700))
CLOCK = pygame.time.Clock()
POINTS = []

class Vector:

    def __init__(self, rotspeed, length, prev=None, start=None):
        self.prevVector = prev
        self.rotationPos = self.prevVector.endpoint if prev is not None else start
        self.endpoint = self.rotationPos[0] + length, self.rotationPos[1]
        self.color = (122,122,122)
        self.rotSpeed = rotspeed
        self.angle = 270
        self.length = length
        self.isLast = False

    def draw(self):
        pygame.draw.line(WINDOW, self.color, self.rotationPos, self.endpoint, 2)

    def rotate(self):

        if self.prevVector is not None:
            self.rotationPos = self.prevVector.endpoint

        sX = self.rotationPos[0]
        sY = self.rotationPos[1]

        self.angle = (self.angle + self.rotSpeed) %360

        eX = (sX) + math.cos((self.angle * PI)/180) * self.length
        eY = (sY) + math.sin((self.angle * PI)/180) * self.length

        self.endpoint = eX, eY

        if self.isLast and len(POINTS) < 360:
            POINTS.append((int(eX), int(eY)))


def drawPoints():


    colors = [
        (148,0,211),
        (75,0,130),
        (0,0,255),
        (0,255,0),
        (255,255,0),
        (255,127,0),
        (255,0,0)
    ]

    for i, point in enumerate(POINTS):

        WINDOW.set_at(point, colors[i%7])
        WINDOW.set_at((point[0]+1, point[1]+1), colors[i%7])
        WINDOW.set_at((point[0]-1, point[1]-1), colors[i%7])
        WINDOW.set_at((point[0]+1, point[1]-1), colors[i%7])
        WINDOW.set_at((point[0]-1, point[1]+1), colors[i%7])

if __name__ == '__main__':


    vectors = {
        1: [80,-2],
        2: [60,-4],
        3: [40, -6],
        4: [20, -10],
        5: [15, 12],
        6: [10, 14],
        7: [8, 16],
        8: [6, 18],
        9: [4, 20],
    }

    vec1 = Vector(start=(350,450), length=100, rotspeed=2)

    vectorsList = [vec1]

    for i in vectors:
        prev = vectorsList[len(vectorsList)-1]
        length = vectors[i][0]
        speed = vectors[i][1]

        vectorsList.append(Vector(rotspeed=speed, length=length, prev=prev))

    vectorsList[len(vectorsList) - 1].isLast = True

    while True:  # Pygame main game loop:
        for event in pygame.event.get():  # Quit game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        WINDOW.fill((0, 0, 0))

        for vec in vectorsList:
            vec.rotate()
            vec.draw()

        drawPoints()
        pygame.display.update()
        CLOCK.tick(60)
