menor = maior = quant = num = 0
while True:
    num = int(input())
    if num == 0:
        break
    quant = quant + 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print(maior)
print(menor)