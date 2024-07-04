from package.maths.terms import Quadrado


def workspace():
    quadrado_1 = Quadrado(3, 4, 2)
    quadrado_1.model()
    print(f'A área do quadrado é igual: {quadrado_1.area()}')	


if __name__ == "__main__":
    print("O arquivo 'testbench_01.py' foi invocado como programa")
    print(f"__name__ == {__name__}")
    workspace()
else:
    print("O arquivo 'testbench_01.py' foi invocado como modulo")
    print(f'__name__ == {__name__}')
