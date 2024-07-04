# Autor: Matheus de Alcântara
from package.maths.terms import Circulo, Ponto, Quadrado, Reta, WhiteBoard


def workspace():
    input("Pressione Enter para iniciar a área de trabalho ")
    print("A área de trabalho foi invocada")
    quadro = WhiteBoard()
    while (input("Deseja adicionar uma forma geométrica? (s/n) ") == "s"):
        print("As formas geométricas disponíveis são: Circulo, Ponto e Reta")
        forma = input("Digite a forma geométrica desejada:\
(1 - Circulo, 2 - Ponto, 3 - Reta, 4 - Quadrado) ")
        switch = {
            "1": Circulo,
            "2": Ponto,
            "3": Reta,
            "4": Quadrado
        }
        if forma in switch:
            x = int(input("Digite a coordenada x: "))
            y = int(input("Digite a coordenada y: "))
            if forma == "1":
                raio = int(input("Digite o raio do círculo: "))
                circulo = switch[forma](raio, x, y)
                quadro.adiciona_forma(circulo.name, circulo._x, circulo._y)
                quadro.print_formas()
            elif forma == "2":
                ponto = switch[forma](x, y)
                quadro.adiciona_forma(ponto.name, ponto._x, ponto._y)
                quadro.print_formas()
            elif forma == "3":
                a = int(input("Digite o coeficiente angular da reta: "))
                b = int(input("Digite o coeficiente linear da reta: "))
                reta = switch[forma](a, b)
                quadro.adiciona_forma(reta.name, reta._a, reta._b)
                quadro.print_formas()
            elif forma == "4":
                lado = int(input("Digite o lado do quadrado: "))
                quadrado = switch[forma](lado, x, y)
                quadro.adiciona_forma(quadrado.name, quadrado._x, quadrado._y)
                quadro.print_formas()


if __name__ == "__main__":
    print("Main foi invocado como programa")
    print("-"*30)
    workspace()
else:
    print("Main foi invocado como módulo")
    print("-"*30)
    workspace()
