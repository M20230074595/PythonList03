import random

print("Valor\tPotência de 2")
print("-------------------")

for _ in range(10):
    valor = random.randint(1, 100)  
    potencia_de_2 = 2 ** valor
    print(f"{valor}\t{potencia_de_2}")
