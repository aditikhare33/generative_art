class Sphere {
    constructor(radius, x, y) {
        this.radius = radius;
        this.x = x;
        this.y = y;
    }

    move(x_change, y_change) {
        this.x += x_change;
        this.y += y_change;
    }

    show() {
        sphere(this.radius);
    }
}



let angle = 0;

function setup() {
  createCanvas(400, 300, WEBGL);
}

function draw() {
  let dx = mouseX - width / 2;
  let dy = mouseY - height / 2;
  let v = createVector(dx, dy, 0);
  v.div(100);

  ambientLight(0, 0, 255);
  directionalLight(255, 0, 0, v);
  //pointLight(255, 0, 0, 200, 0, 0);

  background(255);

  rotateX(angle);
  rotateY(angle * 0.3);
  rotateZ(angle * 1.2);

  noStroke();
  ambientMaterial(255);
  //fill(0, 0, 255);
  torus(100, 25);

  angle += 0.03;
}