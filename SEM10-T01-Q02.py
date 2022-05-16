soma = 0
media = 0
while True:
    n = int(input())
    if n == 0:
        break
    soma = soma + n
    media = soma / n
    quantidade = quantidade + 1
print(media)

