def ordenaQuick(vet, inicio, final, eixo=None):
    if inicio < final:

        p = pivoteamento(vet, inicio, final, eixo)  
        ordenaQuick(vet, inicio, p - 1, eixo)  # Recursão esquerda
        ordenaQuick(vet, p + 1, final, eixo)  # Recursão direita
    
    
    
    return vet

def pivoteamento(vet, inicio, final, eixo= None):

    pivo = vet[final]  
    i = inicio - 1 

    if eixo is None:
    
        for j in range(inicio, final):
            if vet[j] < pivo:  
                i += 1
                vet[i], vet[j] = vet[j], vet[i]  

        vet[i + 1], vet[final] = vet[final], vet[i + 1]  # pivô na posição correta
        return i + 1 
    

    for j in range(inicio, final):
            if (vet[j].x if eixo == 0 else vet[j].y) < (pivo.x if eixo == 0 else pivo.y):  # Compara com o eixo correto
                i += 1
                vet[i], vet[j] = vet[j], vet[i] 

    vet[i + 1], vet[final] = vet[final], vet[i + 1]  # pivô na posição correta
    return i + 1