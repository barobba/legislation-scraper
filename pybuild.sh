#!/usr/bin/env bash

# See https://packaging.python.org/en/latest/tutorials/packaging-projects/#generating-distribution-archives
pip install --upgrade build
python -m build
