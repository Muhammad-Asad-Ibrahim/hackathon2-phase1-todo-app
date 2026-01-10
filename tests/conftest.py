"""
Configuration for pytest.
"""
import sys
import os
from pathlib import Path

# Add src directory to Python path to import todo_app modules
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))