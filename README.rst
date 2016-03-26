==========
pygoogling
==========
.. image:: https://badge.fury.io/py/pygoogling.svg
    :target: https://badge.fury.io/py/pygoogling
    :alt: pypi package version
.. image:: https://www.quantifiedcode.com/api/v1/project/bfbfe707e09b4f109913969336393abf/badge.svg
  :target: https://www.quantifiedcode.com/app/project/bfbfe707e09b4f109913969336393abf
  :alt: Code issues

Using google search engine from python

Tested python version
*********************
- python 2.7.6
- python 3.4.3

Installation
************
.. code-block:: bash

  $ pip install pygoogling

Usage
*****
For now, this library only contain one class, ``GoogleSearch``. Here is a short description to use this library.

.. code-block:: python

  from pygoogling.googling import GoogleSearch


  google_search = GoogleSearch('python')
  google_search.start_search(max_page=3)
  print(google_search.search_result) # will print the url as list of string
  google_search.more_page(4) # to search 4 extra pages
  print(google_search.search_result) # the result will be added to current result

The keyword is the only requirement to initiate this class. The ``max_page`` parameter is used to determine how many google web page result you want to parse. By default, ``max_page`` will be one. The ``GoogleSearch.more_page()`` is a method used to do extra search. The only required parameter is how many more pages you want to get the result of google search.
