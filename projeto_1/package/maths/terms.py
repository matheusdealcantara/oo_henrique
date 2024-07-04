from math import pi


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
        print(f'A coordenada do {__class__.__name__} é: ({self._x}, {self._y})')


class Reta(): 
    def __init__(self, a, b) -> None:
        self.__a = a
        self.__b = b
        
    def setA(self, a):
        if isinstance(a, int):
            self.__a = a
        else:
            self.__a = 0

    def getA(self):
        return self.__a
    
    def setB(self, b):
        if isinstance(b, int):
            self.__b = b
        else:
            self.__b = 0

    def getB(self):
        return self.__b    

    def interpolar(self, x):
        y = self.__a * x + self.__b
        return y
    
    def model(self):
        print(f"Os parâmetros do modelo de reta são: \
a = {self.__a} e b = {self.__b}")


class Circulo(Ponto):
    def __init__(self, raio, x, y):
        super().__init__(x, y)
        self.__raio = raio
        self.name = "Circulo"
        
    def setRaio(self, raio):
        if isinstance(raio, int):
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
    

class Quadrado(Ponto):
    def __init__(self, x, y, lado):
        super().__init__(x, y)
        self.lado = lado
    
    def area(self):
        return self.lado**2
    
    def model(self):
        print(f'A coordenada do Quadrado é: ({self._x}, {self._y}) \
e seu lado: ({self.lado})')
        

