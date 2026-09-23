numeros = [5, 12, 8, 20, 3, 15]
i = 0
numeroMaior10=0

for i in range(0, 6):
    if numeros[i]>10:
        numeroMaior10+=1

print(f"{numeroMaior10} números são maiores que dez nessa lista.")