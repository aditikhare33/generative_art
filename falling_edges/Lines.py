class Star():
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.x = random(0, width)
        self.y = random(0, height)
        self.px = self.x
        self.py = self.y
        self.z = width
        self.velocity = random(4, 10)
    
    def update(self):
        self.py = self.y
        self.y += self.velocity
        if self.y > height:
            self.y = random(-200, -100)
            self.x = random(0, width)
    
    def show(self):
        fill(255)
        noStroke()
        ellipse(self.x, self.y, self.px, self.py)
        
        
