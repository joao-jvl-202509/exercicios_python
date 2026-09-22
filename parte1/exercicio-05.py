precoProduto = float(input("Informe o preço do produto: R$"))
quantidadeProduto = int(input("Agora informe a quantida do produto comprado: "))

precoFinal = precoProduto*quantidadeProduto

print(f"O preço a se pagar é de R${round(precoFinal, 2)}.")