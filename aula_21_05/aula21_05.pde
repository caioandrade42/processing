int cena, frame;
Cena1 cena1;
Cena2 cena2;
Cena3 cena3;
void setup() {
  size(800, 600);
  cena1 = new Cena1();
  cena2 = new Cena2(10, 300);
  cena3 = new Cena3();
  frame = 0;
  cena = 1;
}

void draw() {
  if (cena ==1) {
    cena1.desenhar();
  }else if (cena == 2) {
    cena2.desenhar();
  } else if (cena == 3) {
    cena3.adicionar(mouseX, mouseY);
    cena3.desenhar();    
  }
  frame++;
  if (frame >= 480) {
    cena ++;
    frame = 0;
  }
}
