w = 800
h = 800

blue = "#1380FF"
yellow = "#F8E500"
red = "#F40000"
green = "#2ABA00"
colors = [blue, red, green, yellow]
#curr_color = colors[int(random(0, len(colors)))]
curr_color = 255
incr = 0.1
recent_window = 3.0/incr
bgColor = 255

def setup():
    size(w, h)
    background(bgColor)
    
t_x = random(0, 100)
t_y = random(0, 100)
recents = []

def draw():
    global t_x, t_y, recents
    #background(255)

    thickness = map(noise(t_x, t_y), 0, 1, 5, 5)
    strokeWeight(thickness)
    
    x = map(noise(t_x), 0, 1, 0, w)
    y = map(noise(t_y), 0, 1, 0, h)
    
    recents.append({'x': x, 'y':y, 'th': thickness, 'col': curr_color})
    
    if (len(recents) == 1):
        point(x, y)
        point(y, x)
    else:
        if len(recents) > recent_window*25:
            recents.pop(0)
        else:
            show_recents()
            
    t_x += incr
    t_y += incr
    
    #change_color()

def keyPressed():
    if keyCode == 32:
        saveFrame("output/pic_########.png")
        show_recents()
    
def change_color():
    global curr_color
    chance = int(random(0, 100))
    
    if chance == 1:
        curr_color = colors[int(random(0, len(colors)))]

def show_recents():
    background(bgColor)
    scl = 5.0
    for row in range(0, int(scl)):
        for col in range(0, int(scl)):
            push()
            translate(w/scl*col, h/scl*row)
            rotate(PI/4.0)
            translate(w/18, -h/10)
            stroke(colors[int(row*scl+col)%len(colors)])
            
            shift_upper = (row*scl + col + 1) * recent_window 
            shift_lower = (row*scl + col) * recent_window
            
            for i, item in enumerate(recents):
                if (i >= 4 and i <= shift_upper and i >= shift_lower):
                    #stroke(item['col'])
                    strokeWeight(item['th']/scl)
                    
                    p_item = recents[i-1]
                    p2_item = recents[i-4]
                    noFill()
                    curve(p2_item['x']/scl, p2_item['y']/scl, p_item['y']/scl, p_item['x']/scl, p_item['x']/scl, p_item['y']/scl, item['y']/scl, item['x']/scl)
                    #line(item['x']/scl, item['y']/scl, item['y']/scl, item['x']/scl)
                    #line(p_item['x']/scl, p_item['y']/scl, item['y']/scl, item['x']/scl)
                    line(p_item['x']/scl, p_item['y']/scl, item['x']/scl, item['y']/scl)
                    line(p_item['y']/scl, p_item['x']/scl, item['y']/scl, item['x']/scl)
            pop()
    if len(recents) >= recent_window*25:
        fill(0)
        text("PRESS SPACE FOR NEW OBJECTS", w/2.5 , h/20)
