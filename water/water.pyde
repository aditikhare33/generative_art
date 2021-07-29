cols = 0
rows = 0
scl = 30 #scale variable
water = [[]]
w = 1500
h = 900
img = 0
incr = 0

def setup():
    background(255)
    
    global cols
    global rows 
    global water
    global w 
    global h
    global img 
    
    img = loadImage("water.png")
    print(img)
    
    size(1000, 600, P3D)
    cols = int(w*1.5)/ scl
    rows = h / scl
    water = [[0 for x in range(w)] for y in range(h)] 

    frameRate(7)
    
def draw():
    #camera(width/2, height/2, 300, width/2, height/2, 0, 0, 1, 0);
    #pointLight(0, 0, 255, width/2, height/2, -200);
    global water
    global incr

    strokeWeight(4)
    background(0) #background(0, 0, 100)
    colorMode(HSB)
    
    push()
    filter(POSTERIZE, 7)
    translate(width/2, height/2)
    rotateX(PI/3)
    rotateY(sin(xoff)/30)
    translate(-int(w*1.5)/2, -h/2)
    
    #stroke(0, 0, 255)
    noStroke()
    colorMode(HSB)
    pointLight(200, 100, 100, width, height, width/2);
    pointLight(100, 100, 140, mouseX, height, mouseY);
    pointLight(40, 100, 140, mouseY, height, mouseX);
    
    colorMode(RGB)
    draw_water()
    pop()
    

    push()
    fill(0)
    str_ = "light y-coord:" + str(mouseY)
    text(str_, w/10, h/10)
    str_ = "light x-coord:" + str(mouseX)
    text(str_, w/10, 1.2*h/10)
    pop()
    directionalLight(51, 102, 12, 0, height, 0);
    incr += 0.01
    
    #saveFrame("output/pic_#####.png")
    
xoff = 0f

def draw_water(): 
    global xoff
    for y in range(0, rows):
        yoff = 0
        for x in range(0, cols):
            water[x][y] = map(noise(xoff, sin(yoff) + xoff), 0, 1, -100, 100)
            yoff += (sin(xoff)*0.001 + 0.1) * scl /30
        xoff += 0.1 * scl / 30
    for y in range(0, rows):
        beginShape(TRIANGLE_STRIP) #triangular mesh 
        texture(img)
        for x in range(0, cols):
            vertex(x*scl, y*scl, water[x][y])
            vertex(x*scl, (y+1)*scl, water[x][y+1])
        endShape()
