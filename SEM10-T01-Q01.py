deposito = float(input())
taxa = float(input())
ano = 1
valor_acumulado = deposito
while valor_acumulado <= (2*deposito):
    valor_acumulado = valor_acumulado + (valor_acumulado * (taxa/100))
    ano = ano + 1
print(f"{ano-1}")
