def setup():
  size(1450, 1000)
  
def draw():
    if  mousePressed:
        fill(0)
    else:
        fill(255)
    rect(mouseX, mouseY, 200, 200)
    rect(mouseY, mouseX, 100, 100)
