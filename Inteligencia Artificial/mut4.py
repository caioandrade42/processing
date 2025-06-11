import random
from copy import deepcopy



moedas = [1,5,11,20]

def algoritmo_guloso(valor_troco):
    def algoritmo_guloso(valor_troco):
        moedas_ordenadas = sorted(moedas, reverse=True)        
        resultado = [0,0,0,0]        
        restante = valor_troco        
        for moeda in moedas_ordenadas:
            while restante >= moeda:
                if moeda == 1:
                    resultado[0] += 1
                elif moeda == 5:
                    resultado[1] += 1
                elif moeda == 11:
                    resultado[2] += 1
                elif moeda == 20:
                    resultado[3] += 1
                restante -= moeda        
        return resultado

def popula_individuos(quantidade_individuos, valor_troco):
    for _ in range quantidade_individuos:
        individuo = [0,0,0,0]
        restante = valor_troco
        while restante > 0:
            moeda = random.choice(moedas)
            if moeda <= restante:
                if moeda == 1:
                    individuo[0] += 1
                elif moeda == 5:
                    individuo[1] += 1
                elif moeda == 11:
                    individuo[2] += 1
                elif moeda == 20:
                    individuo[3] += 1
                restante -= moeda
        X_list.append(individuo)


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

def muta_individuo(individuo):
    for i in range(len(individuo)):
            individuo[i] = individuo[i] + random.choice([-1, 1])
    return individuo

print("Digite o valor do troco: ")
valor_troco = int(input())
print("Digite o numero de individuos: ")
quantidade_individuos = int(input()-1)
metodo_guloso = algoritmo_guloso(valor_troco)
X_list = []
X_list.append(metodo_guloso)
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
            if(random.randint(0, 3) == 0):
                if muta_individuo(x1_X, x2_X) <= muta_individuo(x1_Y, x2_Y):
                    X = deepcopy(X)
                    if muta_individuo(x1_X, x2_X) < muta_individuo(x1_M, x2_M):
                        melhor = deepcopy(X)
                    else:
                        parada += 1
                else:
                    X = deepcopy(Y)
                    if muta_individuo(x1_Y, x2_Y) < muta_individuo(x1_M, x2_M):
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
final = muta_individuo(x1, x2)
print(f"x1: {x1}")
print(f"x2: {x2}")
print(f"melhor solucao: {final}\n")