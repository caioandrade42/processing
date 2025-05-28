import random
from copy import deepcopy 


def mutacoes(x1, x2):
    return 0.25*x1**4 - 3*x1**3 + 11*x1**2 - 13*x1 + 0.25*x2**4 - 3*x2**3 + 11*x2**2 - 13*x2

def bin_to_float(bits):
    bin_val = int(''.join(str(b) for b in bits), 2)
    return bin_val / 31 * 6

def recombina_individuo(individuo1, individuo2):
    ponto_recombinacao = random.randint(1, len(individuo1) - 1)
    return individuo1[:ponto_recombinacao] + individuo2[ponto_recombinacao:]

def popula_filhos(X_list):
    while i< len(X_list):
    N_list = [[recombina_individuo(X_list[i], X_list[i+1]) for i in range(len(X_list)-1)] for _ in range(num_individuos)]
    i+=1
    X_list = N_list

print("Digite o numero de individuos: ")
num_individuos = int(input())
X_list = [[random.randint(0, 1) for _ in range(10)] for _ in range(num_individuos)]
N_list = [[]]

t = 0
final = float('inf')
melhor_solucao = float('inf')
print("Digite o numero de iteracoes: ")
max_iter = int(input())
print("Digite o numero de recombinações: ")
max_recomb = int(input())
i=0
while i < len(N_list):
    X = N_list[i] 
    while t < max_iter:        
        Z = [int(random.gauss(0, 1)) for _ in range(10)]
        Y = [(X[i] + Z[i]) % 2 for i in range(10)]        
        x1_X = bin_to_float(X[0:5])
        x2_X = bin_to_float(X[5:10])
        x1_Y = bin_to_float(Y[0:5])
        x2_Y = bin_to_float(Y[5:10])
        if mutacoes(x1_X, x2_X) <= mutacoes(x1_Y, x2_Y):
            X = deepcopy(X)
        else:
            X = deepcopy(Y)
        t += 1
    i += 1
    t = 0

print(f"Melhor individuo: {X}")
x1 = bin_to_float(X[0:5])
x2 = bin_to_float(X[5:10])
final = mutacoes(x1, x2)
print(f"x1: {x1}")
print(f"x2: {x2}")
print(f"melhor solucao: {final}\n")