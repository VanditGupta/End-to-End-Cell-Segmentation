# This file looks for __init__.py files in the project directory so that 
# they can be considered as local packages.

from setuptools import find_packages, setup

setup(
    name = 'cellSegmentation',
    version= '0.0.0',
    author= 'Vandit Gupta',
    author_email= 'vanditgupta22@gmail.com',
    packages= find_packages(),
    install_requires = []
)