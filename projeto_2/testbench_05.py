from package.maths.controllers import WhiteBoard
from package.maths.terms import Circulo, Ponto


def workspace():
    quadro = WhiteBoard()
    circulo_1 = Circulo(3, 2, 2)
    ponto_1 = Ponto(1, 2)

    quadro.adiciona_forma(circulo_1)
    quadro.adiciona_forma(ponto_1)

    quadro.print_formas()

    circulo_1.model()
    ponto_1.model()

    quadro.atualiza_forma("circulo0", 3, 3, 4)

    circulo_1.model()

    quadro.remove_forma("circulo0")
    quadro.print_formas()
    quadro.print_details("ponto1")

    ponto_cpy = quadro.seleciona_forma("ponto1")
    ponto_cpy.model()
    quadro.distancia(ponto_1, circulo_1)
    
    # quadro.interferencia("ponto1", "circulo0")


if __name__ == "__main__":
    print("O arquivo testbench_05.py foi invocado como programa")
    print("-"*30)
    workspace()
else:
    print("O arquivo testbench_05.py foi invocado como módulo")
    print("-"*30)
    workspace()
