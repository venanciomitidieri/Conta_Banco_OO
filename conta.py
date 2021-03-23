""" No primeiro onde fica o construtor __initi__ é tudo que é a CONTA TEM, nos proximos def (metodos) será o que a
CONTA FAZ """


class Conta:

    def __init__(self, numero, titular, saldo, limite):    # Atributos
        print(f'Construindo objeto... {self}')
        self.__numero = numero        # Colocar dois "Underscore" __ na frente da classe, significa que ela é privada.
        self.__titular = titular
        # Para acessar os atributos da função eu devo fazer ._Conta__saldo. Pra facilitar esse caminhos podemos criar
        # os getter e setter mais conhecido no Python como @property e @setter
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):     # Metodos, Funções
        print(f'Saldo {self.__saldo} do titular {self.__titular}')

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print(f'O valor {valor} passou o limite')

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    # O get serve para quando eu quero retornar um valor do objeto.
    # O set serve para alterar um valor, como só o limite será alerado foi somente pra ele.
    # No Python usamos muito o @property para facilitar ainda mais a chamada e edição das variaveis.
    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return '001'

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}


'''
Além desse princípio de responsabilidade única existem outras que foram definidos através do Robert C. Martin no
início dos anos 2000 e são conhecidos pelo acrônimo SOLID:

S - Single responsibility principle
O - Open/closed principle
L - Liskov substitution principle
I - Interface segregation principle
D - Dependency inversion principle
'''

'''
OBSERVAÇÕES:

1 - @staticmethod são metodos estaticos que usamos para quando queremos acessar um metodo sem ter criado um objeto
2 - @property utilizado para chamar um atributo atravez do metodo sem necessidade de colocar o get.
3 - Métodos estáticos devem ser usados com cautela caso contrário pode-se fugir do paradigma da orientação a objetos.
Métodos estáticos tem um cheiro de linguagem procedural já que independe de um objeto para ser chamado e não manipula
informações/atributos de objetos. Deve ser usado com bastante cautela!
4 - 
'''