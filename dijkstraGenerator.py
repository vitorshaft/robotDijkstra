import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw
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
        self.path = None

        self.load_image()

        self.save_button = tk.Button(root, text="Save Path", command=self.save_path)
        self.save_button.pack(side="left")

        self.clear_button = tk.Button(root, text="Clear Path", command=self.clear_path)
        self.clear_button.pack(side="right")

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
            color = "yellow" if len(self.points) == 1 else "green"
            self.canvas.create_oval(x-3, y-3, x+3, y+3, fill=color)

            if len(self.points) == 2:
                self.create_graph()
                self.find_path()

    def create_graph(self):
        height, width = self.img_array.shape
        for y in range(height):
            for x in range(width):
                if self.img_array[y, x] == 0:  # Pixel preto
                    self.graph.add_node((x, y))
                    if x > 0 and self.img_array[y, x-1] == 0:
                        self.graph.add_edge((x, y), (x-1, y))
                    if y > 0 and self.img_array[y-1, x] == 0:
                        self.graph.add_edge((x, y), (x, y-1))
        self.save_graph_image()

    def find_path(self):
        start, end = self.points
        self.path = nx.dijkstra_path(self.graph, start, end)
        self.display_path()

    def display_path(self):
        if self.path:
            self.canvas.delete("path")
            for (x, y) in self.path:
                self.canvas.create_oval(x-1, y-1, x+1, y+1, fill="red", tags="path")

    def save_path(self):
        if self.path:
            path_img = self.img.convert("RGB")
            draw = ImageDraw.Draw(path_img)

            # Draw the path in red
            for (x, y) in self.path:
                draw.point((x, y), fill="red")

            # Draw the start and end points
            start, end = self.points
            draw.ellipse((start[0]-3, start[1]-3, start[0]+3, start[1]+3), fill="yellow")
            draw.ellipse((end[0]-3, end[1]-3, end[0]+3, end[1]+3), fill="green")

            path_img.save("path.jpg")

            with open("path.json", "w") as f:
                json.dump(self.path, f)

            # Show pop-up message
            messagebox.showinfo("Save Path", "Path saved as 'path.jpg' and 'path.json'")

    def clear_path(self):
        self.canvas.delete("path")
        self.points = []
        self.path = None

    def save_graph_image(self):
        graph_img = self.img.convert("RGB")
        draw = ImageDraw.Draw(graph_img)
        for (x, y) in self.graph.nodes:
            draw.point((x, y), fill="blue")
        for (x1, y1), (x2, y2) in self.graph.edges:
            draw.line((x1, y1, x2, y2), fill="white")
        graph_img.save("graph.jpg")
        print("Graph saved as 'graph.jpg'")

if __name__ == "__main__":
    root = tk.Tk()
    app = MapNavigator(root)
    root.mainloop()
