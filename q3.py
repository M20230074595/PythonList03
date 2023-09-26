
def get_fatorial(num):
    if num == 0:
        return 1
    else:
        fatorial = 1
        for i in range(1, num + 1):
            fatorial *= i
        return fatorial

valores_impares = []
for num in range(50, 61):
    if num % 2 != 0:
        valores_impares.append(num)

print("Fatoriais dos valores ímpares de 50 a 60:")
for numero in valores_impares:
    fatorial = get_fatorial(numero)
    print(f"{numero}! = {fatorial}")
