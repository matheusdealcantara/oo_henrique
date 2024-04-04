from math import pi, sqrt

class Reta: 
    
    def __init__(self, a, b) -> None:
        self.__a = a
        self.__b = b
        
    def setA(self, a):
        if type(a) == int:
            self.__a = a
        else:
            self.__a = 0
        
    def getA(self):
        return self.__a
    
    def setB(self, b):
        if type(b) == int:
            self.__b = b
        else:
            self.__b = 0
        
    def interpolar(self, x):
        y = self.__a * x + self.__b
        return y
    
    def model(self):
        print(f"Os parâmetros do modelo de reta são: a={self.__a} e b={self.__b}")
    
class Parabola:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def interpolar(self, x):
        y = self.a*(x**2) + self.b*x + self.c
        return y
    
class Ponto:
    def __init__(self, x, y, cor):
        self._x = x
        self._y = y 
        self.__cor = cor
        
    def setX(self, x):
        if type(x) == int:
            self._x = x
        else:
            self._x = x
    
    def getX(self):
        return self._x   
    
    def setY(self, y):
        if type(y) == int:
            self._y = y
        else:
            self._y = y
    
    def getY(self):
        return self._y  
    
    def setCor(self, cor):
        self.__cor = cor
        
    def getCor(self):
        return self.__cor

class Circulo(Ponto):
    def __init__(self, raio, x, y, cor):
        super().__init__(x, y, cor)
        self.__raio = raio
        
    def setRaio(self, raio):
        if type(raio) == int:
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
   