from math import sqrt

from package.maths.terms import Circulo, Ponto, Quadrado, Triangulo


class WhiteBoard():
    def __init__(self):
        self.formas = {}
        self.count = 0

    def seleciona_forma(self, forma):
        for i in self.formas:
            if i.lower() == forma.lower():
                return self.formas[i]

    def adiciona_forma(self, forma):
        try:
            nome = forma._name + str(self.count)
            self.formas[nome] = forma
            self.count += 1
            print(f"{forma._name} adicionado com sucesso")
        except Exception as e:
            print(f"Erro ao adicionar forma: {e}")

    def remove_forma(self, forma):
        try:
            for i in self.formas:
                if i.lower() == forma.lower():
                    del self.formas[i]
                    print(f"{forma} removido com sucesso")
                    break
        except Exception as e:
            print(f"Erro ao remover forma: {e}")

    def print_formas(self):
        print("="*30)
        print("Formas adicionadas: ")
        for i in self.formas.keys():
            print(i)
        print("="*30)

    def atualiza_forma(self, forma, x, y, raio=None, lado=None,
                       base=None, altura=None):
        try:
            for i in self.formas:
                if i.lower() == forma.lower():
                    forma1 = self.formas[i]
                    break
            forma1.x = x
            forma1.y = y
            if raio:
                forma1.raio = raio
            elif lado:
                forma1.lado = lado
            elif base and altura:
                forma1.base = base
                forma1.altura = altura
            print(f"{forma} atualizada com sucesso")
        except Exception as e:
            print(f"Erro ao atualizar forma: {e}")

    def print_details(self, forma):
        for i in self.formas:
            if i.lower() == forma.lower():
                forma1 = self.formas[i]
                break
        print("="*30)
        forma1.model()
        if (forma[0] != 'p'):
            print(f"Área: {forma1.area()}")
        print("="*30)
    
    def distancia(self, forma1, forma2):
        if forma1 and forma2:
            return sqrt((forma2.x - forma1.x)**2 + (forma2.y - forma1.y)**2)
        else:
            print("Forma geométrica não encontrada")
            return 1
           
    def interferencia(self, forma1, forma2):
        forma_1 = self.seleciona_forma(forma1)
        forma_2 = self.seleciona_forma(forma2)

        if (forma1[0] == 'p' and forma2[0] == 'p'):
            if (self.distancia(forma_1, forma_2) == 0):
                print(f"{forma1} e {forma2} estão no mesmo ponto")
            else:
                print(f"{forma1} e {forma2} não estão no mesmo ponto")
        elif (forma1[0] == 'p' and forma2[0] == 'c'):
            if (self.distancia(forma_1, forma_2) <= forma_2.raio):
                print(f"{forma1} está dentro de {forma2}")
            else:
                print(f"{forma1} não está dentro de {forma2}")
        elif (forma1[0] == 'p' and forma2[0] == 'q'):
            if (self.distancia(forma_1, forma_2) <= forma_2.lado):
                print(f"{forma2} está dentro de {forma1}")
            else:
                print(f"{forma2} não está dentro de {forma1}")
        else:
            if (self.distancia(forma_1, forma_2) <= forma_1.raio + forma_2.raio):
                print(f"{forma1} e {forma2} estão em contato")
            else:
                print(f"{forma1} e {forma2} não estão em contato")


class Menu(WhiteBoard):
    def __init__(self):
        super().__init__()
        self.options = {
            "1": self.create,
            "2": self.read,
            "3": self.update,
            "4": self.delete,
            "5": exit
        }

    def create(self):
        print("As formas geométricas disponíveis são: "
              "Circulo, Ponto, Quadrado e Triangulo")
        forma = input("Digite a forma geométrica desejada:\n"
                      "(1 - Circulo, 2 - Ponto, 3 - Quadrado, 4 - Triangulo) ")
        switch = {
            "1": Circulo,
            "2": Ponto,
            "3": Quadrado,
            "4": Triangulo
        }
        if forma in switch:
            x = int(input("Digite a coordenada x: "))
            y = int(input("Digite a coordenada y: "))
            if forma == "1":
                raio = int(input("Digite o raio do círculo: "))
                circulo = switch[forma](raio, x, y)
                self.adiciona_forma(circulo)
                self.print_formas()
            elif forma == "2":
                ponto = switch[forma](x, y)
                self.adiciona_forma(ponto)
                self.print_formas()
            elif forma == "3":
                lado = int(input("Digite o lado do quadrado: "))
                quadrado = switch[forma](lado, x, y)
                self.adiciona_forma(quadrado)
                self.print_formas()
            elif forma == "4":
                base = int(input("Digite a base do triângulo: "))
                altura = int(input("Digite a altura do triângulo: "))
                triangulo = switch[forma](base, altura, x, y)
                self.adiciona_forma(triangulo)
                self.print_formas()

    def update(self):
        forma = input("Digite o nome da forma "
                      "geométrica que deseja atualizar: ")
        x = int(input("Digite a nova coordenada x: "))
        y = int(input("Digite a nova coordenada y: "))
        if (forma[0].lower() == "c"):
            raio = int(input("Digite o novo raio do círculo: "))
            self.atualiza_forma(forma, x, y, raio=raio)
        elif (forma[0].lower() == "p"):
            self.atualiza_forma(forma, x, y)
        elif (forma[0].lower == "q"):
            lado = int(input("Digite o novo lado do quadrado: "))
            self.atualiza_forma(forma, x, y, lado=lado)
        elif (forma[0].lower == "t"):
            base = int(input("Digite a nova base do triângulo: "))
            altura = int(input("Digite a nova altura do triângulo: "))
            self.atualiza_forma(forma, x, y, base=base, altura=altura)
        else:
            print("Forma geométrica inválida!")
        # self.atualiza_forma()
        pass

    def delete(self):
        forma = input("Digite o nome da forma geométrica que deseja remover: ")
        self.remove_forma(forma)
        self.print_formas()

    def read(self):
        self.print_formas()

    def run(self):
        while True:
            print("Escolha uma das opções:")
            print("1. Adicionar forma geométrica")
            print("2. Imprimir formas geométricas")
            print("3. Atualizar forma geométrica")
            print("4. Remover forma geométrica")
            print("5. Sair")
            option = input("Digite o número da opção desejada: ")
            if option.isdigit() and int(option) in range(1, 6):
                command = list(self.options.keys())[int(option)-1]
                self.options[command]()
            else:
                print("Opção inválida! Tente novamente.")
