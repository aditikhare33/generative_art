cols = 0
rows = 0
scl = 17 #scale variable
terrain = [[]]
w = 1500
h = 900
flying = 0
img = 0

def setup():
    background(255)
    
    global cols
    global rows 
    global terrain
    global w 
    global h
    global img 
    
    img = loadImage("water.png")
    print(img)
    
    size(1000, 600, P3D)
    cols = int(w*1.5)/ scl
    rows = h / scl
    terrain = [[0 for x in range(w)] for y in range(h)] 
    frameRate(8)
    #colorMode(HSB, 359, 100, 100)
    #file = new SoundFile("wind-1.mp3");
    #file.play();
    
def draw():
    #camera(width/2, height/2, 300, width/2, height/2, 0, 0, 1, 0);
    #pointLight(0, 0, 255, width/2, height/2, -200);
    global terrain
    global flying

    strokeWeight(4)
    background(255) #background(0, 0, 100)
    
    push()
    translate(width/2, height/2)
    rotateX(PI/3)
    translate(-int(w*1.5)/2, -h/2)
    
    #stroke(0, 0, 255)
    noStroke()
    colorMode(HSB, 255)
    pointLight(190, 255, 255, width, height, width/2);
    pointLight(50, 255, 100, mouseX, height, mouseY);
    colorMode(RGB)
    draw_terrain()
    pop()
    
    filter(POSTERIZE, 7)
    push()
    fill(0)
    str_ = "y-coord:" + str(mouseY)
    text(str_, w/10, h/10)
    str_ = "x-coord:" + str(mouseX)
    text(str_, w/10, 1.2*h/10)
    pop()
    #flying -= 0.1
    #directionalLight(51, 102, 126, 0, -1, 0);
    
xoff = 0

def draw_terrain():
    global xoff  
    for y in range(0, rows):
        yoff = 0
        for x in range(0, cols):
            terrain[x][y] = map(noise(xoff, yoff), 0, 1, -50, 50)
            yoff += 0.07
        xoff += 0.07
    for y in range(0, rows):
        beginShape(TRIANGLE_STRIP) #triangular mesh 
        texture(img)
        for x in range(0, cols):
            vertex(x*scl, y*scl, terrain[x][y])
            vertex(x*scl, (y+1)*scl, terrain[x][y+1])
        endShape()
