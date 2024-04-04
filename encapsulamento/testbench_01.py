from package.maths.terms import Reta, Parabola, Circulo

def workspace():
    # meu_primeiro_objeto = Reta(2, 3)
    # meu_primeiro_objeto.setA(3)
    # meu_primeiro_objeto.setB(3)
    # meu_primeiro_objeto.model()
    # print(f'Interpolando o número 4 na reta: y = {meu_primeiro_objeto.interpolar(4)}')
    
    
    # meu_segundo_objeto = Parabola(2, 3, 4)
    # print(f'Interpolando o número 4 na parábola: y = {meu_segundo_objeto.interpolar(4)}')
    
    
    meu_circulo = Circulo(2, 2)
    meu_circulo.setA(3)
    meu_circulo.setB(4)
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

