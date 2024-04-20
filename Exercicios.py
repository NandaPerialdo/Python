class Exercicios:
    def __init__(self):
        # Construtor, quando nao precisar delcarar as variaveis, usar pass
        self.num = 0
        self.num1 = 0
        self.num2 = 0
        self.i = 0
        self.resultado = 0

    def somar(self):
        return f"{self.num1} + {self.num2} = {self.num1 + self.num2}"

    def subtrair(self):
        return f"{self.num1} - {self.num2} = {self.num1 - self.num2}"

    def dividir(self):
        if(self.num2 == 0):
            return "Impossivel dividir por zero"
        else:
            return f"{self.num1} / {self.num2} = {self.num1 / self.num2}"

    def multiplicar(self):
        return f"{self.num1} * {self.num2} = {self.num1 * self.num2}"

    def contarDez(self):
        self.i = 1
        for self.i in range (1, 11):
            print(self.i)

    def paresVinte(self):
        self.i = 1
        for self.i in range(1, 21):
            if self.i % 2 == 0:
                print(self.i)

    def somarCem(self):
        self.i = 0
        for self.i in range(1, 101):
            self.resultado += self.i
            print(self.resultado)

    def multCinco(self):
        self.i = 1
        for self.i in range(1, 51):
            if self.i % 5 == 0:
                print(self.i)

    def parImpar(self):
        if self.num % 2 ==











