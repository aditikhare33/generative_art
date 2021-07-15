class Droplet {
  constructor(x, y, z) {
    this.size = 10;
    this.x = x;
    this.y = y;
    this.vel = 0;
  }

  increase_size() {
    this.size += 1;
  }

  show() {
    push();
    translate(this.x - w/2, this.y - h/2);
    normalMaterial();
    sphere(this.size); 
    pop();
  }
  fall() {
    this.vel += 5;
    this.y += this.vel;
    this.size += 10;
    return !(this.y > h);
  }
};

//water mesh global vars
var scl = 40.0;
var w, h, cols, rows;
var t = 0.0;

function setup() {
  w = windowWidth;
  h = windowHeight;
  createCanvas(w, h, WEBGL);

  //w *= 1.9;
  cols = w / scl;
  rows = h / scl;
  //hint(ENABLE_DEPTH_SORT);
  background(50);
  angleMode(RADIANS);
  frameRate(15);
}

var droplets = [];

function draw() {
  background(0);
  
  if (mouseIsPressed) {
    let new_droplet = new Droplet(mouseX, mouseY, 0);
    droplets.push(new_droplet);
  }
  droplets.forEach(update);
  //draw_box();
  //style_mesh();
  //draw_mesh();
  //t += 0.3;
}

function update(value, index, array) {
  value.show();
  if (!value.fall()) {
    array.splice(index, 1);
  }
}

function lights() {
  
}

function draw_box() {
  noFill();
  stroke(255);
  rotateY(0.4);
  rotateX(-0.1);
  box(h/2);
}

function c_noise(t1, t2) {
  return map(noise(t1, t2), 0, 1, -75, 75);
}

function style_mesh() {
  rotateX(1.1);
  translate(-w/2, -h/2, -h/4);

  noFill();
  stroke(255);
 //ambientMaterial();
}

function draw_mesh() {
  var xoff = t, yoff = t;
  for(let j = 0; j < rows; j++) {
    xoff = t;
    beginShape(TRIANGLE_STRIP);
    for(let i = 0; i < cols; i++) {
      vertex(i*scl, j*scl, c_noise(xoff, yoff));
      vertex(i*scl, (j+1)*scl, c_noise(xoff, yoff + 0.1));
      xoff += 0.1;
    }
    yoff += 0.1;
    endShape();
  }  
}

/* STEPS: 
  make 3D 
  create 3D rectangle mesh
  create 3D triangle mesh
  make them move around from noise
  
  add skin 
  add lighting
*/
