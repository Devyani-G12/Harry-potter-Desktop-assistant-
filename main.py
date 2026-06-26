"""Harry Potter Desktop Assistant - Main Entry Point

This module initializes and starts the desktop assistant with GUI and voice listening.
"""

import threading
import logging
import sys
from pathlib import Path

from janu_icon import DraggableIcon
from janu_detect import start_listening

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def main():
    """Initialize and start the Harry Potter Desktop Assistant."""
    try:
        logger.info("🧙‍♂️ Initializing Harry Potter Desktop Assistant...")
        
        # Check for icon file
        icon_path = "hp.png"
        if not Path(icon_path).exists():
            logger.warning(f"Icon file '{icon_path}' not found. Using default icon.")
            # Create a simple default icon if not found
            try:
                from PIL import Image
                img = Image.new('RGB', (96, 96), color='purple')
                img.save(icon_path)
                logger.info(f"Created default icon: {icon_path}")
            except ImportError:
                logger.error("PIL not available for creating default icon")
                sys.exit(1)
        
        # Initialize GUI
        logger.info("Creating GUI...")
        icon = DraggableIcon(icon_path)
        icon.show_panel("🧙‍♂️ Harry Potter Assistant\nListening...")
        
        # Start voice listening in background thread
        logger.info("Starting voice listener...")
        listener_thread = threading.Thread(
            target=start_listening,
            args=(icon,),
            daemon=True,
            name="AudioListener"
        )
        listener_thread.start()
        
        logger.info("✨ Assistant started. Listening for voice commands...")
        
        # Start GUI main loop
        icon.mainloop()
        
    except Exception as e:
        logger.error(f"Failed to start assistant: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
