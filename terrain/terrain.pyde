cols = 0
rows = 0
scl = 20 #scale variable
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
    cols = w / scl
    rows = h / scl
    yoff = 0 # y off set
    terrain = [[0 for x in range(w)] for y in range(h)] 
    frameRate(30)
    colorMode(HSB, 359, 100, 100)
    #file = new SoundFile("wind-1.mp3");
    #file.play();
    
def draw():
    camera(width/2, height/2, 300, width/2, height/2, 0, 0, 1, 0);
    pointLight(200, 200, 200, width/2, height/2, -200);
    global terrain
    global flying

    strokeWeight(4)
    background(354, 90, 100)
    
    translate(width/2, height/2) # draw everything relative to the center of the window
    rotateX(PI/3)
    translate(-w/2, -h/2)
    
    stroke(233, 76, 100)
    #fill(255)
    draw_terrain()
    flying -= 0.1
    directionalLight(51, 102, 126, 0, -1, 0);
    #noFill()
    #stroke(210, 30, 100)
    #draw_terrain()
    #filter(BLUR, 3)
    #filter(POSTERIZE, 2)
    #saveFrame("output/terrain_####.png")
    

def draw_terrain():
    yoff = flying # y off set
    for y in range(0, rows):
        xoff = 0
        for x in range(0, cols):
            terrain[x][y] = map(noise(xoff, yoff), 0, 1, -250, 250)
            xoff += 0.1
        yoff += 0.1
    
    for y in range(0, rows):
        beginShape(TRIANGLE_STRIP) #triangular mesh 
        texture(img)
        for x in range(0, cols):
            vertex(x*scl, y*scl, terrain[x][y])
            vertex(x*scl, (y+1)*scl, terrain[x][y+1])
        endShape()
            
    
            
