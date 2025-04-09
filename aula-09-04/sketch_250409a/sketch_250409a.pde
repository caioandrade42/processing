float ylinha2;
float zlinha5;
void setup(){
  size(600,600);
  zlinha5=120;
  ylinha2=320;
}

void draw(){
  noFill();
  background(255);
  stroke(255, 102, 0);
  line(120, 80, 320, 20);
  line(ylinha2, 300, 120, 300);
  stroke(0, 0, 0);
  bezier(120, 80,  320, 20,  ylinha2, 300,  120, 300);
  ylinha2 = ylinha2+0.2;
}
