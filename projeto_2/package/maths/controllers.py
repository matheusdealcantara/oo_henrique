from math import sqrt

from package.maths.terms import Circulo, Ponto, Quadrado, Segmento, Triangulo


class WhiteBoard():
    def __init__(self):
        self.formas = {}
        self.count = 0

    def seleciona_forma(self, forma):
        try:
            for i in self.formas:
                if i.lower() == forma.lower():
                    return self.formas[i]
        except Exception as e:
            print(f"Erro ao selecionar forma: {e}")

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
        if len(self.formas) == 0:
            print("Não há formas adicionadas")
            print("="*30)
            return
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
            print("="*30)
            print(f"{forma} atualizado com sucesso")
            forma1.model()
            print("="*30)
        except Exception as e:
            print(f"Erro ao atualizar forma: {e}")

    def distancia(self, forma1, forma2):
        forma_1 = self.seleciona_forma(forma1)
        forma_2 = self.seleciona_forma(forma2)

        if isinstance(forma_2, Segmento):
            distancia1 = sqrt((forma_1.x - forma_2.x1)**2
                              + (forma_1.y - forma_2.y1)**2)
            distancia2 = sqrt((forma_1.x - forma_2.x2)**2
                              + (forma_1.y - forma_2.y2)**2)
            return distancia1 + distancia2
        if forma_1 and forma_2:
            return sqrt((forma_2.x - forma_1.x)**2
                        + (forma_2.y - forma_1.y)**2)
        else:
            print("Forma geométrica não encontrada")
            return 1

    def interferencia(self, forma1, forma2):
        try:
            forma_1 = self.seleciona_forma(forma1)
            forma_2 = self.seleciona_forma(forma2)
        except Exception as e:
            print(f"Erro ao verificar interferência: {e}")

        print("="*30)
        if (forma1[0] == 'p' and forma2[0] == 'p'):
            if (self.distancia(forma1, forma2) == 0):
                print(f"{forma1} e {forma2} estão no mesmo ponto")
            else:
                print(f"{forma1} e {forma2} não estão no mesmo ponto")
        elif (forma1[0] == 'p' and forma2[0] == 'c'):
            if (self.distancia(forma1, forma2) <= forma_2.raio):
                print(f"{forma1} está dentro de {forma2}")
            else:
                print(f"{forma1} não está dentro de {forma2}")
        elif (forma1[0] == 'p' and forma2[0] == 'q'):
            if (self.distancia(forma1, forma2) <= forma_2.lado/2 and
                    self.distancia(forma1, forma2) <= forma_2.diagonal()/2):
                print(f"{forma1} está dentro de {forma2}")
            else:
                print(f"{forma2} não está dentro de {forma1}")
        elif (forma1[0] == 'p' and forma2[0] == 't'):
            if (self.distancia(forma1, forma2) <= forma_2.base/2 and
                    self.distancia(forma1, forma2) <= forma_2.altura/2):
                print(f"{forma1} está dentro de {forma2}")
            else:
                print(f"{forma1} não está dentro de {forma2}")
        elif (forma1[0] == 'p' and forma2[0] == 's'):
            if (self.distancia(forma1, forma2) == forma_2.comprimento()):
                print(f"{forma1} pertence ao {forma2}")
            else:
                print(f"{forma1} não pertence ao {forma2}")
        else:
            if (self.distancia(forma1, forma2) <= forma_1.raio + forma_2.raio):
                print(f"{forma1} e {forma2} estão em contato")
            else:
                print(f"{forma1} e {forma2} não estão em contato")
        print("="*30)


class Menu(WhiteBoard):

    def __init__(self):
        self.quadro = WhiteBoard()
        self.options = {
            "1": self.create,
            "2": self.read,
            "3": self.update,
            "4": self.delete,
            "5": self.interferencia,
            "6": self.distancia,
            "7": exit,
            "8": self.tutorial
        }

    count = 0
    if count == 0:
        def tutorial(self):
            print("="*30)
            print("Tutorial de uso:")
            print("1. Adicionar forma geométrica: Adiciona uma forma "
                  "geométrica ao quadro branco")
            print("2. Imprimir formas geométricas: Imprime as formas "
                  "geométricas adicionadas ao quadro branco")
            print("3. Atualizar forma geométrica: Atualiza as coordenadas "
                  "de uma forma geométrica adicionada ao quadro branco")
            print("4. Remover forma geométrica: Remove uma forma geométrica "
                  "adicionada ao quadro branco")
            print("5. Verificar interferência entre formas geométricas: "
                  "Verifica se uma forma geométrica está dentro de outra")
            print("6. Calcular distância entre formas geométricas: Calcula a "
                  "distância entre duas formas geométricas")
            print("7. Sair: Encerra o programa")
            print("="*30)
            print("Para utilizar as funções que solicitam o nome da forma "
                  "geométrica, utilize o nome da forma seguido do número de "
                  "identificação, por exemplo: Circulo0")
            print("="*30)

    def create(self):
        print("As formas geométricas disponíveis são: "
              "Circulo, Ponto, Quadrado e Triangulo")
        forma = input("Digite a forma geométrica desejada "
                      "(1 - Circulo, 2 - Ponto, 3 - Quadrado, 4 - Triangulo, "
                      " 5 - Segmento de reta):")
        switch = {
            "1": Circulo,
            "2": Ponto,
            "3": Quadrado,
            "4": Triangulo,
            "5": Segmento
        }
        if forma in switch:
            if forma == "5":
                x1 = int(input("Digite a coordenada x1: "))
                y1 = int(input("Digite a coordenada y1: "))
                x2 = int(input("Digite a coordenada x2: "))
                y2 = int(input("Digite a coordenada y2: "))
                segmento = switch[forma](x1, y1, x2, y2)
                self.quadro.adiciona_forma(segmento)
                self.quadro.print_formas()
            else:
                x = int(input("Digite a coordenada x: "))
                y = int(input("Digite a coordenada y: "))
                if forma == "1":
                    raio = int(input("Digite o raio do círculo: "))
                    circulo = switch[forma](raio, x, y)
                    self.quadro.adiciona_forma(circulo)
                    self.quadro.print_formas()
                elif forma == "2":
                    ponto = switch[forma](x, y)
                    self.quadro.adiciona_forma(ponto)
                    self.quadro.print_formas()
                elif forma == "3":
                    lado = int(input("Digite o lado do quadrado: "))
                    quadrado = switch[forma](lado, x, y)
                    self.quadro.adiciona_forma(quadrado)
                    self.quadro.print_formas()
                elif forma == "4":
                    base = int(input("Digite a base do triângulo: "))
                    altura = int(input("Digite a altura do triângulo: "))
                    triangulo = switch[forma](base, altura, x, y)
                    self.quadro.adiciona_forma(triangulo)
                    self.quadro.print_formas()

    def update(self):
        if len(self.quadro.formas) == 0:
            print("="*30)
            print("Não há formas geométricas adicionadas")
            print("="*30)
            return
        forma = input("Digite o nome da forma "
                      "geométrica que deseja atualizar: ")
        x = int(input("Digite a nova coordenada x: "))
        y = int(input("Digite a nova coordenada y: "))
        if (forma[0].lower() == "c"):
            raio = int(input("Digite o novo raio do círculo: "))
            self.quadro.atualiza_forma(forma, x, y, raio=raio)
        elif (forma[0].lower() == "p"):
            self.quadro.atualiza_forma(forma, x, y)
        elif (forma[0].lower == "q"):
            lado = int(input("Digite o novo lado do quadrado: "))
            self.quadro.atualiza_forma(forma, x, y, lado=lado)
        elif (forma[0].lower == "t"):
            base = int(input("Digite a nova base do triângulo: "))
            altura = int(input("Digite a nova altura do triângulo: "))
            self.quadro.atualiza_forma(forma, x, y, base=base, altura=altura)
        else:
            print("Forma geométrica inválida!")

    def delete(self):
        if len(self.quadro.formas) == 0:
            print("="*30)
            print("Não há formas geométricas adicionadas")
            print("="*30)
            return
        forma = input("Digite o nome da forma geométrica que deseja remover: ")
        self.quadro.remove_forma(forma)
        self.quadro.print_formas()

    def read(self):
        self.quadro.print_formas()

    def interferencia(self):
        if len(self.quadro.formas) == 0:
            print("="*30)
            print("Não há formas geométricas adicionadas, adicione "
                  "pelo menos duas formas geométricas para verificar.")
            print("="*30)
            return
        elif len(self.quadro.formas) == 1:
            print("Adicione mais formas geométricas "
                  "para verificar interferência")
            return
        forma1 = input("Digite o nome do ponto a ser utilizado: ")
        forma2 = input("Digite o nome da forma geométrica a ser utilizada: ")
        self.quadro.interferencia(forma1, forma2)

    def distancia(self):
        print("="*30)
        if len(self.quadro.formas) == 0:
            print("Não há formas geométricas adicionadas, adicione "
                  "pelo menos duas formas geométricas para verificar.")
            return
        elif len(self.quadro.formas) == 1:
            print("Adicione mais formas geométricas "
                  "para verificar a distância")
            return
        forma1 = input("Digite o nome da primeira forma geométrica: ")
        forma2 = input("Digite o nome da segunda forma geométrica: ")
        print(f"A distância entre {forma1} e {forma2} é: "
              f"{self.quadro.distancia(forma1, forma2):.2f}")
        print("="*30)

    def run(self):
        count = 0
        if count == 0:
            self.tutorial()
        while True:
            print("Escolha uma das opções:")
            print("1. Adicionar forma geométrica")
            print("2. Imprimir formas geométricas")
            print("3. Atualizar forma geométrica")
            print("4. Remover forma geométrica")
            print("5. Verificar interferência entre formas geométricas")
            print("6. Calcular distância entre formas geométricas")
            print("7. Sair")
            print("8. Tutorial de uso")
            option = input("Digite o número da opção desejada: ")
            if option.isdigit() and int(option) in range(1, 9):
                command = list(self.options.keys())[int(option)-1]
                self.options[command]()
            else:
                print("Opção inválida! Tente novamente.")
