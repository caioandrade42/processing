import random

vetor = [None]*10
for i in range(10):
    vetor[i] = random.randint(0, 1)
    

str1 = ""
str2 = ""
x1 = float()
x2 = float()
final = float()

sub1 = vetor[0:5]
sub2 = vetor[5:10]

for i in range(5):
    str1 += str(sub1[i])
    str2 += str(sub2[i])
    
bin1 = int(str1, 2)
bin2 = int(str2, 2)

x1 = bin1/31*6
x2 = bin2/31*6 

final = 0.25*x1**4-3*x1**3+11*x1**2-13*x1+0.25*x2**4-3*x2**3+11*x2**2-13*x2

print(bin1)
print(bin2)
print(x1)
print(x2)
print(final)


def f(x1, x2):
    return 0.25*x1**4 - 3*x1**3 + 11*x1**2 - 13*x1 + 0.25*x2**4 - 3*x2**3 + 11*x2**2 - 13*x2

def bin_to_float(bits):
    bin_val = int(''.join(str(b) for b in bits), 2)
    return bin_val / 31 * 6


X = [random.randint(0, 1) for _ in range(10)]
t = 0
max_iter = 1000 

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


x1 = bin_to_float(X[0:5])
x2 = bin_to_float(X[5:10])
final = f(x1, x2)
print("Solução final:", X)
print("x1:", x1)
print("x2:", x2)
print("f(x1, x2):", final)
