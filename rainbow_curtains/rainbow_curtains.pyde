def setup():
    size(300, 300)
    background(0)
    colorMode(HSB)
    
t1 = random(0, 10)
t2 = random(0, 10)
t3 = 0
def draw():
    global t1
    global t2
    global t3
    
    x = map(noise(t1), 0, 1, 0, 1.5*width)
    y = map(noise(t2), 0, 1, 0, 1.5*height)
    stroke(t3, 255, 255)
    line(0, 0, x, y)
    
    t1 += 0.004
    t2 += 0.004
    t3 = 0 if t3 > 255 else t3 + 1
    
