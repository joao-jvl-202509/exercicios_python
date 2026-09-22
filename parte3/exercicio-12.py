print("Digite vários números, quando não quiser mais adicionar números, digite zero: ")
somaNumeros=0

while True:
    numero = int(input("Digite o próximo número: "))
    somaNumeros=somaNumeros+numero
    if numero==0:
        break

print(f"A soma de todos os números digitados é de {somaNumeros}.")