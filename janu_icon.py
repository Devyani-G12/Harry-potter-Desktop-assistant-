"""GUI Icon and Panel Module

Manages the draggable GUI icon and response panel for the assistant.
"""

import tkinter as tk
import logging
from pathlib import Path
from typing import Optional, Tuple

try:
    from PIL import Image, ImageTk
except ImportError:
    Image = None
    ImageTk = None
    logging.warning("PIL not available. GUI will have limited functionality.")

logger = logging.getLogger(__name__)


class DraggableIcon(tk.Tk):
    """Draggable icon window with response panel."""
    
    # Default dimensions
    ICON_SIZE = 96
    PANEL_WIDTH = 320
    PANEL_HEIGHT = 140
    
    # Colors
    BG_COLOR = "#ff00ff"  # Magenta for transparency
    PANEL_BG = "#1e1e1e"  # Dark theme
    PANEL_FG = "#e8fdf8"  # Light text
    
    def __init__(self, image_path: str = None):
        """Initialize draggable icon.
        
        Args:
            image_path: Path to icon image file
        """
        super().__init__()
        
        try:
            # Window setup
            self.overrideredirect(True)
            self.attributes("-topmost", True)
            self.configure(bg=self.BG_COLOR)
            self.wm_attributes("-transparentcolor", self.BG_COLOR)
            self.attributes("-alpha", 0.95)
            
            # Drag tracking variables
            self._x = 0
            self._y = 0
            
            # Load and prepare icon
            self._setup_icon(image_path)
            
            # Setup UI components
            self._setup_canvas()
            self._setup_panel()
            
            # Bind mouse events
            self.bind("<ButtonPress-1>", self._start_move)
            self.bind("<B1-Motion>", self._do_move)
            
            logger.info("DraggableIcon initialized successfully")
        
        except Exception as e:
            logger.error(f"Error initializing DraggableIcon: {e}")
            raise
    
    def _setup_icon(self, image_path: Optional[str]) -> None:
        """Setup the icon image.
        
        Args:
            image_path: Path to icon image
        """
        if image_path and Path(image_path).exists() and Image:
            try:
                img = Image.open(image_path).resize(
                    (self.ICON_SIZE, self.ICON_SIZE),
                    Image.Resampling.LANCZOS
                )
                self.tk_img = ImageTk.PhotoImage(img)
                logger.info(f"Loaded icon: {image_path}")
            except Exception as e:
                logger.error(f"Error loading icon: {e}")
                self.tk_img = None
        else:
            logger.warning("Icon not found or PIL unavailable")
            self.tk_img = None
    
    def _setup_canvas(self) -> None:
        """Setup the canvas for icon display."""
        self.canvas = tk.Canvas(
            self,
            bg=self.BG_COLOR,
            highlightthickness=0,
            width=self.ICON_SIZE,
            height=self.ICON_SIZE
        )
        self.canvas.place(x=0, y=0, width=self.ICON_SIZE, height=self.ICON_SIZE)
        
        if self.tk_img:
            self.canvas.create_image(
                0, 0,
                anchor="nw",
                image=self.tk_img
            )
        else:
            # Fallback: draw a colored circle
            self.canvas.create_oval(
                5, 5,
                self.ICON_SIZE - 5, self.ICON_SIZE - 5,
                fill="purple",
                outline="white",
                width=2
            )
    
    def _setup_panel(self) -> None:
        """Setup the response panel."""
        self.panel = tk.Text(
            self,
            bg=self.PANEL_BG,
            fg=self.PANEL_FG,
            font=("Segoe UI", 11),
            wrap="word",
            bd=0,
            relief="flat",
            padx=10,
            pady=10
        )
        self.panel.place(
            x=self.ICON_SIZE + 10,
            y=10,
            width=self.PANEL_WIDTH - 20,
            height=self.PANEL_HEIGHT - 20
        )
        self.panel.config(state="disabled")
        
        # Set geometry
        self.geometry(
            f"{self.ICON_SIZE + self.PANEL_WIDTH}x{self.PANEL_HEIGHT}+100+100"
        )
    
    def show_panel(self, text: str) -> None:
        """Display text in the response panel.
        
        Args:
            text: Text to display
        """
        if not text or not isinstance(text, str):
            return
        
        try:
            self.panel.config(state="normal")
            self.panel.delete("1.0", "end")
            self.panel.insert("end", text.strip())
            self.panel.config(state="disabled")
            logger.debug(f"Displayed panel: {text[:50]}...")
        except Exception as e:
            logger.error(f"Error displaying panel: {e}")
    
    def _start_move(self, event) -> None:
        """Start dragging the window.
        
        Args:
            event: Mouse event
        """
        self._x = event.x
        self._y = event.y
    
    def _do_move(self, event) -> None:
        """Handle window dragging.
        
        Args:
            event: Mouse event
        """
        self.geometry(f"+{event.x_root - self._x}+{event.y_root - self._y}")
