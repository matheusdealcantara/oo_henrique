from package.maths.terms import Ponto


def workspace():
    ponto_1 = Ponto(3, 1)
    ponto_1.model()

    ponto_1.x = 4
    ponto_1.y = 5

    ponto_1.model()

    ponto_1.x = -3
    ponto_1.y = -2

    ponto_1.model()


if __name__ == "__main__":
    print("O arquivo 'testbench_01.py' foi invocado como programa")
    print(f"__name__ == {__name__}")
    workspace()
else:
    print("O arquivo 'testbench_01.py' foi invocado como modulo")
    print(f'__name__ == {__name__}')
