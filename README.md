# Cobertura 5G
> Este projeto tem como objetivo principal desenvolver um simulador capaz de representar a cobertura da distribuição de antenas de médio e pequeno alcance em uma determinada área geográfica.

## Funcionalidades:
- Mapear a localização das antenas: Coletar e organizar dados sobre a localização e o raio de alcance das antenas.
- Analisar a cobertura: Desenvolver um algoritmo que, a partir da localização do usuário, identifique a antena mais próxima.
- Visualizar os resultados: Criar uma interface intuitiva que permita visualizar a cobertura da rede.
  
# Apresentando a solução do problema: 👾

> Nesta solução optamos por utilizar a Árvore KD-Tree como estrutura principal para armazenar as coordenadas das antenas e o algorimo KNN para procurar o ponto que está no alcance do raio das antenas. Caso o usuário não defina o número de antenas e o raio de alcance, as antenas são geradas de forma  randômica e alcance tem valor fixo. 

## Justificativa da escolha da EDA e do algoritmo de busca: ✅

- **K-D TREE:** 
    > Uma vez que as antenas possuem coordenadas x e y, a K-D Tree foi a melhor opção encontrada por organizar os dados em um espaço K-dimensional. Além disso, essa estrutura é eficaz em operações de busca.

    > A K-D Tree divide o espaço k-dimensional em regiões menores por meio da divisão recursiva. Cada nó é um ponto da árvore e cada nível da árvore representa uma dimensão. No primeiro nível, a árvore pode dividir os pontos com base na primeira dimensão, no segundo nível na segunda dimensão, e assim por diante.

   **Complexidade na construção:**
  
  - **Melhor caso e caso médio:** (n log n), onde n é o número de pontos. Isso ocorre porque a construção da árvore envolve dividir recursivamente o conjunto de dados em partes iguais, o que pode ser feito em tempo logarítmico usando algoritmos como quicksort(ordenação rápida).

   - **Pior caso:**  O(n²), quando os dados estão ordenados de forma que as divisões sempre ocorram em um único ponto.

 - **KNN:**

    > Esse algoritmo de busca procura o "vizinho mais próximo" da base de dados. Dado o ponto de consulta, a partir da raiz, o algoritmo decide qual subárvor (esquerda ou direita) explorar com base no valor do ponto de consulta no eixo de divisão do nó atual. A distância entre os pontos(usamos a distância euclidiana) é calculada e, se o ponto for um dos vizinhos mais próximos, ele é adicionado na lista dos k vizinhos mais próximos. 

    > Vale ressaltar que, a medida que o número de dimensões aumenta, o KNN se torna menos eficiente.

    **Complexidade:**

    - **Melhor  caso  e caso médio:** O(log n), quando a árvore está perfeitamente balanceada e a busca pode ser feita em um número mínimo de comparações.

    - **Pior caso:** O(n), quando a árvore está desbalanceada ou os dados estão agrupados de forma não uniforme, forçando a busca a percorrer grande parte da árvore.

    **Implementação:**
    >1. Segue o caminho da árvore até o ponto mais próximo (comparando x ou y alternadamente).
    >2. Guarda os k pontos mais próximos encontrados até o momento.
    >3. Verifica se precisa explorar o outro lado da árvore:
    >3.1. Caso precise, ele percorre a sub-arvore. Caso contrário, ele ignora, economizando verificações.

- **QuickSort:**

    > O algoritmo segue o princípio da divisão e conquista:

    > Escolhe um pivô (geralmente o último elemento da lista).
    Reorganiza os elementos ao redor do pivô, colocando os menores à esquerda e os maiores à direita.
    Aplica o processo recursivamente nas duas partes resultantes até que a lista esteja ordenada.

    > No contexto da KD-Tree, o QuickSort é modificado para ordenar os pontos com base em um eixo específico:
    Se o eixo for X, os pontos são ordenados pelo valor de x.
    Se o eixo for Y, os pontos são ordenados pelo valor de y.
    Isso permite que a construção da árvore utilize sempre o ponto mediano de forma eficiente, garantindo que a busca por vizinhos mais próximos (KNN) seja otimizada.

    **Complexidade**

    - **Melhor caso e caso médio:** O(n log n), devido à divisão balanceada dos elementos.

    - **Pior caso:** O(n²), se a escolha do pivô for ruim (como em uma lista já ordenada).

### Como a solução foi modularizada? 🚀

- **cAntenas:**
    > Objetivo: Gerar pontos com coordenadas X e Y aleatórias, restrigindo-as aos limites máximo e mínimo;

- **cKdTree:**
    > Objetivo: Organizar pontos no plano cartesiano e permitir consultas eficientes para encontrar os k pontos mais próximos de uma coordenada de interesse. Segue abaixo seus principais módulos:

    - ***Construir***
        >  A árvore é construída recursivamente, particionando os pontos ao longo dos eixos alternados (X e Y) em cada nível. O ponto mediano de cada conjunto é escolhido como nó raiz, e os subconjuntos à esquerda e à direita são distribuídos como filhos. A ordenação dos pontos antes da divisão é realizada utilizando o algoritmo QuickSort, garantindo eficiência na separação dos nós.

    - ***Inserir:***
        > A inserção segue a lógica da construção da árvore, navegando pelos nós de acordo com o eixo correspondente ao nível de profundidade e posicionando o novo ponto na subárvore correta.

    - ***KNN:***
        > A busca pelo vizinho mais próximo utiliza um algoritmo recursivo otimizado, que explora a estrutura da árvore para descartar regiões irrelevantes do espaço, reduzindo o número de comparações. Durante a busca:

        1. O algoritmo segue o ramo mais provável onde o ponto estaria.
        2. Mantém uma lista ordenada dos k vizinhos mais próximos encontrados até o momento.
        3. Verifica se é necessário explorar o outro lado da árvore com base na distância do hiperplano de divisão.

- **cNo:**
    > Objetivo: Ser o ponto de conexão entre a árvore e suas sub-árvores.

- **QuickSort:**

    > Objetivo: Ordenar rapidamente os pontos da KD-Tree com base em um eixo específico (X ou Y). 

- **Main:**
 > Objetivo: Demonstar graficamente se determinado ponto está dentro do alcance de uma antena. Nele inserimos pontos aleatórios na árvore, capturamos um click que gera um novo ponto na janela de vizualização, recebemos a posição do clique e verificamos se está posição está dentro do raio de uma antena. Caso o ponto esteja dentro do raio, ele fica verde, caso não esteja ele fica vermelho e realça a antena mais próxima. Além disso, ao pressionar a tecla "espaço", os quadrantes da árvore são desenhados na janela e ao clicar na tecla "enter" eles somem. 

 > Biblioteca: **pyglet**.

## Metodologia ágil adotada: 🧙
 >  Inicialmente, cada desenvolvedor ficou responsável por duas funcionalidades do código. Realizamos reuniões semanais para alinhar o projeto e os alinhamentos pequenos foram feitos de acordo com a demanda no WhatsApp.

### Atribuição dos Devs:
 > Segue abaixo a contribuição de cada DEV: 

#### Nicole Siva:
- cAntenas
- KNN

#### Yuri Santos:
 - cKdTree
 - cNo

 ### Ambos:
 - Quicksort
 - main

## Devs: 🧑🏿‍💻👩🏿‍💻

- [Nicole Silva](https://github.com/Nicolesilvaa)
- [Yuri Chagas](https://github.com/Snorlaxch)

## Demonstração: 


# Referências 📚

[1]	Heineman, George T., Gary Pollice, and Stanley Selkow. **Algorithms in a nutshell: A practical guide**. O'Reilly Media, Inc.", 2016.

[2]	Samet, Hanan. **Foundations of multidimensional and metric data structures**. Morgan Kaufmann, 2006.
