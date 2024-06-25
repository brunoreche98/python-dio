class Bicicleta:
    def __init__(self, color, model, year, value):
        self.color = color
        self.model = model
        self.year = year
        self.value = value

    def buzinar(self):
        print("Plim Plim")

    def parar(self):
        print("Parando bicicleta")
        print("Bicicleta parada!")

    def correr(self):
        print("Acelerando!!")

    #def __str__(self):
    #    return f"Bicicleta: {self.color}, {self.model}, {self.year}, {self.value}"

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor
        in self.__dict__.items()])}"

bike1 = Bicicleta("amarela", "Caloi RSX-19", 2012, "R$1900.00")
#bike1.correr()
#bike1.buzinar()
#bike1.parar()

print(bike1)
