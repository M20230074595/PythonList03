import random

def media_pares(contagem_pares, soma_pares):
    if  contagem_pares > 0:
        return soma_pares / contagem_pares
    else:
        return 0
    
def media_impares(contagem_impares, soma_impares):
    if  contagem_impares > 0:
        return soma_impares / contagem_impares
    else:
        return 0

valores = []
soma_total = 0
soma_pares = 0
soma_impares = 0
contagem_pares = 0
contagem_impares = 0

for _ in range(50):
    valor = random.randint(1, 1000) 
    valores.append(valor)
    soma_total += valor
    if valor % 2 == 0:  
        soma_pares += valor
        contagem_pares += 1
    else:
        soma_impares += valor
        contagem_impares += 1



print("Valores gerados aleatoriamente:")
print(valores)
print(f"Soma total dos valores: {soma_total}")
print(f"Média dos valores pares: {media_pares(contagem_pares,soma_pares)}")
print(f"Média dos valores ímpares: {media_impares(contagem_impares, soma_impares)}")
