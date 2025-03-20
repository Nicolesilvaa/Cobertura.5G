import random

class Antenas:
    
    def __init__(self, x = 0.0,y = 0.0):
         
        self.x = x
        self.y = y
        
    def prit(self):
        print(f'Ponto =  ( {self.x} , {self.y} )')
        
    def getCoordenadas(self):
        return (self.x, self.y) 

    def gerarAntenas(self, minX, minY, maxX, maxY):
        
        self.x = round(random.uniform(minX, maxX), 2)
        self.y = round(random.uniform(minY, maxY), 2)

    def __str__(self):
        return f"({self.x}, {self.y})"


    def __repr__(self):
        return self.__str__()
    
if __name__ == "__main__":
    
    # Teste simples: gerar 5 antenas e imprimir suas coordenadas
    nAntenas = int(input("Digite o número de antenas da sua região: "))
    minX, minY = -9, 20
    maxX, maxY = 15, 10

    antenas = []  
    
    for i in range(nAntenas):

        antena = Antenas()
        antena.gerarAntenas(minX, minY, maxX, maxY)
        antenas.append(antena)
    
    for antena in antenas:
        print(antena) 

