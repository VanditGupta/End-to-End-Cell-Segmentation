# This file looks for __init__.py files in the project directory so that they can be considered as local packages.
# https://stackoverflow.com/questions/1471994/what-is-setup-py
# Helps to package the project and install it using pip install .

from setuptools import find_packages, setup

setup(
    name = 'cellSegmentation',
    version= '0.0.0',
    author= 'Vandit Gupta',
    author_email= 'vanditgupta22@gmail.com',
    packages= find_packages(),
    install_requires = []
)