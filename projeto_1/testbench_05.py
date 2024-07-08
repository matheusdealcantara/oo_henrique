from package.maths.terms import Circulo, Ponto, Quadrado, Quadro, Triangulo


def workspace():
    p1 = Ponto(1, 2)
    circle1 = Circulo(2, 2, 2)
    quadrado1 = Quadrado(3, 4, 2)
    triangulo1 = Triangulo(5, 6, 3, 4)

    quadro1 = Quadro()
    quadro1.adiciona_forma(p1, p1.x, p1.y)
    quadro1.adiciona_forma(circle1, circle1.x, circle1.y)
    quadro1.adiciona_forma(quadrado1, quadrado1.x, quadrado1.y)
    quadro1.adiciona_forma(triangulo1, triangulo1.x, triangulo1.y)

    quadro2 = Quadro()
    quadro2.adiciona_forma(p1, p1.x, p1.y)
    quadro2.adiciona_forma(circle1, circle1.x, circle1.y)
    quadro2.adiciona_forma(quadrado1, quadrado1.x, quadrado1.y)
    quadro2.adiciona_forma(triangulo1, triangulo1.x, triangulo1.y)
    
    print('-'*15)
    print('Quadro 1')
    print('-'*15)
    
    for forma in quadro1.formas:
        print(forma)

    print('-'*15)
    print('Quadro 2')
    print('-'*15)

    for forma in quadro2.formas:
        print(forma)


if __name__ == "__main__":
    print("O arquivo 'testbench_05.py' foi invocado como programa")
    print(f"__name__ == {__name__}")
    workspace()
else:
    print("O arquivo 'testbench_05.py' foi invocado como modulo")
    print(f'__name__ == {__name__}')