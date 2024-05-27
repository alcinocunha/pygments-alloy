#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='pygments-alloy',
    version='0.2',
    description='Pygments lexer for Alloy.',
    keywords='pygments alloy lexer',
    license='GPL v2.0',

    author='Alcio Cunha',
    author_email='alcino@di.uminho.pt',

    url='https://github.com/alcinocunha/pygments-alloy.git',

    packages=find_packages(),
    install_requires=['pygments >= 1.4'],

    entry_points='''[pygments.lexers]
                    alloy=src:AlloyLexer
    
                    [pygments.styles]
                    alloy=src:AlloyStyle''',

    classifiers=[],
)
