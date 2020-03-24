# Tests

This directory contains tests in order to ensure that functions, methods and classes properly work as wanted.
Every file **must** follow the naming convention of `test_<name>.py`, and every function inside the file that is wanted to test also must follow the same convention: `def test_<name>(...)`.

An example of a function for testing purposes looks as follows:

```python
# inside tests/test_file1.py file

from apackage.amodule import add

def test_addition():
    assert add(1, 2) == 3
    # 'assert'  is the keyword to work with testing
    # this test will succeed as 1+2 equals 3, otherwise it will fail, e.g.
    # assert add(1, 2) == 4
    # 1+2 is not equal to 4
```

The `add()` functions just returns a sum of two numbers:

```python
# inside apackage/amodule.py

def add(x, y):
    return x + y
```

The package used for testing this project is `pytest`, but it's not needed as it's not explicitly used in the code.
