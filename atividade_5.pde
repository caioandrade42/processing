int n = 5; 
float[][] m = new float[n][2];

void setup() {
  size(800, 600);
  for (int i = 0; i < n; i++) {
    m[i][0] = width/2;
    m[i][1] = height/2;
  }
}

void draw() {
  background(0);

  m[0][0] = lerp(m[0][0], mouseX, 0.1);
  m[0][1] = lerp(m[0][1], mouseY, 0.1);
  for (int i = 1; i < n; i++) {
    m[i][0] = lerp(m[i][0], m[i-1][0], 0.1);
    m[i][1] = lerp(m[i][1], m[i-1][1], 0.1);
  }

  for (int i = 0; i < n; i++) {
    mostrarBola(m[i][0], m[i][1]);
  }
}

void mostrarBola(float x, float y) {
  noStroke();
  fill(255, 150);
  ellipse(x, y, 80, 80);
}