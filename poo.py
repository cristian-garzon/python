from math import sqrt
class punto:
    def __init__(self, x=0,y=0):
        self.x=x
        self.y=y
    def __str__(self):
        return "({},{})".format(self.x,self.y)
    def cuadrante(self):
        if self.x<0 and self.y<0:
            print("tercer cuadrante")
        elif self.x>0 and self.y>0:
            print("primer cuadrante")
        elif self.x>0 and self.y<0:
            print("cuarto cuadrante")
        elif self.x<0 and self.y>0:
            print("segundo cuadrante")
        elif self.x==0 and self.y!=0:
            print("sobre el eje x")
        elif self.x!=0 and self.y==0:
            print("sobre el eje y")
        else:
            print("en el punto origen")
    def vector(self, p):
        print("El vector entre {} y {} es ({}, {})".format(
            self, p, p.x - self.x, p.y - self.y) )  
    def distancia(self, p):
        print("la distancia entre {} y {} es {}".format(self,p,sqrt((p.x-self.x)**2+(p.y-self.y)**2)))
class rectangulo:
    def __init__(self, inicio=punto(),fin=punto()):
        self.fin=fin
        self.inicio=inicio
        self.b=self.fin.x-self.inicio.x
        self.h=self.fin.y-self.inicio.y
        self.a=self.b*self.h
    def base(self):
        print("la base es de {}".format(self.b))
    def altura(self):
        print("la altura es de {}".format(self.h))
    def area(self):
        print("la base es de {}".format(self.a))
a=punto(2,3)
b=punto(5,5)
c=punto(-3,-1)
d=punto()
print(a,b,c,d)
a.cuadrante()
c.cuadrante()
d.cuadrante()
a.vector(b)
b.vector(a)
a.distancia(b)
b.distancia(a)
a.distancia(d)
b.distancia(d)
c.distancia(d)
e=rectangulo(a,b)
e.base()
e.altura()
e.area()

        