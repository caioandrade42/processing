class Cena4{
  float x,y,cor,cor2,cor3;

  Cena4(float x, float y, float cor, float cor2, float cor3){
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
  void mostrarBola(Cena4 b){    
    fill(b.cor, b.cor2, b.cor3);
    noStroke();
    circle(b.x, b.y, 80);
  }
  void seguirBola(Cena4 b, Cena4 b2){
    b.x= lerp(b.x, b2.x, 0.2);
    b.y= lerp(b.y, b2.y, 0.2);
  }
}