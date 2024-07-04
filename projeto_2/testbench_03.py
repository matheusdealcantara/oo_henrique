from package.maths.terms import Circulo, Ponto, WhiteBoard


def workspace():
    quadro = WhiteBoard()
    circulo_1 = Circulo(3, 2, 2)
    ponto_1 = Ponto(1, 2)

    circulo_1.model()
    ponto_1.model()
    quadro.adiciona_forma(circulo_1.__name, circulo_1._x, circulo_1._y)
    quadro.print_formas()
    quadro.adiciona_forma(ponto_1.__name, ponto_1._x, ponto_1._y)
    print("=========================")
    quadro.print_formas()


if __name__ == "__main__":
    print("Testbench 03 foi invocado como programa")
    print("-"*30)
    workspace()
else:
    print("Testbench 03 foi invocado como módulo")
    print("-"*30)
    workspace()
