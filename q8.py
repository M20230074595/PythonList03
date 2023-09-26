import random
times = ["Flamengo  ","São Paulo ","ABC       ", "América   ", "Vasco     "]
num_votacoes = int(input("Digite o número de votações: "))
votos_por_time = {time: 0 for time in times}


for _ in range(num_votacoes):
    voto = random.choice(times)
    votos_por_time[voto] += 1
time_preferido = max(votos_por_time, key=votos_por_time.get)




print("\nResultados das votações:")
for time, votos in votos_por_time.items():
    print(f"{time}:\t {votos} votos")
print(f"\nO time preferido é: {time_preferido}")
