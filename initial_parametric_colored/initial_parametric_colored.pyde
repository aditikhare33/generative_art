t = 0.0
t2 = 50
t2_minus_mode = False
HEIGHT = 500
WIDTH = 500

def setup():
    background(20)
    size(HEIGHT, WIDTH)
    
def draw():
    global t
    global t2
    
    background(20)
    
    translate(HEIGHT/2, WIDTH/2)
    
    #stroke(abs(t2*sin(t2) + 150), abs((255 - t2)*sin(t2 + 0.5) + 150), abs(t2*sin(t2 + 0.75) + 150))
    #print(abs(t2*sin(t2) + 100), abs((255 - t2)*sin(t2 + 0.5) + 100), abs(t2*sin(t2 + 0.75) + 100))
    stroke(255)
    strokeWeight(5)
    
    circle(y2(t), y1(t), 6)
    #point(x2(t), y2(t))
    
    #t = (t + 0.1) if t < 100 else 0
    for i in range(0,10):
        j = i * 0.01
        #stroke
        stroke(255)
        line(x1(t + j), y1(t + j), x2(t + j), y2(t + j))
        
        stroke(255, 150, 150)
        t += 5
        line(x1(t + j), y1(t + j), x2(t + j), y2(t + j))
        t -=5
        #stroke(abs(t2*sin(t2) + 150), abs((255 - t2)*sin(t2 + 0.5) + 150), abs(t2*sin(t2 + 0.75) + 150))

        handle_color_change()
        
    t += 0.001

def handle_color_change():
    global t2_minus_mode
    global t2
    
    if t2 > 253:
        t2_minus_mode = True
    elif t2 < 50:
        t2_minus_mode = False
    
    if t2_minus_mode:
        t2 -= 0.1
    else:
        t2 += 0.1
    
def x1(t):
    #return 40 * cos(t)
    return 80 * (cos(16*t) + cos(6*t)/2 + sin(10*t)/3)

def y1(t):
    #return 40 * sin(t)
    return 80 * (sin(16*t) + sin(6*t)/2 + cos(10*t)/3)
    
def x2(t):
    return 80 * cos(t)
    #return 40 * (2*cos(t) + sin(2*t)*cos(60*t))
    
def y2(t):
    return 80 * sin(t)
    #return 40 * (sin(2*t) + sin(60*t))
