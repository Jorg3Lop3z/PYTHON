numeros = []
n = 0
with open("numbers.txt", "r") as file:
    for x in file:
        n = int(x.strip())
        numeros.append(n)
numeros.sort()
print(numeros[-1])
print(numeros[-2])
print(numeros[-3])