numeros = []

for i in range(10):
    numeros.append(int(input("Digite um número: ")))

print("Lista original:", numeros)
print("Lista ordenada crescente:", sorted(numeros))

unicos = []
for n in numeros:
    if n not in unicos:
        unicos.append(n)
print("Lista sem repetidos:", unicos)
