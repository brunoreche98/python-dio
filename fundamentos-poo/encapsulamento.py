class Conta:
    def __init__(self, numero_agencia, saldo=0):
        self._saldo = saldo
        self.numero_agencia = numero_agencia

    def depositar(self, valor):
        self._saldo += valor
        
    def sacar(self, valor):
        self._saldo -= valor

    def mostrar_saldo(self):
        return self._saldo
    # Método onde pode-se acessar os dados/variáveis que são privadas

conta = Conta("0001", 8000)
# Conta.depositar(50)
print(conta.numero_agencia)
# print(conta._saldo) -> _ sugere que o atributo saldo é privado e logo não deve ser acessado fora do escopo da Classe.
print(conta.mostrar_saldo()) # -> retorno do meu saldo
#----------------------------------------------------------------------------------------------------------------------
# -------------- Properties --------------
class Foo:
    def __init__(self, variavel_privada=None):
        self._variavel_privada = variavel_privada

    @property # -> getter (leitura)
    def variavel_privada(self):
        return self._variavel_privada or 0
    
    @variavel_privada.setter # -> setter (modifica)
    def variavel_privada(self, value):
        self._variavel_privada += value

    @variavel_privada.deleter
    def variavel_privada(self):
        self._variavel_privada = -1
    
foo = Foo(10)
print(foo.variavel_privada)
foo.variavel_privada = 30
print(foo.variavel_privada)
del foo.variavel_privada
print(foo.variavel_privada)