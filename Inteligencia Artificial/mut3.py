import random
from copy import deepcopy 


def mutacoes(x1, x2):
    return 0.25*x1**4 - 3*x1**3 + 11*x1**2 - 13*x1 + 0.25*x2**4 - 3*x2**3 + 11*x2**2 - 13*x2

def bin_to_float(bits):
    bin_val = int(''.join(str(b) for b in bits), 2)
    return bin_val / 31 * 6

def recombina_individuo(individuo1, individuo2, N_list):
    ponto_recombinacao = random.randint(1, len(individuo1) - 1)
    individuo1 = individuo1[:ponto_recombinacao] + individuo2[ponto_recombinacao:]
    N_list.append(individuo1)
    individuo2 = individuo2[:ponto_recombinacao] + individuo1[ponto_recombinacao:]
    N_list.append(individuo2)
    return 

def popula_filhos(X_list):
    i = 1
    while i< len(X_list):
        recombina_individuo(X_list[i-1], X_list[(i)], N_list)
        i+=1
    X_list = N_list

print("Digite o numero de individuos: ")
num_individuos = int(input())
X_list = [[random.randint(0, 1) for _ in range(10)] for _ in range(num_individuos)]
N_list = []

melhor = X_list[0]

t = 0
final = float('inf')
melhor_solucao = float('inf')
print("Digite o numero de iteracoes: ")
max_iter = int(input())
print("Digite o numero de recombinações: ")
max_recomb = int(input())
recomb=0
i=0
parada = 0
while recomb < max_recomb:
    popula_filhos(X_list)

    while i < len(N_list):
        X = N_list[i] 
        while t < max_iter:     
            Z = [int(random.gauss(0, 1)) for _ in range(10)]
            Y = [(X[i] + Z[i]) % 2 for i in range(10)]        
            x1_X = bin_to_float(X[0:5])
            x2_X = bin_to_float(X[5:10])
            x1_Y = bin_to_float(Y[0:5])
            x2_Y = bin_to_float(Y[5:10])
            x1_M = bin_to_float(melhor[0:5])
            x2_M = bin_to_float(melhor[5:10])
            if(random.randint(0, 3) == 0):
                if mutacoes(x1_X, x2_X) <= mutacoes(x1_Y, x2_Y):
                    X = deepcopy(X)
                    if mutacoes(x1_X, x2_X) < mutacoes(x1_M, x2_M):
                        melhor = deepcopy(X)
                    else:
                        parada += 1
                else:
                    X = deepcopy(Y)
                    if mutacoes(x1_Y, x2_Y) < mutacoes(x1_M, x2_M):
                        melhor = deepcopy(Y)
                    else:
                        parada += 1
            t += 1
            
        i += 1
        
        t = 0
    recomb += 1

print(f"Melhor individuo: {melhor}")
x1 = bin_to_float(melhor[0:5])
x2 = bin_to_float(melhor[5:10])
final = mutacoes(x1, x2)
print(f"x1: {x1}")
print(f"x2: {x2}")
print(f"melhor solucao: {final}\n")