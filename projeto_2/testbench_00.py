from package.maths.terms import Ponto


def workspace():
    ponto_1 = Ponto(3, 1)

    ponto_1.model()


if __name__ == "__main__":
    print("O arquivo 'testbench_00.py' foi invocado como programa")
    workspace()
else:
    print("O arquivo 'testbench_00.py' foi invocado como modulo")
    workspace()