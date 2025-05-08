ArrayList<Float> posicoesX;
ArrayList<Float> posicoesY;
ArrayList<Float> velocidadesY;
ArrayList<Float> velocidadesX;

void setup() {
  size(800, 600);
  posicoesX = new ArrayList<Float>();
  posicoesY = new ArrayList<Float>();
  velocidadesY = new ArrayList<Float>();
  velocidadesX = new ArrayList<Float>();
}

void draw() {
  background(150); 
  posicoesX.add((float) mouseX);
  posicoesY.add((float) mouseY);
  velocidadesY.add(random(1, 5));
  velocidadesX.add(random(-5, 5));  
  
  for (int i = posicoesX.size() - 1; i >= 0; i--) {    
    posicoesY.set(i, posicoesY.get(i) + velocidadesY.get(i));
    posicoesX.set(i, posicoesX.get(i) + velocidadesX.get(i));    
    noStroke();
    ellipse(posicoesX.get(i), posicoesY.get(i), 20, 20);
    fill(random(255), random(255), random(255));
  }
}