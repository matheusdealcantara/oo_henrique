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
    
class Circulo:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        
    def setX(self, x):
        if type(x) == int:
            self.__x = x
        else:
            self.__x = 0
            
    def getX(self):
        return self.__x
    
    def setY(self, y):
        if type(y) == int:
            self.__y = y
        else:
            self.__y = 0
            
    def getY(self):
        return self.__y
    
    def raio(self):
        return sqrt((self.__x**2 + self.__y**2))
    
    def diametro(self):
        return sqrt((self.__x**2 + self.__y**2))*2
    
    def area(self):
        return pi*(sqrt((self.__x**2 + self.__y**2))**2)
    
    def circunferencia(self):
        return 2*pi*sqrt((self.__x**2 + self.__y**2))
   
class Ponto:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y 
        
    def setX(self, x):
        if type(x) == int:
            self.__x = x
        else:
            self.__x = x
    
    def getX(self, x):
        return self.__x   
    
    def setY(self, y):
        if type(y) == int:
            self.__y = y
        else:
            self.__y = y
    
    def getY(self, y):
        return self.__y  