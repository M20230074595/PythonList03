valores_positivos = []

while True:
    valor = int(input("Digite um valor positivo (ou um valor negativo para encerrar): "))
    if valor < 0:
        break  
    else:
        valores_positivos.append(valor)

if len(valores_positivos) > 0:
    print("Valores positivos inseridos:")
    for valor in valores_positivos:
        print(valor)
else:
    print("Nenhum valor positivo foi inserido.")
