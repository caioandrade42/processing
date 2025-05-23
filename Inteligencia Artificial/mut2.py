import random


def f(x1, x2):
    return 0.25*x1**4 - 3*x1**3 + 11*x1**2 - 13*x1 + 0.25*x2**4 - 3*x2**3 + 11*x2**2 - 13*x2

def bin_to_float(bits):
    bin_val = int(''.join(str(b) for b in bits), 2)
    return bin_val / 31 * 6


X_list = [[random.randint(0, 1) for _ in range(10)] for _ in range(10)]
t = 0
print("Digite o numero de iteracoes: ")
max_iter = int(input())
i=0
while i < len(X_list):
    X = X_list[i] 
    while t < max_iter:        
        Z = [int(random.gauss(0, 1)) for _ in range(10)]
        Y = [(X[i] + Z[i]) % 2 for i in range(10)]        
        x1_X = bin_to_float(X[0:5])
        x2_X = bin_to_float(X[5:10])
        x1_Y = bin_to_float(Y[0:5])
        x2_Y = bin_to_float(Y[5:10])
        if f(x1_X, x2_X) <= f(x1_Y, x2_Y):
            X = X[:]
        else:
            X = Y[:]
        t += 1
    i += 1
    t = 0

for idx, X in enumerate(X_list):
    x1 = bin_to_float(X[0:5])
    x2 = bin_to_float(X[5:10])
    final = f(x1, x2)
    print(f"Solucao {idx+1}: {X}")
    print(f"x1: {x1}")
    print(f"x2: {x2}")
    print(f"f(x1, x2): {final}\n")
