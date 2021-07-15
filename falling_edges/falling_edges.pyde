from Lines import *

lines = []

def setup():
    global lines
    size(400, 400)
    lines = [Star(height, width) for i in range(0, 250)]

def draw():
    background(20)
    for line in lines:
        line.update()
        line.show()
        
