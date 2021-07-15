class Particle():
    def __init__(self, width, height):
        r = (height+width)/2 #ratio
        self.winHeight = height
        self.winWidth = width
        self.size = random(0, r/15)
        self.x = random(0, self.winWidth)
        self.y = random(0, self.winHeight)
        self.vel = PVector(random(r/-100, r/100), random(r/-100, r/100))
        self.color = color(random(0, 255), 255, 255)
        
    def show(self):
        stroke(0)
        #fill(self.color)
        strokeWeight(self.size)
        circle(self.x, self.y, self.size)
        #tint(255, 128)
        
    def update(self):
        self.x += self.vel.x
        self.y += self.vel.y
    
    def pos(self):
        return {"x": self.x, "y": self.y}
        
    def join(self, particle2): #inelastic_collide
        #self.mix_colors(particle2)
        self.size += particle2.size
        del particle2
        
    def mix_colors(self, particle2):
        amt = (self.size + 0.0) / (self.size + particle2.size)
        pcolor = self.color
        self.color = lerpColor(self.color, particle2.color, 0.5)
    
    def edges(self):
        # bounce off walls and have lower magnitude of velocity
        if self.y >= self.winHeight or self.y <= 0 or self.x >= self.winWidth or self.x <= 0:
            p_vel_x = -1 * self.vel.x #* 0.8
            self.vel.x = self.vel.y #* 0.8
            self.vel.y = p_vel_x
            
            self.update()
            
        
        
    
    
