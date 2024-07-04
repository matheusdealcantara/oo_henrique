from package.maths.terms import Circulo


def workspace():
    meu_circulo = Circulo(2, 2, 2)
    meu_circulo.setX(3)
    meu_circulo.setY(4)
    meu_circulo.setRaio(5)
    meu_circulo.model()
    print(f'A área do círculo é igual: {meu_circulo.area():.2f}')
    print(f'O diametro do circulo é: {meu_circulo.diametro():.2f}')
    print(f'A circunferencia do círculo é: {meu_circulo.circunferencia():.2f}')


if __name__ == "__main__":
    print("O arquivo 'testbench_02.py' foi invocado como programa")
    print(f"__name__ == {__name__}")
    workspace()
else:
    print("O arquivo 'testbench_02.py' foi invocado como modulo")
    print(f'__name__ == {__name__}')
