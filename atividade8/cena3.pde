class Cena3 {
  ArrayList<Float> posicoesX;
  ArrayList<Float> posicoesY;
  ArrayList<Float> velocidadesY;
  ArrayList<Float> velocidadesX;

  Cena3() {
    posicoesX = new ArrayList<Float>();
    posicoesY = new ArrayList<Float>();
    velocidadesY = new ArrayList<Float>();
    velocidadesX = new ArrayList<Float>();
  }

  void adicionar(float x, float y) {
    posicoesX.add(x);
    posicoesY.add(y);
    velocidadesY.add(random(1, 5));
    velocidadesX.add(random(-5, 5));
  }

  void desenhar() {
    background(150);
    for (int i = posicoesX.size() - 1; i >= 0; i--) {
      posicoesY.set(i, posicoesY.get(i) + velocidadesY.get(i));
      posicoesX.set(i, posicoesX.get(i) + velocidadesX.get(i));
      noStroke();
      fill(random(255), random(255), random(255));
      ellipse(posicoesX.get(i), posicoesY.get(i), 20, 20);
    }
  }
}