#texto = input("Informe um texto: ")
texto = ""
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra)
else:
    print()
    print("Executado no final do laço")

# range com for   
for num in range(0, 51, 5):
    print(num, end=" ")

print()
print(list(range(11)))