import sys
import math
import random
from datetime import datetime

import objetosGeometricos as cObjetos  # importa o modulo com os objetos geometricos

import pyglet
from pyglet import shapes
from pyglet.window import Window
from pyglet.window import key
from pyglet.window import mouse

import cAntenas, cNo, KdTree

# dimensões da janela
WIN_X = 800
WIN_Y = 800
pto_atual = None
Draw_global= None
# *******************************************************
# ***                                                 ***
# *******************************************************

# Criar a Janela

def draw_quadrants(node, x_min, y_min, x_max, y_max, profundidade, batch, formas):

    if node is None:
        return
    
    ponto = node.getDado()
    x = ponto.x
    y = ponto.y
    
    if profundidade % 2 == 0:
        # Divisão vertical (batch X)
        linha = shapes.Line(x, y_min, x, y_max, thickness=1, color=(255, 255, 255), batch=batch)
        formas.append(linha)
        
        draw_quadrants(node.getFilhoEsq(), x_min, y_min, x, y_max, profundidade + 1, batch, formas)
        draw_quadrants(node.getFilhoDir(), x, y_min, x_max, y_max, profundidade + 1, batch, formas)
    else:
        # Divisão horizontal (batch Y)
        linha = shapes.Line(x_min, y, x_max, y,  thickness=1, color=(255, 255, 255), batch=batch)
        formas.append(linha)
        
        draw_quadrants(node.getFilhoEsq(), x_min, y_min, x_max, y, profundidade + 1, batch, formas)
        draw_quadrants(node.getFilhoDir(), x_min, y, x_max, y_max, profundidade + 1, batch, formas)

def gameLoop(nAntenas, alcance):

    global window, batch

    window = pyglet.window.Window(WIN_X, WIN_Y)
    window.set_caption('Cobertura 5G')

    batch = pyglet.graphics.Batch()
    formas = []
    arvore = KdTree.KDTree()
    antenas = []

    for i in range(nAntenas):
        x = random.uniform(50, WIN_X - 50)
        y = random.uniform(50, WIN_Y - 50)
        antena = cAntenas.Antenas(x, y)
        antenas.append(antena)

    arvore.inicializar(antenas)
    
    # Visualizar as antenas como círculos
    for antena in antenas:
        formas.append(shapes.Circle(antena.x, antena.y, 5, color=(244, 164, 96), batch=batch))

    # Desenho da área de alcance
    def draw_area_alcance(x, y):
        radius = alcance  # Raio da área de alcance (pode ser ajustado)
        formas.append(shapes.Circle(x, y, radius, color=(244, 164, 96), batch=batch))

    def distancia(p1, p2):
        return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


    # Função para colorir o ponto com base na proximidade das antenas
    def colorir(x, y, alcance):
        ponto = cAntenas.Antenas(x, y)

        for antena in antenas:  # Corrigido de pontos para antenas
            dist = distancia(ponto, antena)
            if dist <= alcance:
                formas.append(shapes.Circle(x, y, 5, color=(0, 100, 0), batch=batch))
                return

        formas.append(shapes.Circle(x, y, 5, color=(178, 34, 34), batch=batch))

    @window.event
    def on_draw():
        window.clear()
        batch.draw()

    @window.event
    def on_mouse_press(x, y, button, modifiers):
        if button == mouse.LEFT:
            busca = cAntenas.Antenas(x, y)
            maisProximo = arvore.KNN(busca.x, busca.y, k=1)

            if maisProximo:
                draw_area_alcance(maisProximo.x, maisProximo.y)
                colorir(x, y, alcance)
                

    @window.event
    def on_key_press(symbol, modifiers):
        
        if symbol == key.SPACE:
            draw_quadrants(arvore.raiz, 0, 0, WIN_X, WIN_Y, 0, batch, formas)

        elif symbol == key.ENTER:
            formas.clear()
            
            for antena in antenas:
                formas.append(shapes.Circle(antena.x, antena.y, 5, color=(244, 164, 96), batch=batch))
    
    pyglet.app.run()

def trataLinhaDeComadoAntenas():
    n = 10
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
        if n < 0:
            n = 10
    else:
        n = random.randint(1, 50)
    return n

def trataLinhaDeComadoAlcance():
    n = 10
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
        if n < 0:
            n = 10
    else:
        n = 20
    return n
# *******************************************************
# ***                                                 ***
# *******************************************************


if __name__ == '__main__':
    random.seed(int(datetime.now().strftime('%H%M%S')))

    nAntenas = trataLinhaDeComadoAntenas()
    alcance =  trataLinhaDeComadoAlcance()

    print(nAntenas)
    print(f"Número de antenas: {nAntenas}")
    
    gameLoop(nAntenas,alcance)
  