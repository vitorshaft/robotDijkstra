import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import networkx as nx
import numpy as np
import json
import matplotlib.pyplot as plt

class MapNavigator:
    def __init__(self, root):
        self.root = root
        self.root.title("Map Navigator")
        self.canvas = tk.Canvas(root, cursor="cross")
        self.canvas.pack(fill="both", expand=True)
        self.canvas.bind("<Button-1>", self.set_point)
        self.points = []
        self.img = None
        self.graph = nx.Graph()

        self.load_image()

    def load_image(self):
        img_path = filedialog.askopenfilename(filetypes=[("JPEG files", "*.jpg")])
        self.img = Image.open(img_path).convert("L")
        self.img_array = np.array(self.img)
        self.tk_img = ImageTk.PhotoImage(self.img)
        self.canvas.create_image(0, 0, anchor="nw", image=self.tk_img)

    def set_point(self, event):
        if len(self.points) < 2:
            x, y = event.x, event.y
            self.points.append((x, y))
            self.canvas.create_oval(x-3, y-3, x+3, y+3, fill="red")

            if len(self.points) == 2:
                self.create_graph()
                self.find_path()

    def create_graph(self):
        # Adiciona nós e arestas ao grafo
        height, width = self.img_array.shape
        for y in range(height):
            for x in range(width):
                if self.img_array[y, x] == 0:  # Pixel preto
                    self.graph.add_node((x, y))
                    if x > 0 and self.img_array[y, x-1] == 0:
                        self.graph.add_edge((x, y), (x-1, y))
                    if y > 0 and self.img_array[y-1, x] == 0:
                        self.graph.add_edge((x, y), (x, y-1))

    def find_path(self):
        start, end = self.points
        path = nx.dijkstra_path(self.graph, start, end)
        self.save_output(path)
        self.display_path(path)

    def save_output(self, path):
        path_img = self.img.convert("RGB")
        pixels = path_img.load()
        for (x, y) in path:
            pixels[x, y] = (255, 0, 0)  # Red path

        path_img.save("path.jpg")

        with open("path.json", "w") as f:
            json.dump(path, f)

    def display_path(self, path):
        plt.imshow(self.img, cmap="gray")
        x_coords, y_coords = zip(*path)
        plt.plot(x_coords, y_coords, color="red")
        plt.scatter(*zip(*self.points), color="blue")
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = MapNavigator(root)
    root.mainloop()
