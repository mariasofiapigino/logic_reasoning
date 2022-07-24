# Logic Reasoning

[![](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

## What's here

### Balanced Parentheses

**count_balanced_parentheses** is a function that receives a string and returns true if the string has balanced parentheses (A sequence of characters is understood to be correctly balanced with respect to parentheses if each of the opening parentheses has its closed parentheses).
As an example, `((()()))` returns `true`, while `((()` returns `false`.

### Find and multiply

Given a list of numbers, it finds two of them that add up to 2022 and returns the product of them.
As an example, the list `[1.5, 1010, 1012]` returns `1.022.120`. 

## Contributing

1. **Fork this repo**   
2. **Git clone**
    ```bash
    $ git clone git@github.com:mariasofiapigino/logic_reasoning.git
    ```
3. **Poetry install**
    ```bash
    $ poetry install
    ```
### Testing
Tests were developed with pytest.
```bash
  $ pytest
```
