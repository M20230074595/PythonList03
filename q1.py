while True:
    numero = int(input("Digite um número inteiro de 1 a 10: "))
    if 1 <= numero <= 10:
        break
    else:
        print("Número fora do intervalo válido. Tente novamente.")
print(f"Tabuada do {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
