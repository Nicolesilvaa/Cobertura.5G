import cNo
import random
import math
import QuickSort
import cAntenas

class KDTree:
    def __init__(self):

        self.raiz = None

    def inserir(self, raiz, ponto, profundidade=0):
        if raiz is None:
            return cNo.cNo(ponto)

        eixo = profundidade % 2
        if eixo == 0:
            comparar = ponto.x < raiz.getDado().x
        else:
            comparar = ponto.y < raiz.getDado().y

        if comparar:
            raiz.setFilhoEsq(self.inserir(raiz.getFilhoEsd(), ponto, profundidade + 1))
        else:
            raiz.setFilhoDir(self.inserir(raiz.getFilhoDir(), ponto, profundidade + 1))

        return raiz

    def ordenar_pontos(self, pontos, eixo):

        QuickSort.ordenaQuick(pontos, 0, len(pontos) - 1, eixo)
        
        return pontos


    def construir(self, pontos, profundidade=0):
        if not pontos:
            return None

        eixo = profundidade % 2
        pontos_ordenados = self.ordenar_pontos(pontos, eixo)
        mediana = len(pontos_ordenados) //2  

        no = cNo.cNo(pontos_ordenados[mediana])
        no.setFilhoEsq(self.construir(pontos_ordenados[:mediana], profundidade + 1))
        no.setFilhoDir(self.construir(pontos_ordenados[mediana + 1:], profundidade + 1))

        return no

    def KNN(self, x, y, k=1):
        busca = cAntenas.Antenas(x, y)
        maisProximos = []
        self.KNNrecursivo(self.raiz, busca, maisProximos, k, 0)
        return maisProximos[0][1] if maisProximos else None  

    def KNNrecursivo(self, no, busca, maisProximos, k, profundidade):
        if no is None:
            return

        noCor = no.getDado()
        distancia = math.sqrt((busca.x - noCor.x)**2 + (busca.y - noCor.y)**2)
        maisProximos.append((distancia, noCor))
        QuickSort.ordenaQuick(maisProximos, 0, len(maisProximos) - 1)

        if len(maisProximos) > k:
            maisProximos.pop()

        if busca.x < noCor.x:
            self.KNNrecursivo(no.getFilhoEsq(), busca, maisProximos, k, profundidade + 1)
            if len(maisProximos) < k or abs(busca.x - noCor.x) < maisProximos[-1][0]:
                self.KNNrecursivo(no.getFilhoDir(), busca, maisProximos, k, profundidade + 1)
        else:
            self.KNNrecursivo(no.getFilhoDir(), busca, maisProximos, k, profundidade + 1)
            if len(maisProximos) < k or abs(busca.y - noCor.y) < maisProximos[-1][0]:
                self.KNNrecursivo(no.getFilhoEsq(), busca, maisProximos, k, profundidade + 1)

    def inicializar(self, pontos):
        self.raiz = self.construir(pontos)

    def imprimir_arvore(self, no, nivel=0):
        
        if no is not None:
            print(" " * nivel  + f" Ponto: {no.getDado()}, Eixo: {'X' if nivel % 2 == 0 else 'Y'}")
            
            self.imprimir_arvore(no.getFilhoEsq(), nivel + 1)
            self.imprimir_arvore(no.getFilhoDir(), nivel + 1)
            

if __name__ == "__main__":

    pontos = []
    for i in range(20):
        antena = cAntenas.Antenas(round(random.uniform(1, 20), 2), round(random.uniform(1, 20), 2))
        pontos.append(antena)
    
    arvore = KDTree()
    arvore.inicializar(pontos)
    print("Estrutura da KD-Tree:")
    arvore.imprimir_arvore(arvore.raiz)
    
    ponto_consulta = cAntenas.Antenas(5, 10)
    mais_proximo = arvore.KNN(ponto_consulta.x, ponto_consulta.y, k=1)
    print(f"\nO ponto mais próximo de {ponto_consulta} é {mais_proximo}")
