import random as r

n = [r.randint(0, 10) for i in range(10)]
m = [r.randint(0, 10) for i in range(10)]
print(n)
print(m)
summa = []
summa = n + m
print(summa)
nopovt = []
tran =[]
for i in range(len(summa)):
    if summa[i] not in nopovt:
        nopovt.append(summa[i])
for j in range(len(n)):
    if n[j] in m and n[j] not in tran:
        tran.append(n[j])
print(nopovt)
print(tran)
print([min(n), min(m), max(n), max(m)])








