from package.maths.terms import Triangulo


def workspace():
    triangulo = Triangulo(4, 2, 3, 5)
    triangulo.model()
    return


if __name__ == '__main__':
    print("O arquivo 'testbench_04.py' foi invocado como programa")
    print(f"__name__ == {__name__}")
    workspace()
else:
    print("O arquivo 'testbench_04.py' foi invocado como modulo")
    print(f'__name__ == {__name__}')
