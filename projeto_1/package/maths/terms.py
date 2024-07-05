from math import pi, sqrt


class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
       
    @property
    def x(self):
        return self._x

    @x.setter   
    def x(self, x):
        if isinstance(x, int) and x >= 0:
            self._x = x
        else:
            self._x = 0
   
    @property
    def y(self):
        return self._y
      
    @y.setter
    def y(self, y):
        if isinstance(y, int) and y >= 0:
            self._y = y
        else:
            self._y = 0
    
    def model(self):
        print(f'A coordenada do {__class__.__name__} é: ({self.x}, {self.y})')


class Reta(): 
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def a(self):
        return self._a

    @a.setter  
    def a(self, a):
        if isinstance(a, int) and a >= 0:
            self._a = a
        else:
            self._a = 0

    @property
    def b(self):
        return self._b    

    @b.setter
    def b(self, b):
        if isinstance(b, int) and b >= 0:
            self._b = b
        else:
            self._b = 0

    def interpolar(self, x):
        y = self.a * x + self.b
        return y
    
    def model(self):
        print(f"Os parâmetros do modelo de reta são: \
a = {self.a} e b = {self.b}")


class Circulo(Ponto):
    def __init__(self, raio, x, y):
        super().__init__(x, y)
        self.__raio = raio

    @property
    def raio(self):
        return self.__raio
    
    @raio.setter
    def raio(self, raio):
        if isinstance(raio, int) and raio >= 0:
            self.__raio = raio
        else:
            self.__raio = 0

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

    @property
    def lado(self):
        return self._lado
    
    @lado.setter
    def lado(self, lado):
        if isinstance(lado, int) and lado >= 0:
            self._lado = lado
        else:
            self._lado = 0

    def area(self):
        return self.lado**2

    def perimetro(self):
        return 4*self.lado
    
    def diagonal(self):
        return self.lado*sqrt(2)

    def model(self):
        print(f'A coordenada do Quadrado é: ({self._x}, {self._y}) \
e seu lado: {self.lado}')


class Triangulo(Ponto):
    def __init__(self, x, y, base, altura):
        super().__init__(x, y)
        self.base = base
        self.altura = altura

    @property
    def base(self):
        return self._base
    
    @base.setter
    def base(self, base):
        if base is int and base >= 0:
            self._base = base
        else:
            self._base = 0

    @property
    def altura(self):
        return self._altura
    
    @altura.setter
    def altura(self, altura):
        if altura is int and altura >= 0:
            self._altura = altura
        else:
            self._altura = 0

    def area(self):
        return (self.base*self.altura)/2

    def perimetro(self):
        return self.base + self.altura + sqrt(self.base**2 + self.altura**2)

    def model(self):
        print(f'A coordenada do Triângulo é: ({self._x}, {self._y}) '
              'e sua base: {self.base} e sua altura: {self.altura}')
