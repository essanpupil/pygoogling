from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='pygoogling',
    version='0.0.1',
    description='Python library to do google search',
    long_description=long_description,
    url='https://github.com/essanpupil/pygoogling',
    author='Ikhsan Noor Rosyidin',
    author_email='jakethitam1985@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='google search python module',
    py_modules=['pygoogling.googling'],
    install_requires=['bs4','requests','html5lib'],
)