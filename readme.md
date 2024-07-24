# Projeto de Navegação de Robô

Este projeto consiste em dois scripts Python para criar e analisar mapas de navegação para robôs. O primeiro script permite desenhar mapas e gerar imagens que podem ser usadas para simular rotas de robôs. O segundo script lê um mapa binário, permite ao usuário selecionar pontos de origem e destino, e utiliza o algoritmo de Dijkstra para calcular e visualizar a rota mais curta entre esses pontos.

## Scripts

### 1. Desenhando o Mapa

**Descrição:** Este script permite ao usuário desenhar um mapa interativo com fundo preto e obstáculos na cor branca. O usuário pode desenhar formas geométricas (retângulos, elipses e linhas) com poucos cliques e gerar uma imagem do mapa (`mapa.jpg`).

**Requisitos:**
- Python 3.9
- Bibliotecas: `pygame`, `numpy`, `PIL`

**Como Usar:**
1. Execute o script `mapGenerator.py`.
2. Use as ferramentas na interface para desenhar obstáculos e formas geométricas no mapa.
3. Salve o mapa gerado como `mapa.jpg` clicando no botão "Salvar Mapa".

**Arquivo:** `mapGenerator.py`

### 2. Calculando a Rota do Robô

**Descrição:** Este script lê um mapa binário em formato `.jpg`, onde áreas brancas representam obstáculos e áreas pretas representam o ambiente navegável. O usuário pode selecionar pontos de origem e destino na interface gráfica. O script cria um grafo com base nas bordas dos obstáculos e usa o algoritmo de Dijkstra para encontrar e exibir a rota mais curta entre os pontos selecionados.

**Requisitos:**
- Python 3.9
- Bibliotecas: `opencv-python`, `matplotlib`, `networkx`, `numpy`, `PIL`

**Como Usar:**
1. Execute o script `dijkstraGenerator.py`.
2. Selecione o ponto de origem e o ponto de destino clicando no mapa exibido.
3. O script calculará a rota e a exibirá no mapa.
4. A rota será salva em uma nova imagem e em um arquivo JSON.

**Arquivo:** `dijkstraGenerator.py`

## Instalação

Para instalar as dependências, execute:

```bash
pip install pygame numpy pillow opencv-python matplotlib networkx
