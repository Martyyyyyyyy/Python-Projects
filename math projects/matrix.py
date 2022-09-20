import random

m = int(input('m = '))
n = int(input('n = '))

A = [ [random.randint(-10, 11) for j in range(n)] for i in range(m) ]

print('-------------------------')
print("A:")
for i in range(m):
    print(A[i])

B = [ [ A[i][j]+10 for j in range(n) ] for i in range(m) ]

print("B:")
for i in range(m):
    print(B[i])