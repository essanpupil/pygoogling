# pygoogling
[![Documentation Status](https://readthedocs.org/projects/pip/badge/)](http://pygoogling.readthedocs.org/en/latest/)
Using google search engine from python

## Installation
I haven't upload this to pypi yet. But you can install this package by  
following this instruction bellow.
```
git clone https://github.com/essanpupil/pygoogling.git
cd pygoogling
python setup.py install
```
## Usage
```
>>> from pygoogling.googling import GoogleSearch
>>> googling = GoogleSearch('python')

# max_page is optional, by default the value will be 1
googling.start_search(max_page=1)
>>> for link in googling.search_result:
...     print link
...
https://www.python.org/
https://en.wikipedia.org/wiki/Python_(programming_language)
https://www.codecademy.com/learn/python
https://www.python.org/
http://weknowyourdreamz.com/python.html
http://www.telegraph.co.uk/news/earth/wildlife/11809197/Escaped-9ft-python-on-loose-in-Shoebury-in-Essex.html
http://weknowyourdreamz.com/python.html
https://realpython.com/learn/python-first-steps
http://www.tutorialspoint.com/python/
http://www.learnpython.org/
https://www.reddit.com/r/Python/
https://www.python.org/
https://en.wikipedia.org/wiki/Python_(programming_language)
https://www.codecademy.com/learn/python
https://www.python.org/
http://weknowyourdreamz.com/python.html
http://www.telegraph.co.uk/news/earth/wildlife/11809197/Escaped-9ft-python-on-loose-in-Shoebury-in-Essex.html
http://weknowyourdreamz.com/python.html
https://realpython.com/learn/python-first-steps
http://www.tutorialspoint.com/python/
http://www.learnpython.org/
https://www.reddit.com/r/Python/

# more_page is required. You have to specified how many more page you want to
# access. The result will be appended to the current result
googling.more_search(more_page=1)
>>> googling.more_search(more_page=1)
>>> for link in googling.search_result:
...     print link
...
https://www.python.org/
https://en.wikipedia.org/wiki/Python_(programming_language)
https://www.codecademy.com/learn/python
https://www.python.org/
http://weknowyourdreamz.com/python.html
http://www.telegraph.co.uk/news/earth/wildlife/11809197/Escaped-9ft-python-on-loose-in-Shoebury-in-Essex.html
http://weknowyourdreamz.com/python.html
https://realpython.com/learn/python-first-steps
http://www.tutorialspoint.com/python/
http://www.learnpython.org/
https://www.reddit.com/r/Python/
https://www.python.org/
https://en.wikipedia.org/wiki/Python_(programming_language)
https://www.codecademy.com/learn/python
https://www.python.org/
http://weknowyourdreamz.com/python.html
http://www.telegraph.co.uk/news/earth/wildlife/11809197/Escaped-9ft-python-on-loose-in-Shoebury-in-Essex.html
http://weknowyourdreamz.com/python.html
https://realpython.com/learn/python-first-steps
http://www.tutorialspoint.com/python/
http://www.learnpython.org/
https://www.reddit.com/r/Python/
http://www.pythoncarsecurity.com/
http://www.lynda.com/Python-training-tutorials/415-0.html
http://showmedo.com/videotutorials/python
http://montrealpython.org/
https://github.com/google/google-api-python-client
https://www.continuum.io/downloads
http://greenteapress.com/wp/think-python/
https://www.edx.org/course/introduction-python-data-science-microsoft-dat208x-0
http://pythonnet.sourceforge.net/
```
