frutas = ('maça', 'banana', 'uva', 'abacate',)
#print(frutas)

matriz = (
    (1, 'c', 10),
    ('b', 'a', 18),
    (18, -3, 'name')
)

#print(matriz)
#print(matriz[0][0])
#print(matriz[1][1])
#print(matriz[2][-1])
#print(matriz[-1][1])

#for tup in matriz:
#    print(tup[0], tup[1])

for indice, tup in enumerate(matriz):
    print(f"{indice}: {tup[1]}")