float[] vetor;
int quantidade = 10;

void setup() {
  size(800, 400);
  vetor = new float[quantidade];
  for (int i = 0; i < vetor.length; i++) {
    vetor[i] = random(alturaBarra); 
  }
  noLoop();
}

void draw() {
  background(255);
  stroke(0);
  fill(100, 150, 255);
  
  float larguraBarra = width / (float) vetor.length;
  
  for (int i = 0; i < vetor.length; i++) {
    float x = i * larguraBarra;
    float y = alturaBarra - vetor[i];
    rect(x, y, larguraBarra - 2, vetor[i]);
    fill(random(255), random(255),random(255)); 
  }
}