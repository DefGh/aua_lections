from scipy import stats

i = - 3.14
xs = []

while i <= 3.14:
    xs.append(i)
    i += 0.01

med = 0
std = 1

print("[", end="")    

for x in xs:
    zindex = (x - med) / std
    y = stats.norm.pdf(zindex)
    print(f"{y:.4f}", end="" if x == xs[-1] else ",")

print("]")