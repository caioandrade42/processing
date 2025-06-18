import random
import operator
from copy import deepcopy

# -----------------------------
# CONFIGURAÇÕES DO PROBLEMA
# -----------------------------

ENTRADAS = [0,1,2,3,4,5,6,7,8,9,10]
SAIDAS   = [6,2,0,0,2,6,12,20,30,42,56]  # f(x) = 2*x + 1

# Funções primitivas
FUNCOES = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': lambda x, y: x / y if y != 0 else 0  # Evita divisão por zero
}

# Terminais
TERMINAIS = ['x']

# -----------------------------
# GERAÇÃO DE ÁRVORES ALEATÓRIAS
# -----------------------------

def gerar_arvore(max_depth=4, is_func=True):
    if max_depth == 0 or (not is_func and random.random() < 0.5):
        return random.choice(TERMINAIS + [str(random.randint(-5,5))])
    else:
        op = random.choice(list(FUNCOES.keys()))
        esquerda = gerar_arvore(max_depth - 1, False)
        direita = gerar_arvore(max_depth - 1, False)
        return [op, esquerda, direita]

# -----------------------------
# AVALIAÇÃO DA FUNÇÃO
# -----------------------------

def avaliar_arvore(arvore, x):
    if isinstance(arvore, list):
        op, esq, dir = arvore
        fe = avaliar_arvore(esq, x)
        fd = avaliar_arvore(dir, x)
        try:
            return FUNCOES[op](fe, fd)
        except:
            return float('inf')
    else:
        if arvore == 'x':
            return x
        else:
            return int(arvore)

def calcular_fitness(arvore):
    erro_total = 0
    for x, y in zip(ENTRADAS, SAIDAS):
        try:
            saida = avaliar_arvore(arvore, x)
            erro_total += abs(saida - y)
        except:
            erro_total += float('inf')
    return erro_total

# -----------------------------
# RECOMBINAÇÃO (CROSSOVER)
# -----------------------------

def crossover(arvore1, arvore2):
    if isinstance(arvore1, list) and isinstance(arvore2, list) and random.random() < 0.7:
        ponto = random.randint(0, 2)
        nova_arvore = deepcopy(arvore1)
        nova_arvore[ponto] = deepcopy(arvore2[random.randint(0, 2)])
        return nova_arvore
    else:
        return deepcopy(random.choice([arvore1, arvore2]))

# -----------------------------
# MUTAÇÃO
# -----------------------------

def mutacao(arvore, taxa_mut=0.1):
    if random.random() < taxa_mut:
        tipo = random.choice(['troca_no', 'troca_valor', 'insercao'])
        if tipo == 'troca_no' and isinstance(arvore, list):
            idx = random.randint(0, 2)
            arvore[idx] = gerar_arvore(2, False)
        elif tipo == 'troca_valor' and not isinstance(arvore, list):
            return random.choice(TERMINAIS + [str(random.randint(-5,5))])
        elif tipo == 'insercao' and isinstance(arvore, list):
            idx = random.randint(0, 2)
            novo_no = [random.choice(list(FUNCOES.keys())), arvore[idx], gerar_arvore(2, False)]
            arvore[idx] = novo_no
    return arvore

# -----------------------------
# SELEÇÃO (TORNEIO)
# -----------------------------

def selecao(populacao, fitnesses):
    competidores = random.sample(list(zip(populacao, fitnesses)), 3)
    competidores.sort(key=lambda x: x[1])
    return competidores[0][0]

# -----------------------------
# PROGRAMAÇÃO GENÉTICA PRINCIPAL
# -----------------------------

def programacao_genetica(max_geracoes=100, tam_pop=50, max_depth=3):
    populacao = [gerar_arvore(max_depth) for _ in range(tam_pop)]
    melhor = None
    menor_erro = float('inf')

    for geracao in range(max_geracoes):
        fitnesses = []
        for arvore in populacao:
            erro = calcular_fitness(arvore)
            fitnesses.append(erro)
            if erro < menor_erro:
                menor_erro = erro
                melhor = deepcopy(arvore)                
                print(f"[Geração {geracao}] Novo melhor: {arvore} → Erro total: {menor_erro}")
                if menor_erro == 0:
                    print("🎯 Solução encontrada!")
                    return melhor

        # Nova geração
        nova_pop = []
        for _ in range(tam_pop):
            pai1 = selecao(populacao, fitnesses)
            pai2 = selecao(populacao, fitnesses)
            filho = crossover(pai1, pai2)
            filho = mutacao(filho)
            nova_pop.append(filho)
        populacao = nova_pop

    print("\n⚠️ Máximo de gerações atingido.")
    return melhor

# -----------------------------
# IMPRESSÃO SIMPLES DA ÁRVORE
# -----------------------------

def imprimir_arvore(arvore):
    if isinstance(arvore, list):
        return f"({arvore[0]} {imprimir_arvore(arvore[1])} {imprimir_arvore(arvore[2])})"
    else:
        return str(arvore)

# -----------------------------
# EXECUÇÃO PRINCIPAL
# -----------------------------

print("🔍 Iniciando Programação Genética...\n")
melhor_funcao = programacao_genetica(max_geracoes=1000, tam_pop=1000, max_depth=3)

print("\n🧠 Melhor função encontrada:")
print(imprimir_arvore(melhor_funcao))

# Teste final
x_teste = 6
resultado_previsto = avaliar_arvore(melhor_funcao, x_teste)
print(f"\nTestando com x = {x_teste}: Resultado = {resultado_previsto}")