from package.maths.terms import Reta


def workspace():
    meu_primeiro_objeto = Reta(2, 3)
    meu_primeiro_objeto.a = 2
    meu_primeiro_objeto.b = 3
    meu_primeiro_objeto.model()
    print(f'Interpolando o número 4 na reta: '
          f'y = {meu_primeiro_objeto.interpolar(4)}')


if __name__ == "__main__":
    print("O arquivo 'testbench_01.py' foi invocado como programa")
    print(f"__name__ == {__name__}")
    workspace()
else:
    print("O arquivo 'testbench_01.py' foi invocado como modulo")
    print(f'__name__ == {__name__}')
