//const { push, pop } = require("core-js/core/array");

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
  w = 800;
  h = 800;
  createCanvas(w, h, WEBGL);

  cols = (w*2) / scl;
  rows = h / scl;
  background(50);
  angleMode(RADIANS);
  frameRate(8);
}

var droplets = [];

function draw() {
  background(255);
  
  /*if (mouseIsPressed) {
    let new_droplet = new Droplet(mouseX, mouseY, 0);
    droplets.push(new_droplet);
  }
  droplets.forEach(update); */
  //draw_box();
  lights();
  style_mesh();
  draw_mesh();
  rotateX(t);

  

  textFont('Georgia');
  text(mouseY, w/10, h/10);

  t += 0.1;
}

function update(value, index, array) {
  value.show();
  if (!value.fall()) {
    array.splice(index, 1);
  }
}

function lights() {
  let width = w;
  let height = h;
  pointLight(200, 100, 100, width, height, width/2);
  pointLight(140, 100, 140, mouseX, height, mouseY);
  pointLight(50, 100, 140, mouseY, height, mouseX);
}

function draw_box() {
  push();
  noFill();
  stroke(255);
  rotateY(0.4);
  rotateX(-0.1);
  box(h/2);
  pop();
}

function c_noise(t1, t2) {
  return map(noise(t1, t2), 0, 1, -105, 105);
}

function style_mesh() {
  rotateX(1.1);
  translate(-(2*w)/2, -h/2, -h/4);

  noFill();
  //fill(0, 255, 255);
  noStroke()
  stroke(0);
}

var xoff = 0;
function draw_mesh() {
  let water = [];
  for (let x = 0; x < cols; x++) {
      water[x] = [];
    for (let y = 0; y < rows; y++) {
      water[x][y] = 0;
    }
  }

  for (let y = 0; y < rows; y++) {
    let yoff = 0;
    for (let x = 0; x < cols; x++) {
      water[x][y] = map(noise(xoff, sin(yoff) + xoff), 0, 1, -150, 150);
      yoff += (sin(xoff)*0.001 + 0.1) * scl /30;
    }
    xoff += 0.1 * scl / 30;
  }

  for (let y = 0; y < rows; y++) { 
    beginShape(TRIANGLE_STRIP);
    for (let x = 0; x < cols; x++) {
      vertex(x*scl, y*scl, water[x][y])
      vertex(x*scl, (y+1)*scl, water[x][y+1])
    }
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
