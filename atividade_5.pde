float [][] m;

void setup() {
  size(800, 600);
  m[5][2];
  m[0][0] = 400.0;
  m[0][1] = 300.0;
}

void draw(){
  background(0);
  mostrarBola(m[0][0], m[0][1]);
  seguirMouse(m[0][0], m[0][1]);
  for (int i = 1; i < 5; ++i) {
      mostrarBola(m[i][0], m[i][1]);
      m[i][0] = lerp(m[i][0], m[i-1][0], 0.1);
      m[i][1] = lerp(m[i][1], m[i-1][1], 0.1);
  }
}

void seguirMouse(float m[0][0], float m[0][1]){
  float x = m[0][0];
  float y = m[0][1];
  noStroke();
  circle(x, y, 80);
  x = lerp(x, mouseX, 0.1);
  y = lerp(y, mouseY, 0.1);
}

void mostrarBola(float x, float y){
  noStroke();
  circle(x, y, 80);
}