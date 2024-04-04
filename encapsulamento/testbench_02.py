from package.maths.terms import Circulo

def workspace():
    meu_circulo = Circulo(2, 2)
    meu_circulo.setX(3)
    meu_circulo.setY(4)
    print(f'O raio do círculo é igual: {meu_circulo.raio()}')
    print(f'A área do círculo é igual: {meu_circulo.area()}')
    print(f'O diametro do circulo é: {meu_circulo.diametro()}')
    print(f'A circunferencia do círculo é: {meu_circulo.circunferencia()}')

if __name__ == "__main__":
    print("O arquivo 'testbench_01.py' foi invocado como programa")
    print(f"__name__ == {__name__}")
    workspace()
else:
    print("O arquivo 'testbench_01.py' foi invocado como modulo")
    print(f'__name__ == {__name__}')
