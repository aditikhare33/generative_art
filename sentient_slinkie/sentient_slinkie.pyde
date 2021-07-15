def setup():
    size(500, 300)
    background(0)
    colorMode(HSB)

t1 = random(0, 10)
t2 = random(0, 10)
t3 = 0
t4 = 100

def draw():
    global t1
    global t2
    global t3
    global t4
    
    fill(color(t3, 255, 255))
    #noStroke()
    x = map(noise(t1), 0, 1, -.5*width, 1.5*width)
    y = map(noise(t2), 0, 1, -.5*height, 1.5*height)
    ellipse(x, y, width/15, width/15)#30*(sin(t4) + 1) + 50, 30*(sin(t4) + 1) + 50)
    
    #fill(color(t4, 255, 255))
    #ellipse(y, x, width/20, width/20)
            
    t1 +=  0.008
    t2 += 0.008
    t3 = 0 if t3 > 255 else t3 + 1
    #t4 = 0 if t4 > 255 else t4 + 1.2
    
    #saveFrame("output/line-######.png");
    
