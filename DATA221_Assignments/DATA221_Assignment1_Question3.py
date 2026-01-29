# Safe function Application

def power (x, y):
    return x ** y # Compute x^y

pairs = [[5, 2], [3, -1], [4, 3], [2, 0]]
result = []

for x, y in pairs: #unpacking argument
    if y < 0:
        continue
    result.append(power(x, y))

print(result)