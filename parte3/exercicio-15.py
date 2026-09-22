print("Digite vários números.")
numerosPositivos=0

while True:
    numero = int(input("Digite o próximo número: "))
    if numero==0:
        break
    if numero%2==0:
        numerosPositivos+=1

print(f"Você digitou {numerosPositivos} números positivos.")
