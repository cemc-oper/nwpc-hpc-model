from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='nwpc-hpc-model',

    version='0.3.2',

    description='A collection of models for HPC used in NWPC.',
    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/perillaroc/nwpc-hpc-model',

    author='perillaroc',
    author_email='perillaroc@gmail.com',

    license='GPL-3.0',

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],

    keywords='nwpc hpc model',

    packages=find_packages(exclude=[
        'contrib', 'docs', 'tests', 'docker'
    ]),

    install_requires=[],

    extras_require={
        'test': [
            'pyyaml',
            'pytest',
            'pytest-cov',
            'codecov'
        ],
        'cov': [
            'pytest-cov',
            'codecov'
        ]
    },

    entry_points={}
)
