import random
from copy import deepcopy

moedas = [1,5,11,20]

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
    for _ in range(quantidade_individuos):
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

def calcula_moedas(individuo):
    soma = 0
    troco_resultante = 0
    troco_resultante =troco_resultante + individuo[0]*1
    troco_resultante = troco_resultante + individuo[1]*5
    troco_resultante = troco_resultante + individuo[2]*11
    troco_resultante = troco_resultante + individuo[3]*20
    if troco_resultante == valor_troco:
        return true
    else :
        return false

def quantidade_moedas(individuo):
    quantidade = 0
    for i in range(4):
        quantidade += individuo[i]
    return quantidade

print("Digite o valor do troco: ")
valor_troco = int(input())
print("Digite o numero de individuos: ")
quantidade_individuos = int(input())
metodo_guloso = algoritmo_guloso(valor_troco)
X_list = []
X_list.append(metodo_guloso)
N_list = []
melhor = []

melhor.append(X_list)
melhor.append(X_list)

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
            if(random.randint(0, 3) == 0):
                X = muta_individuo(X)                
                if calcula_moedas(X) & quantidade_moedas(X)<quantidade_moedas(melhor[0]):
                    if quantidade_moedas(X)<quantidade_moedas(melhor[1]):
                        melhor[1] = deepcopy(X)
                    else:
                        parada += 1
            t += 1
            
        i += 1
        
        t = 0
    recomb += 1

print(f"Melhor individuo: {melhor[1]}")
print(f"Melhor individuo usando algoritmo guloso: {melhor[0]}")