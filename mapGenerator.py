import tkinter as tk
from PIL import Image, ImageDraw

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

        save_button = tk.Button(root, text="Save Map", command=self.save_image)
        save_button.pack()

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

if __name__ == "__main__":
    root = tk.Tk()
    app = ObstacleDrawer(root)
    root.mainloop()
