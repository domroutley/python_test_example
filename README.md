# python_test_example

## Virtual env
- To create a new virtual python env  
  `python3 -m venv [name of folder to put venv in]`  
  Standards are either `.venv` or `venv` for the folder name

- To activate your virtual env  
  `source [path to your venv]/bin/activate`

- To test that your virtual env is active  
  `which python` <- should return a path ending `[path to your venv]/bin/python` NOT `/usr/bin/python`

- To deactivate your virtual env  
  `deactivate`

## Testing
- To run tests  
  `python -m unittest test_example.py`
- For more/better examples see > https://docs.python.org/3.7/library/unittest.html#command-line-interface

## Docs
unittest - https://docs.python.org/3.7/library/unittest.html  
unittest.mock - https://docs.python.org/3.7/library/unittest.mock.html
