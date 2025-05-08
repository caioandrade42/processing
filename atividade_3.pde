int solY=100, contador=0;

float cor=255;

float band1 = 190, band2 = 42,numero,grau=0,grau5=0,grau10=1.5,grau20=3,grau3=4.5,corMastro=0;

void setup()
{
  size(600,600);
}

void draw(){
contador ++;
if (contador%60==0) {
  grau3 = 0;
  grau5 = 0;
  grau10 = 0;
  grau20 = 0;
  grau10=random(-PI, PI);
  grau20 = random(-PI, PI);
  grau3 = random(-PI, PI);
  grau5 = random(-PI, PI);
}

background (0, cor, cor);

fill(cor, cor,0);

circle(100, solY, 200);

fill(0,cor,0);

ellipse (500,600,1500,500);

fill (band1,band2, band2);

rect(450,100,14,300);

noStroke();

beginShape();

vertex(464,100);

vertex(564,100);

vertex(540,115);

vertex(564,130);

vertex(464,130);

endShape();

translate (300,300);

rotate(grau);

fill(0);

rect(-60,20,20,150);


fill(cor);

push();

fill(cor);

translate(-50, 20);

rotate(grau5);

rect(0,0,100,20);

pop();

push();

fill(cor);

translate(-50, 20);

rotate(grau10);

rect(0,0,100,20);

pop();

push();

fill(cor);

translate(-50, 20);

rotate(grau20);

rect(0,0,100,20);

pop();

push();

fill(cor);

translate(-50, 20);

rotate(grau3);

rect(0,0,100,20);

pop();

grau5 -= 0.08;

grau10 -= 0.08;

grau20 -= 0.08;

grau3 -= 0.08;

solY=solY+1;

//cor=cor-0.7;

band1=band1-0.50;

band2=band2-0.20;

corMastro = corMastro - 0.20;


}