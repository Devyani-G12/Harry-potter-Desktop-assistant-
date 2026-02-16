import tkinter as tk
from PIL import Image, ImageTk

class DraggableIcon(tk.Tk):
    def __init__(self, image_path):
        super().__init__()

        self.overrideredirect(True)
        self.attributes("-topmost", True)
        self.configure(bg="#ff00ff")
        self.wm_attributes("-transparentcolor", "#ff00ff")
        self.attributes("-alpha", 0.95)

        self.ICON_SIZE = 96
        self.PANEL_WIDTH = 320
        self.PANEL_HEIGHT = 140

        img = Image.open(image_path).resize(
            (self.ICON_SIZE, self.ICON_SIZE),
            Image.Resampling.LANCZOS
        )
        self.tk_img = ImageTk.PhotoImage(img)

        self.geometry(f"{self.ICON_SIZE + self.PANEL_WIDTH}x{self.PANEL_HEIGHT}")

        self.canvas = tk.Canvas(self, bg="#ff00ff", highlightthickness=0)
        self.canvas.place(x=0, y=0, width=self.ICON_SIZE, height=self.ICON_SIZE)
        self.canvas.create_image(0, 0, anchor="nw", image=self.tk_img)

        self.panel = tk.Text(
            self,
            bg="#1e1e1e",
            fg="#e8fdf8",
            font=("Segoe UI", 16),
            wrap="word",
            bd=0
        )
        self.panel.place(
            x=self.ICON_SIZE + 10,
            y=10,
            width=self.PANEL_WIDTH - 20,
            height=self.PANEL_HEIGHT - 20
        )
        self.panel.config(state="disabled")

        self.bind("<ButtonPress-1>", self.start_move)
        self.bind("<B1-Motion>", self.do_move)

        self._x = self._y = 0

    def show_panel(self, text):
        self.panel.config(state="normal")
        self.panel.delete("1.0", "end")
        self.panel.insert("end", text)
        self.panel.config(state="disabled")

    def start_move(self, e):
        self._x, self._y = e.x, e.y

    def do_move(self, e):
        self.geometry(f"+{e.x_root - self._x}+{e.y_root - self._y}")
