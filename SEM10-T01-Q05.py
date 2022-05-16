ano = 2016
mes = 10
sal = float(input())
div = float(input())
while True:
    div *= 1.15
    if mes == 3:
        sal *= 1.05
    elif mes == 12:
        mes = 1
        ano += 1
        continue
    mes += 1
    if div > sal:
        print(f'{mes}/{ano}')
        break
