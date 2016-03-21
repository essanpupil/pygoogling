"""Setup script for pygoogling."""
from codecs import open as open_codec
from os import path
from setuptools import setup

HERE = path.abspath(path.dirname(__file__))

with open_codec(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()


setup(
    name='pygoogling',
    version='0.0.2',
    description='Python library to do google search',
    long_description=LONG_DESCRIPTION,
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
        'Programming Language :: Python :: 3.4',
    ],
    keywords='google search python module',
    py_modules=['pygoogling.googling'],
    install_requires=['bs4', 'requests', 'html5lib'],
)
