from math import pi


class Reta: 
    def __init__(self, a, b) -> None:
        self.__a = a
        self.__b = b
        
    def setA(self, a):
        if a is int:
            self.__a = a
        else:
            self.__a = 0
        
    def getA(self):
        return self.__a
    
    def setB(self, b):
        if b is int:
            self.__b = b
        else:
            self.__b = 0
        
    def interpolar(self, x):
        y = self.__a * x + self.__b
        return y
    
    def model(self):
        print(f"Os parâmetros do modelo de reta são: a={self.__a} e b={self.__b}")
        

class Ponto:
    def __init__(self, x, y):
        self._x = x
        self._y = y 
       
    def setX(self, x):
        if x is int:
            self._x = x
        else:
            self._x = x
   
    def getX(self):
        return self._x   
    
    def setY(self, y):
        if y is int:
            self._y = y
        else:
            self._y = y
    
    def getY(self):
        return self._y  
    
    def model(self):
        print(f'A coordenada do ponto é: ({self._x}, {self._y})')


class Circulo(Ponto):
    def __init__(self, raio, x, y):
        super().__init__(x, y)
        self.__raio = raio
        self.name = "Circulo"
        
    def setRaio(self, raio):
        if raio is int:
            self.__raio = raio
        else:
            self.__raio = 0 
            
    def getRaio(self):
        return self.__raio 

    def model(self):
        print(f'A coordenada do círculo é: ({self._x}, {self._y}) e seu raio é: {self.__raio}')

    def diametro(self):
        return self.__raio*2
    
    def area(self):
        return pi*(self.__raio**2)
    
    def circunferencia(self):
        return 2*pi*self.__raio
    
   
class WhiteBoard():
    def __init__(self):
        self.formas = []
        self.count = 0

    def adiciona_forma(self, forma, x, y):
        model = {
            'nome': f'{forma}_{self.count}',
            'x': x,
            'y': y,
        }
        self.formas.append(model)
        self.count += 1

    def print_formas(self):
        for i in self.formas:
            for j in i.items():
                print(j)    