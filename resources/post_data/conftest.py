import pytest
import sys
import pathlib


@pytest.fixture(scope="function", autouse=True)
def setup():
    print('hello test')
    print(__file__)
    sys.path.append(str(pathlib.Path(__file__).resolve().parent))
    print(sys.path)
