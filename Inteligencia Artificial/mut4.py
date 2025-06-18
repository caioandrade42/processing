import random


moedas = [1, 5, 11, 20]


def algoritmo_guloso(valor_troco):
    moedas_ordenadas = sorted(moedas, reverse=True)
    resultado = [0] * len(moedas)
    restante = valor_troco

    for i, moeda in enumerate(moedas_ordenadas):
        if restante >= moeda:
            qtd = restante // moeda
            resultado[i] += qtd
            restante -= qtd * moeda
    return resultado


def fitness(individuo, moedas, valor_troco):
    soma = sum(qtd * moeda for qtd, moeda in zip(individuo, moedas))
    if soma != valor_troco:
        return float('inf')  
    return sum(individuo)  


def gerar_individuo(moedas, valor_troco):
    while True:
        individuo = [0] * len(moedas)
        restante = valor_troco
        while restante > 0:
            idx = random.randint(0, len(moedas)-1)
            moeda = moedas[idx]
            if moeda <= restante:
                individuo[idx] += 1
                restante -= moeda
        if fitness(individuo, moedas, valor_troco) < float('inf'):
            return individuo

def crossover(pai1, pai2, moedas, valor_troco):
    ponto = random.randint(1, len(pai1) - 1)
    filho = pai1[:ponto] + pai2[ponto:]
    if fitness(filho, moedas, valor_troco) < float('inf'):
        return filho
    else:
        return gerar_individuo(moedas, valor_troco)


def mutacao(individuo, moedas, valor_troco, taxa_mut=0.1):
    if random.random() < taxa_mut:
        i = random.randint(0, len(individuo)-1)
        j = random.randint(0, len(individuo)-1)
        if individuo[i] > 0:
            individuo[i] -= 1
            individuo[j] += 1
    return individuo


def selecionar(populacao, moedas, valor_troco, tamanho_elite=2):
    populacao.sort(key=lambda x: fitness(x, moedas, valor_troco))
    return populacao[:tamanho_elite]


def algoritmo_genetico(valor_troco, moedas, tam_pop, max_geracoes, num_crossovers):
    populacao = [gerar_individuo(moedas, valor_troco) for _ in range(tam_pop)]
    melhor = min(populacao, key=lambda x: fitness(x, moedas, valor_troco))

    for geracao in range(max_geracoes):
        nova_pop = []
        elite = selecionar(populacao, moedas, valor_troco)
        nova_pop.extend(elite)

        while len(nova_pop) < tam_pop and num_crossovers > 0:
            pai1, pai2 = random.sample(populacao, 2)
            filho = crossover(pai1, pai2, moedas, valor_troco)
            filho = mutacao(filho, moedas, valor_troco)
            nova_pop.append(filho)
            num_crossovers -= 1

        
        while len(nova_pop) < tam_pop:
            nova_pop.append(gerar_individuo(moedas, valor_troco))

        populacao = nova_pop
        atual = min(populacao, key=lambda x: fitness(x, moedas, valor_troco))
        if fitness(atual, moedas, valor_troco) < fitness(melhor, moedas, valor_troco):
            melhor = atual

    return melhor


def quantidade_moedas(individuo):
    return sum(individuo)


print("Digite o valor do troco:")
valor_troco = int(input())

print("Digite o tamanho da população inicial:")
tam_pop = int(input())

print("Digite o número máximo de gerações:")
max_geracoes = int(input())

print("Digite o número máximo de crossovers por geração:")
num_crossovers = int(input())


guloso = algoritmo_guloso(valor_troco)
ag = algoritmo_genetico(valor_troco, moedas, tam_pop, max_geracoes, num_crossovers)


qtd_guloso = quantidade_moedas(guloso)
qtd_ag = quantidade_moedas(ag)

print("\nResultado:")
print(f"Guloso: {guloso} → Moedas: {qtd_guloso}")
print(f"Genético: {ag} → Moedas: {qtd_ag}")

if qtd_ag < qtd_guloso:
    print("🎉 O Algoritmo Genético encontrou uma solução mais eficiente!")
elif qtd_ag == qtd_guloso:
    print("✅ Os dois métodos usaram o mesmo número de moedas.")
else:
    print("⚠️ O Algoritmo Guloso foi mais eficiente.")