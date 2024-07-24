import tkinter as tk
from PIL import Image, ImageDraw, ImageTk
import cv2
import numpy as np

class ObstacleDrawer:
    def __init__(self, root):
        self.root = root
        self.root.title("Obstacle Drawer")
        self.canvas = tk.Canvas(root, bg='black', cursor="cross", width=500, height=500)
        self.canvas.pack(fill="both", expand=True)

        self.shape = tk.StringVar(value="freeform")
        self.start_x, self.start_y = None, None

        shape_frame = tk.Frame(root)
        shape_frame.pack()

        shapes = [("Freeform", "freeform"), ("Rectangle", "rectangle"), ("Circle", "circle")]
        for text, mode in shapes:
            b = tk.Radiobutton(shape_frame, text=text, variable=self.shape, value=mode)
            b.pack(side="left")

        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

        self.image = Image.new("L", (500, 500), "black")
        self.draw = ImageDraw.Draw(self.image)

        # Campo para inserir o raio de inflação
        inflation_frame = tk.Frame(root)
        inflation_frame.pack()
        tk.Label(inflation_frame, text="Raio de Inflação (pixels):").pack(side="left")
        self.inflation_radius = tk.Entry(inflation_frame)
        self.inflation_radius.pack(side="left")

        save_button = tk.Button(root, text="Save Map", command=self.save_image)
        save_button.pack()

        inflate_button = tk.Button(root, text="Inflate Obstacles", command=self.inflate_obstacles)
        inflate_button.pack()

    def start_draw(self, event):
        self.start_x, self.start_y = event.x, event.y

    def paint(self, event):
        shape_mode = self.shape.get()
        if shape_mode == "freeform":
            if self.start_x and self.start_y:
                self.canvas.create_line(self.start_x, self.start_y, event.x, event.y, width=5, fill='white')
                self.draw.line([(self.start_x, self.start_y), (event.x, event.y)], fill='white', width=5)
            self.start_x, self.start_y = event.x, event.y
        else:
            self.canvas.delete("preview")
            if shape_mode == "rectangle":
                self.canvas.create_rectangle(self.start_x, self.start_y, event.x, event.y, fill='white', outline='white', tags="preview")
            elif shape_mode == "circle":
                x1, y1 = self.start_x, self.start_y
                x2, y2 = event.x, event.y
                radius = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
                self.canvas.create_oval(x1-radius, y1-radius, x1+radius, y1+radius, fill='white', outline='white', tags="preview")

    def reset(self, event):
        shape_mode = self.shape.get()
        if shape_mode == "rectangle":
            self.draw.rectangle([(self.start_x, self.start_y), (event.x, event.y)], fill='white', outline='white')
            self.canvas.delete("preview")
            self.canvas.create_rectangle(self.start_x, self.start_y, event.x, event.y, fill='white', outline='white')
        elif shape_mode == "circle":
            x1, y1 = self.start_x, self.start_y
            x2, y2 = event.x, event.y
            radius = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
            self.draw.ellipse([x1-radius, y1-radius, x1+radius, y1+radius], fill='white', outline='white')
            self.canvas.delete("preview")
            self.canvas.create_oval(x1-radius, y1-radius, x1+radius, y1+radius, fill='white', outline='white')
        self.start_x, self.start_y = None, None

    def save_image(self):
        self.image.save("mapa.jpg")
        print("Mapa salvo como 'mapa.jpg'")

    def inflate_obstacles(self):
        radius = int(self.inflation_radius.get())
        map_image = np.array(self.image)

        kernel = np.ones((2 * radius + 1, 2 * radius + 1), np.uint8)
        inflated_map = cv2.dilate(map_image, kernel, iterations=1)

        inflated_image = Image.fromarray(inflated_map)

        # Exibir imagem inflada em uma nova janela
        self.show_inflated_image(inflated_image)

        inflated_image.save("mapa_inflado.jpg")
        print("Mapa inflado salvo como 'mapa_inflado.jpg'")

    def show_inflated_image(self, img):
        new_window = tk.Toplevel(self.root)
        new_window.title("Mapa Inflado")

        img = img.convert("RGB")  # Converter para RGB
        img_tk = ImageTk.PhotoImage(img)
        
        label = tk.Label(new_window, image=img_tk)
        label.image = img_tk  # Manter referência para evitar garbage collection
        label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = ObstacleDrawer(root)
    root.mainloop()
