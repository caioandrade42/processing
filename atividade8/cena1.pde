class Cena1 {
  float x;

  Cena1() {
    x = -300;
  }

  void setupCena1() {
    size(600, 600);
    background(255);
    stroke(0);
    noFill();
    strokeWeight(2); 

    line(0, height / 2, width, height / 2); 
    line(width / 2, 0, width / 2, height); 

    stroke(255, 255, 0); 
  }

  void desenhar() {
    translate(width / 2, height / 2);
    scale(1, -1); 

    float y = pow(x / 75.0, 3) * 75; 
    if (x > -300) {
      float prevY = pow((x - 1) / 75.0, 3) * 75;
      line(x - 1, prevY, x, y);
    }

    x += 1;
  }
}

