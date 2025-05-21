class Cena2 {
  float[] vetor;
  int quantidade;
  float alturaBarra;

  Cena2(int quantidade, float alturaBarra) {
    this.quantidade = quantidade;
    this.alturaBarra = alturaBarra;
    vetor = new float[quantidade];
    for (int i = 0; i < vetor.length; i++) {
      vetor[i] = random(alturaBarra); 
    }
  }

  void desenhar() {
    background(255);
    stroke(0);
    fill(100, 150, 255);
    
    float larguraBarra = width / (float) vetor.length;
    
    for (int i = 0; i < vetor.length; i++) {
      float x = i * larguraBarra;
      float y = alturaBarra - vetor[i];
      rect(x, y, larguraBarra - 2, vetor[i]);
      fill(random(255), random(255), random(255)); 
    }
  }
}