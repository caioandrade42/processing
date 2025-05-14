float x,y;



void void setup() {
  size(800, 600);
  x = random(width);
  y = random(height);
}

void draw() {
  background(0);
  circle(x, y, 80);
  x = lerp(x, mouseX, 0.1);
  y = lerp(y, mouseY, 0.1);
}
