# Métodos de classe e Métodos estáticos
# Um método de classe recebe um primeiro parâmetro que aponta para a classe, enquanto um método estático não.
# Um método de classe pode acessar ou modificar o estado da classe enquanto um método estático não pode acessá-lo ou modificá-lo

# Quando usar: Geralmente usamos o método de classe para criar métodos de fábrica. Já os métodos estáticos para criar funções utilitárias

class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod # -> transforma em método de classe, e por convenção o 1º parâmetro é cls que referência a própria classe
    def criar_apartir_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)
    
    @staticmethod # -> transforma em método estático
    def e_maior_idade(idade):
        return idade >= 18

p = Pessoa('bruno', 25)
print(p.nome, p.idade)

p2 = Pessoa.criar_apartir_data_nascimento(1998, 8, 11, 'Bruno')
print(p2.nome, p2.idade)

p3 = Pessoa.e_maior_idade(20)
print(p3)
p3 = Pessoa.e_maior_idade(17)
print(p3)
#-------------------------------------------------------------------------------------------------------------------------
# Interfaces o que são: O conceito é definir um contrato, onde são declarados os métodos (o que deve ser feito) e suas respectivas assinaturas. Em Python utilizamos classes abstratas para criar contratos. Classes abstratas não podem ser instanciadas.
# Classes Abstratas: 

from abc import ABC, abstractmethod

class Controle_remoto(ABC):
    @abstractmethod
    def ligar(self):
        pass
 
    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractmethod
    def marca(self):
        pass

class Controle_tv(Controle_remoto):
    def ligar(self):
        print('Ligando a TV')

    def desligar(self):
        print('Desligando a TV')

    @property
    def marca(self):
        return "Samsung"

class Controle_ar_condicionado(Controle_remoto):
    def ligar(self):
        print('Ligando o Ar condicionado')

    def desligar(self):
        print('Desligando o Ar condicionado')

    @property
    def marca(self):
        return "Panasonic"

controle = Controle_tv()
controle.ligar()
controle.desligar()
print(controle.marca)

controle_ar = Controle_ar_condicionado()
controle_ar.ligar()
controle_ar.desligar()
print(controle_ar.marca)