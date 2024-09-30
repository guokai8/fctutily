# setup.py

from setuptools import setup, find_packages

setup(
    name='fctutils',
    version='0.1.0',
    description='A Python package for factor manipulation and analysis, mirroring R\'s fctutils.',
    author='Kai Guo',
    author_email='guokai8@gmail.com',
    packages=find_packages(),
    install_requires=[
        'pandas>=1.0.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
