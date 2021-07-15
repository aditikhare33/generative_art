let t = 0;
let t2 = 0;
let size = 30;

function setup() {
  createCanvas(windowWidth, windowHeight);
  background(0);
  colorMode(HSB)
}

function keyPressed() {
    if (key === 'w') {
      size += 3;
    } else if (key === 's') {
      size -= 3;
    } else if (key == 'r') {
      background(0)
    }
}

function draw() {
  fill(color(t, 255, 255));
  rect(mouseX, mouseY, (sin(t2) + 2) * 155, (sin(t2) + 2) * 155);

  if (t >= 255) { t = 0; }
  else { t++; }

  if (t2 >= 30) { t2 = 0; }
  else { t2 += 0.01; }

  
}
