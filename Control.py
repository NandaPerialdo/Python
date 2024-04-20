from Exercicios import Exercicios

class Control:
    def __init__(self):
        self.opcao = -1
        self.exer = Exercicios()

    def coletar1(self):
        self.exer.num = int(input("Informe um numero: "))

    def coletar2(self):
        self.exer.num1 = int(input("Informe o primeiro numero: "))
        self.exer.num2 = int(input("informe o segundo numero: "))

    def menu(self):
        self.opcao = int(input("----- Menu ------\n\n" +
                "\n0. Sair" +
                "\n1. Somar" +
                "\n2. Subtrair" +
                "\n3. Dividir" +
                "\n4. Multiplicar" +
                "\n5. Contar até 10" +
                "\n6. Imprima os números pares de 1 a 20" +
                "\n7. Soma dos números de 1 a 100" +
                "\n8. Imprima os múltiplos de 5 de 1 a 50" +
                "\n9. Imprima se é par ou ímpar" +
                "\nEscolha uma das opções acima: "))

    def operacao(self):
        while(self.opcao != 0):
            self.menu()#mostrar menu
            if(self.opcao == 0):
                print("Obrigado!")
            elif(self.opcao == 1):
                self.coletar2()
                print(self.exer.somar())
            elif(self.opcao == 2):
                self.coletar2()
                print(self.exer.subtrair())
            elif(self.opcao == 3):
                self.coletar2()
                print(self.exer.dividir())
            elif(self.opcao == 4):
                self.coletar2()
                print(self.exer.multiplicar())
            elif(self.opcao == 5):
                print(self.exer.contarDez())
            elif(self.opcao == 6):
                print(self.exer.paresVinte())
            elif(self.opcao == 7):
                print(self.exer.somarCem())
            elif(self.opcao == 8):
                print(self.exer.multCinco())
            elif(self.opcao == 9):
                self.coletar1()
                print(self.exer.parImpar())
            else:
                print("Código escolhido nao é valido")

