import sys
import os
from pathlib import Path

print(__file__)
sys.path.append(str(Path(__file__).resolve().parent))
sys.path.append(str(Path(os.getcwd()) / Path('layer_builder/table_model/python')))
print(sys.path)
