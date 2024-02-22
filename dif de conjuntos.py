v = []
while len(v) < 10:
    x = int(input("Escreva um numero: "))
    if x in v:
        print("Nao pode escrever esse numero.")
    else:
        v.append(x)

w = []
while len(w) < 5:
    z = int(input("Escreva um numero: "))
    if z in w:
        print("Nao pode escrever esse numero.")
    else:
        w.append(z)


print(v - w)
print(v.difference(w))