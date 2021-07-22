from particle import Particle

w = 500
h = 500
NUM_PARTICLES = ((w + h)/10)
particles = []
t = 0.0

def setup():
    global particles 
    size(w, h)
    colorMode(HSB)
    particles = [Particle(width, height) for i in range(0, NUM_PARTICLES)]
  
  
def keyPressed():
    global particles
    if key: #reset
        particles = [Particle(width, height) for i in range(0, NUM_PARTICLES)]
    
    
def draw():
    global t
    background(255)
    
    for particle in particles:
        particle.update()
        for particle2 in particles:
            if particle.pos == particle2.pos:
                probability = random(-100000,100)
                if int(probability) + particle.size + particle2.size > 1: 
                    particle.join(particle2)
        particle.edges()
        particle.show()
    filter(BLUR, 4)
    filter(POSTERIZE, 4)
    
    t += 0.01
    
    text("PRESS SPACE TO RESTART THE SIMULATION WITH NEW PARTICLES", w/10, h/16)
    
