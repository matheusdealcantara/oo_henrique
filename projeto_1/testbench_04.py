from package.maths.terms import Triangulo


def workspace():
    triangulo = Triangulo(4, 2, 3, 5)
    triangulo.model()
    print(f'A área do triângulo é: {triangulo.area()}')
    print(f'O perímetro do triângulo é: {triangulo.perimetro()}')

    print('='*30)

    triangulo.x = 3
    triangulo.y = 4
    triangulo.base = 7
    triangulo.altura = 8

    triangulo.model()
    print(f'A área do triângulo é: {triangulo.area()}')
    print(f'O perímetro do triângulo é: {triangulo.perimetro()}')


if __name__ == '__main__':
    print("O arquivo 'testbench_04.py' foi invocado como programa")
    print(f"__name__ == {__name__}")
    workspace()
else:
    print("O arquivo 'testbench_04.py' foi invocado como modulo")
    print(f'__name__ == {__name__}')
