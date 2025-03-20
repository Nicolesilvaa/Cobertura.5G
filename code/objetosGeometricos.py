# #########################################
# Define um Tipo Abstrato de Dados (TAD) 
# para armazenar cores no formato RGB
# #########################################

class cCor:

    def __init__(self, r=255, g=255, b=255):
        self.r = r
        self.g = g
        self.b = b

    def setCor(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def setR(self, r):
        self.r = r

    def setG(self, g):
        self.g = g

    def setB(self, b):
        self.b = b

    def getCor(self):
        return self.r, self.g, self.b

    def getR(self):
        return self.r

    def getG(self):
        return self.g

    def getB(self):
        return self.b

    def __str__(self):
        return f'[ {self.r} , {self.g} , {self.b} ]'

# #########################################
# Define um Tipo Abstrato de Dados (TAD) 
# para armazenar pontos em 2D com cor
# #########################################

class cPonto:

    def __init__(self, x=0.0, y=0.0, c=cCor(0, 0, 0)):
        self.x      = x
        self.y      = y
        self.cor    = c

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getCorPto(self):
        return self.cor

    def __str__(self):
        return f'( {self.x} , {self.y } ) {self.cor}'

# #########################################
# Define um Tipo Abstrato de Dados (TAD) 
# para armazenar um retangulo 2D
# #########################################

class cRect:

    def __init__(self, pto=cPonto(), width=2.0, height=2.0):
        self.ptoBase    = pto
        self.width      = 1.0 if width == 0 else abs(width)
        self.heigth     = 1.0 if height == 0 else abs(height)

    def __str__(self):
        return f'Rect =  ( {self.ptoBase.getX()} , {self.ptoBase.getY()} ) - ( {self.width}, {self.heigth})'

    def getPtoBase(self):
        return self.ptoBase
        
    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.heigth

  
# *******************************************************
# ***                                                 ***
# *******************************************************
if __name__ == '__main__':

    r1 = cRect(cPonto(10, 10), 20, 20)

    p0 = cPonto(-10, -10, cCor(255, 0, 0))

    r2 = cRect(p0, 5, 0)

    print(r1)
    print(r2)
    print(p0)