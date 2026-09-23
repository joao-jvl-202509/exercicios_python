numeros = [12, 22, 5, 4, 8]
i = 0
numeroMaior=0

for i in range(0, 5):
    if numeros[i]>numeroMaior:
        numeroMaior=numeros[i]

print(f"O maior número da lista é {numeroMaior}")