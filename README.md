# Real Python article overview generator
## Installation instructions
```
$ python3 -m venv myenv
$ source myenv/bin/activate
$ pip install --upgrade pip setuptools
$ pip install -r requirements.txt
```
## Usage
Create a TXT file containing all URLs of the Real Python overview pages containing all articles.  
This can be done by running the following script and dump the results in a TXT file:
```
$ ./generate_urls.sh > urls.txt
```
Help screen of the Python program:
```
$ python generate_articles.py --help
usage: generate_articles.py [-h] [--print] [--html] url_file

Real Python article overview generator.

positional arguments:
  url_file    Input file with URLs.

optional arguments:
  -h, --help  show this help message and exit
  --print     Display raw format list.
  --html      Display HTML content.
```
