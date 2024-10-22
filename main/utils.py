import sys
import logging
import importlib
from pathlib import Path

def load_plugins(plugin_name):
    path = Path(f"main/plugins/{plugin_name}.py")
    # Check if the plugin exists
    if not path.is_file():
        raise FileNotFoundError(f"Plugin '{plugin_name}' not found at path: {path}")
    name = f"main.plugins.{plugin_name}"
    # Load the plugin module
    try:
        spec = importlib.util.spec_from_file_location(name, path)
        load = importlib.util.module_from_spec(spec)
        load.logger = logging.getLogger(plugin_name)
        spec.loader.exec_module(load)
        sys.modules[f"main.plugins.{plugin_name}"] = load
        print(f"main has Imported {plugin_name}")
    except Exception as e:
        logging.error(f"Failed to load plugin {plugin_name}: {e}")
        raise