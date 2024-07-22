from math import pi, sqrt


class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
        self._name = __class__.__name__
       
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
        print(f'A coordenada do {self._name} é: ({self.x}, {self.y})')


class Segmento():
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self._name = __class__.__name__

    @property
    def x1(self):
        return self._x1
    
    @x1.setter
    def x1(self, x1):
        if isinstance(x1, int) and x1 >= 0:
            self._x1 = x1
        else:
            self._x1 = 0

    @property
    def y1(self):
        return self._y1
    
    @y1.setter
    def y1(self, y1):
        if isinstance(y1, int) and y1 >= 0:
            self._y1 = y1
        else:
            self._y1 = 0

    @property
    def x2(self):
        return self._x2
    
    @x2.setter
    def x2(self, x2):
        if isinstance(x2, int) and x2 >= 0:
            self._x2 = x2
        else:
            self._x2 = 0

    @property
    def y2(self):
        return self._y2
    
    @y2.setter
    def y2(self, y2):
        if isinstance(y2, int) and y2 >= 0:
            self._y2 = y2
        else:
            self._y2 = 0

    def comprimento(self):
        return sqrt((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2) 

    def model(self):
        print(f'As coordenadas dos pontos do {self._name} são: '
              f'({self.x1}, {self.y1}) e ({self.x2}, {self.y2})'
              f' e seu comprimento é: {self.comprimento():.2f}')


class Reta: 
    def __init__(self, a, b) -> None:
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
        y = self._a * x + self._b
        return y
    
    def model(self):
        print(f"Os parâmetros do modelo de reta são: \
a={self.a} e b={self._b}")
        

class Circulo(Ponto):
    def __init__(self, raio, x, y):
        super().__init__(x, y)
        self.raio = raio
        self._name = __class__.__name__
        
    @property
    def raio(self):
        return self._raio
    
    @raio.setter
    def raio(self, raio):
        if isinstance(raio, int) and raio >= 0:
            self._raio = raio
        else:
            self._raio = 0

    def model(self):
        print(f'A coordenada do {self._name} é: ({self._x}, {self._y}) \
e seu raio é: {self._raio}')

    def diametro(self):
        return self._raio*2
    
    def area(self):
        return pi*(self._raio**2)
    
    def circunferencia(self):
        return 2*pi*self._raio
    

class Quadrado(Ponto):
    def __init__(self, lado, x, y):
        super().__init__(x, y)
        self.lado = lado
        self._name = __class__.__name__
        
    @property
    def lado(self):
        return self._lado
    
    @lado.setter
    def lado(self, lado):
        if isinstance(lado, int) and lado >= 0:
            self._lado = lado
        else:
            self._lado = 0

    def model(self):
        print(f'A coordenada do {self._name} é: ({self._x}, {self._y}) \
e seu lado é: {self.lado}')
   
    def area(self):
        return self.lado**2

    def perimetro(self):
        return 4*self.lado

    def diagonal(self):
        return self.lado*sqrt(2)


class Triangulo(Ponto):
    def __init__(self, x, y, base, altura):
        super().__init__(x, y)
        self.base = base
        self.altura = altura
        self._name = __class__.__name__

    @property
    def base(self):
        return self._base
    
    @base.setter
    def base(self, base):
        if isinstance(base, int) and base >= 0:
            self._base = base
        else:
            self._base = 0

    @property
    def altura(self):
        return self._altura
   
    @altura.setter
    def altura(self, altura):
        if isinstance(altura, int) and altura >= 0:
            self._altura = altura
        else:
            self._altura = 0

    def area(self):
        return (self.base*self.altura)/2

    def perimetro(self):
        return self.base + self.altura + sqrt(self.base**2 + self.altura**2)

    def model(self):
        print(f'A coordenada do Triângulo é: ({self._x}, {self._y}) '
              f'sua base: {self.base} e sua altura: {self.altura}')
