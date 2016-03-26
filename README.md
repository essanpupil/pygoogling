# pygoogling
[![Code Issues](https://www.quantifiedcode.com/api/v1/project/bfbfe707e09b4f109913969336393abf/badge.svg)](https://www.quantifiedcode.com/app/project/bfbfe707e09b4f109913969336393abf)  
Using google search engine from python

## Tested python version
- python 2.7.6
- python 3.4.3  

## Installation
I haven't upload this to pypi yet. But you can install this package by  
following this instruction bellow.
```shell
git clone https://github.com/essanpupil/pygoogling.git
cd pygoogling
python setup.py install
```

## Usage
For now, this library only contain one class, `GoogleSearch`. Here is a short description to use this library.  

```python
from pygoogling.googling import GoogleSearch

google_search = GoogleSearch('python')
google_search.start_search(max_page=3)
print(len(google_search.search_result))
10
print(google_search.search_result)
['https://www.python.org/', 'https://www.codecademy.com/learn/python', 'https://www.python.org/', . . .]
google_search.more_page(4)
print(len(google_search.search_result))
40
print(google_search.search_result)
['https://www.python.org/', 'https://www.codecademy.com/learn/python', 'https://www.python.org/', . . .]
```
The keyword is the only requirement to initiate this class. The `max_page` parameter is used to determine how many google web page result you want to parse. By default, `max_page` will be 1. The `GoogleSearch.more_page()` is a method used to do extra search. The only required parameter is how many more pages you want to get the result of google search.
