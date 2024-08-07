from package.maths.terms import Circulo, Ponto, WhiteBoard


def workspace():
    quadro = WhiteBoard()
    circulo_1 = Circulo(3, 2, 2)
    ponto_1 = Ponto(1, 2)

    circulo_1.model()
    ponto_1.model()
    quadro.adiciona_forma(circulo_1.name, circulo_1._x, circulo_1._y)
    quadro.print_formas()
    quadro.adiciona_forma("ponto", ponto_1._x, ponto_1._y)
    print("=========================")
    quadro.print_formas()


if __name__ == "__main__":
    workspace()