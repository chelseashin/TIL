# Baby Gin greedy algorithm
num = 123123
c = [0] * 12
for i in range(6):
    c[num % 10] += 1
    num //= 10
i = 0
triplet = 0
run = 0

while i < 10:
    if c[i] >= 3:
        c[i] > 3
        c[i] -= 3
        triplet += 1
        continue
    if c[i] >= 1 and c[i+1] > 1 and c[i+2] >= 1:
        c[i] -= 1
        c[i+1] -= 1
        c[i+2] -= 1
        run += 1
        continue
    i += 1
if triplet + run == 2:
    print("Baby Gin")
else:
    print("Not Baby Gin")