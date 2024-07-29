# Projeto de Navegação de Robô / Robot Navigation Project

Este projeto consiste em dois scripts Python para criar e analisar mapas de navegação para robôs. O primeiro script permite desenhar mapas e gerar imagens que podem ser usadas para simular rotas de robôs. O segundo script lê um mapa binário, permite ao usuário selecionar pontos de origem e destino, e utiliza o algoritmo de Dijkstra para calcular e visualizar a rota mais curta entre esses pontos.

This project consists of two Python scripts for creating and analyzing navigation maps for robots. The first script allows you to draw maps and generate images that can be used to simulate robot routes. The second script reads a binary map, allows the user to select origin and destination points, and uses Dijkstra's algorithm to calculate and visualize the shortest route between these points.

## Scripts

### 1. Desenhando o Mapa / Drawing the Map

**Descrição:** Este script permite ao usuário desenhar um mapa interativo com fundo preto e obstáculos na cor branca. O usuário pode desenhar formas geométricas (retângulos, elipses e linhas) com poucos cliques e gerar uma imagem do mapa (`mapa.jpg`).

**Description:** This script allows the user to draw an interactive map with a black background and white obstacles. The user can draw geometric shapes (rectangles, ellipses, and lines) with a few clicks and generate an image of the map (`mapa.jpg`).

**Requisitos / Requirements:**
- Python 3.9
- Bibliotecas / Libraries: `pygame`, `numpy`, `PIL`

**Como Usar / How to Use:**
1. Execute o script `mapGenerator.py`.
2. Use as ferramentas na interface para desenhar obstáculos e formas geométricas no mapa.
3. Salve o mapa gerado como `mapa.jpg` clicando no botão "Salvar Mapa".

1. Run the `mapGenerator.py` script.
2. Use the tools in the interface to draw obstacles and geometric shapes on the map.
3. Save the generated map as `mapa.jpg` by clicking the "Save Map" button.

**Arquivo / File:** `mapGenerator.py`

### 2. Calculando a Rota do Robô / Calculating the Robot's Route

**Descrição:** Este script lê um mapa binário em formato `.jpg`, onde áreas brancas representam obstáculos e áreas pretas representam o ambiente navegável. O usuário pode selecionar pontos de origem e destino na interface gráfica. O script cria um grafo com base nas bordas dos obstáculos e usa o algoritmo de Dijkstra para encontrar e exibir a rota mais curta entre os pontos selecionados.

**Description:** This script reads a binary map in `.jpg` format, where white areas represent obstacles and black areas represent the navigable environment. The user can select origin and destination points in the graphical interface. The script creates a graph based on the edges of the obstacles and uses Dijkstra's algorithm to find and display the shortest route between the selected points.

**Requisitos / Requirements:**
- Python 3.9
- Bibliotecas / Libraries: `opencv-python`, `matplotlib`, `networkx`, `numpy`, `PIL`

**Como Usar / How to Use:**
1. Execute o script `dijkstraGenerator.py`.
2. Selecione o ponto de origem e o ponto de destino clicando no mapa exibido.
3. O script calculará a rota e a exibirá no mapa.
4. A rota será salva em uma nova imagem e em um arquivo JSON.

1. Run the `dijkstraGenerator.py` script.
2. Select the origin point and the destination point by clicking on the displayed map.
3. The script will calculate the route and display it on the map.
4. The route will be saved in a new image and in a JSON file.

**Arquivo / File:** `dijkstraGenerator.py`

## Instalação / Installation

Para instalar as dependências, execute:
To install the dependencies, run:

```bash
pip install pygame numpy pillow opencv-python matplotlib networkx
