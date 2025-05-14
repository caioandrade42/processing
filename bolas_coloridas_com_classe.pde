float x,y;
Bola bolas[] = new Bola[5];


void setup() {
  size(1400, 800);
  x = 400.0;
  y = 300.0;
  for (int i = 0; i < bolas.length; ++i) {
    bolas[i] = new Bola((x+i+4), (y+i+4), random(255), random(255), random(255));
  }
}

void draw() {
  background(0);
  for (int i = 0; i < bolas.length; i++){    
    bolas[0].move();
    bolas[0].mostrarBola(bolas[0]);
    if (i > 0){
      bolas[i].seguirBola(bolas[i], bolas[i-1]);
      bolas[i].mostrarBola(bolas[i]);
  }
  }
}

class Bola{
  float x,y,cor,cor2,cor3;

  Bola(float x, float y, float cor, float cor2, float cor3){
    this.x = x;
    this.y = y;
    this.cor = cor;
    this.cor2 = cor2;
    this.cor3 = cor3;
  }
  void move(){
    x = lerp(x, mouseX, 0.1);
    y = lerp(y, mouseY, 0.1);
  }
  void mostrarBola(Bola b){    
    fill(b.cor, b.cor2, b.cor3);
    noStroke();
    circle(b.x, b.y, 80);
  }
  void seguirBola(Bola b, Bola b2){
    b.x= lerp(b.x, b2.x, 0.2);
    b.y= lerp(b.y, b2.y, 0.2);
  }
}