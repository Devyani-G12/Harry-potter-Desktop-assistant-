"""Configuration Management Module

Handles loading, saving, and managing assistant configuration.
"""

import json
import logging
from pathlib import Path
from typing import Dict, Any

logger = logging.getLogger(__name__)

CONFIG_FILE = "assistant_config.json"

DEFAULT_CONFIG = {
    "wake_words": ["harry", "potter", "dev", "assistant"],
    "audio_sample_rate": 16000,
    "audio_buffer_seconds": 3,
    "whisper_model": "tiny",
    "ui_alpha": 0.95,
    "ui_theme": "dark",
    "auto_start": True,
    "debug_mode": False,
    "max_retries": 3
}


class ConfigManager:
    """Manages application configuration."""
    
    def __init__(self, config_file: str = CONFIG_FILE):
        """Initialize configuration manager.
        
        Args:
            config_file: Path to configuration file
        """
        self.config_file = config_file
        self.config = self._load_config()
    
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from file or use defaults.
        
        Returns:
            Dictionary with configuration
        """
        if not Path(self.config_file).exists():
            logger.info(f"Creating new config file: {self.config_file}")
            self.save_config(DEFAULT_CONFIG)
            return DEFAULT_CONFIG.copy()
        
        try:
            with open(self.config_file, "r") as f:
                config = json.load(f)
            
            # Merge with defaults for new keys
            for key, value in DEFAULT_CONFIG.items():
                config.setdefault(key, value)
            
            logger.info(f"Loaded config from {self.config_file}")
            return config
        
        except json.JSONDecodeError:
            logger.error(f"Invalid JSON in {self.config_file}. Using defaults.")
            return DEFAULT_CONFIG.copy()
        except IOError as e:
            logger.error(f"Error reading config file: {e}. Using defaults.")
            return DEFAULT_CONFIG.copy()
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get a configuration value.
        
        Args:
            key: Configuration key
            default: Default value if key not found
        
        Returns:
            Configuration value or default
        """
        return self.config.get(key, default)
    
    def set(self, key: str, value: Any) -> None:
        """Set a configuration value.
        
        Args:
            key: Configuration key
            value: Configuration value
        """
        self.config[key] = value
        self.save_config()
    
    def save_config(self, config: Dict[str, Any] = None) -> bool:
        """Save configuration to file.
        
        Args:
            config: Configuration dictionary to save
        
        Returns:
            True if saved successfully, False otherwise
        """
        try:
            config = config or self.config
            with open(self.config_file, "w") as f:
                json.dump(config, f, indent=4)
            logger.info(f"Saved config to {self.config_file}")
            return True
        except IOError as e:
            logger.error(f"Failed to save config: {e}")
            return False
    
    def reset_to_defaults(self) -> None:
        """Reset configuration to defaults."""
        self.config = DEFAULT_CONFIG.copy()
        self.save_config()
        logger.info("Configuration reset to defaults")


# Global config instance
_config_manager = ConfigManager()


def get_config() -> ConfigManager:
    """Get the global configuration manager.
    
    Returns:
        ConfigManager: The global config instance
    """
    return _config_manager
