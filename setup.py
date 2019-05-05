# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='space-invasor',
    version='1.0',
    description='space invasor',
    long_description=readme,
    author='Humberto Arndt',
    author_email='humberto.arndt@gmail.com',
    url='https://github.com/hrndt93/space-invasor',
    license=license,
    python_requires='>=3.6',
    packages=find_packages(exclude=('tests', 'docs'))
)

