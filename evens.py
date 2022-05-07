evens = []
with open("numbers.txt", "r") as file:
    for x in file:
        n = int(x.strip())
        if n % 2 == 0:
            evens.append(str(n)+"\n")

file = open("even_numbers.txt", "w")
for x in evens:
    file.write(x)
file.close()
print("List of even numbers created!")