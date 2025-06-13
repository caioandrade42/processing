float x,y;
int cena=1;
Cena1 cena1 = new Cena1();
Cena2 cena2 = new Cena2(10, 300);
Cena3 cena3 = new Cena3();
Cena4 cena4[] = new Cena4[5];
void setup() {
  size(800, 600);
  cena = 1;
  x = 400.0;
  y = 300.0;
  for (int i = 0; i < cena4.length; ++i) {
    cena4[i] = new Cena4((x+i+4), (y+i+4), random(255), random(255), random(255));
  }
}

void draw() {
  if (cena ==1) {
    cena1.desenhar();
  }else if (cena == 2) {
    cena2.desenhar();
  } else if (cena == 3) {
    cena3.adicionar(mouseX, mouseY);
    cena3.desenhar();    
  }else if (cena == 4) {
    background(0);
    for (int i = 0; i < cena4.length; i++){  
      cena4[0].move();
      cena4[0].mostrarBola(cena4[0]);
      if (i > 0){
        cena4[i].seguirBola(cena4[i], cena4[i-1]);
        cena4[i].mostrarBola(cena4[i]);
      }
    }
  }
}

void keyPressed() {
  if (key == ' ') {
    cena++;
    if (cena > 4) {
      cena = 1;
    }
  }
}