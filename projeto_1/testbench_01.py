from package.maths.terms import Reta


def workspace():
    reta1 = Reta(2, 3)
    reta1.model()
    print(f'Interpolando o número 4 na reta: '
          f'y = {reta1.interpolar(4)}')

    reta1.a = -5
    reta1.b = -4
    print(f'Interpolando o número 4 na reta: '
          f'y = {reta1.interpolar(4)}')


if __name__ == "__main__":
    print("O arquivo 'testbench_01.py' foi invocado como programa")
    print(f"__name__ == {__name__}")
    workspace()
else:
    print("O arquivo 'testbench_01.py' foi invocado como modulo")
    print(f'__name__ == {__name__}')
