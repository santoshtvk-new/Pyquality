import yaml
import os

def load_aliases():
    alias_path = os.path.join(os.path.dirname(__file__), "..", "..", "METHOD_ALIASES.yml")
    if not os.path.exists(alias_path):
        return {}
    with open(alias_path, 'r') as f:
        return yaml.safe_load(f)

# The loaded aliases can be used by the browser instance to dynamically map methods.
ALIASES = load_aliases()

from .api import API
__version__ = "0.1.0"
