numero = int(input("Digite um número: "))
fatorialNumero=1

for i in range(1, numero+1):
    fatorialNumero = fatorialNumero*i

print(f"O fatorial do número {numero} é de {fatorialNumero}.")

