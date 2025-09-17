import random

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45]
A = random.choice(numbers)
numbers.pop(A)
B = random.choice(numbers)
numbers.pop(B)
C = random.choice(numbers)
numbers.pop(C)
D = random.choice(numbers)
numbers.pop(D)
E = random.choice(numbers)
numbers.pop(E)
F = random.choice(numbers)

print("Your lucky numbers are "+str(A)+", "+str(B)+", "+str(C)+", "+str(D)+", "+str(E)+" and "+str(F)+".")