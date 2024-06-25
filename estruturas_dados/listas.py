carros = ['gol', 'astra', 'palio']

for indice, carro in enumerate(carros):
    print(f"O {carro} está na posição {indice}")

numeros = [1, 2, 16, 25, 39, 41, 44, 50, 65, 78]
pares = []

for num in numeros:
    if num % 2 == 0:
        pares.append(num)
        print(num, end=" ")
print()

frutas = ['maça', 'banana', 'mamão', 'abacaxi']
frutas.extend(['uva', 'abacate', 'maracujá']) # -> vários elementos entre colchetes...
#frutas.append('abacate') -> um elemento

print(frutas)
print(frutas.index('maracujá')) # -> retorna o índice 