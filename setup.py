#!/usr/bin/env python

from distutils.core import setup


def _requirements():
    """ Load `requirements.txt` and read its contents """
    with open('requirements.txt') as src:
        return src.read().splitlines()


setup(
    name='SpotiPaper',
    version='0.1',
    description='Python Distribution Utilities',
    url='https://github.com/sebastianseitz/SpotiPaper',
    packages=['spotipaper'],
    install_requires=_requirements(),
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: MacOS',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ]
)
