from setuptools import setup, find_packages
import codecs

setup(

    # Versions should comply with PEP440. For single-sourced versioning, see
    # http://packaging.python.org/en/latest/tutorial.html#version
    version= '0.0.1',

    description='A sample Python project',
    long_description='Hi',

    # The project URL.
    url='https://github.com/dghubble/pypkg',

    # Author details
    author='Dalton Hubble',
    author_email='dghubble@gmail.com',

    # Choose your license
    license='MIT',
    
    # What does your project relate to?
    keywords='pypkg setuptools development',

    # Run-time package dependencies. These will be installed by pip when your
    # project is installed.
    install_requires=[
        'requests',
    ]
)
