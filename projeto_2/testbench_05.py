from package.maths.controllers import WhiteBoard
from package.maths.terms import Circulo, Ponto, Quadrado, Segmento, Triangulo


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

    # circulo_1.model()

    quadro.remove_forma("circulo0")
    quadro.print_formas()

    circulo = Circulo(3, 2, 2)
    quadro.adiciona_forma(circulo)
    quadro.print_details("ponto1")
    quadro.print_formas()

    ponto_cpy = quadro.seleciona_forma("ponto1")
    ponto_cpy.model()

    print('='*30)
    print(f'A distância entre o ponto1 e o circulo2 é: '
          f'{quadro.distancia("ponto1", "circulo2"):.2f}')
    
    quadro.interferencia("ponto1", "circulo2")
    print('='*30)

    quadrado = Quadrado(1, 1, 2)
    quadro.adiciona_forma(quadrado)
    quadro.print_formas()
    quadro.print_details("quadrado3")

    print(f'A distância entre o ponto1 e o quadrado3 é: ' 
          f'{quadro.distancia("ponto1", "quadrado3")}')
    quadro.interferencia("ponto1", "quadrado3")

    segmento = Segmento(3, 3, 2, 2)
    segmento.model()
    quadro.adiciona_forma(segmento)
    print(f'{segmento.comprimento():.2f}')
    quadro.print_formas()
    print(f'A distância entre o ponto1 e o segmento4 é: '
          f'{quadro.distancia("ponto1", "segmento4"):.2f}')
    quadro.interferencia("ponto1", "segmento4")


if __name__ == "__main__":
    print("O arquivo testbench_05.py foi invocado como programa")
    print("-"*30)
    workspace()
else:
    print("O arquivo testbench_05.py foi invocado como módulo")
    print("-"*30)
    workspace()
