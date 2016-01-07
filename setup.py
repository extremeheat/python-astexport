# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

version = "1.0.0"

description = "Python command line application to export Python AST as Json."

with open(path.join(here, "README.rst"), encoding="utf-8") as f:
    long_descr = f.read()

setup(
    name = "astexport",
    version = version,

    description = description,
    long_description = long_descr,
    license = "MIT",
    url = "https://github.com/fpoli/python-astexport",

    author = "Federico Poli",
    author_email = "federpoli@gmail.com",

    packages = find_packages(exclude=["tests"]),

    entry_points = {
        "console_scripts": [
            "astexport = astexport.cli:main"
        ]
    },

    install_requires = [
    ],
    extras_require = {
        "dev": [
            "meta",
            "twine",
            "nose == 1.3.3",
            "pep8 == 1.4.6"
        ]
    },

    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Compilers",
        "Topic :: Software Development :: Disassemblers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5"
    ]
)
