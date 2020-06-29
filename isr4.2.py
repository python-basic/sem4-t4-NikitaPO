import random

list = [random.randint(-100, 100) for i in range(6)]
print(list)

posit = []
negat = []
for i in list:
    (lambda i: posit.append(i) if i>0 else negat.append(i))(i)

print(posit)
print(negat)

even = []
odd = []
for i in list:
    (lambda i: odd.append(i) if i % 2 else even.append(i))(i)

print(even)
print(odd)
