"""
Real Python article generator.

Creates a list in HTML format with all Real Python articles.
"""

import argparse
import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://realpython.com'
VERSION = '1.0.0'


def read_data(input_file):
    """Read all lines from the input file."""
    try:
        with open(input_file, 'r') as infile:
            return infile.read().splitlines()
    except (FileNotFoundError, PermissionError, FileExistsError) as error:
        raise ValueError(error)


def retrieve_articles(urls):
    """Retrieve all articles."""
    result = []
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        for elem in soup.find_all('h2', class_='card-title'):
            title = elem.text
            url = BASE_URL + elem.find_previous('a').get('href')
            date = elem.find_next('span').text
            try:
                join = True if 'fa-star' in elem.find_next('i').attrs['class'] else False
            except AttributeError:
                join = False
            result.append((title, url, date, join))
    return result


def print_articles(articles):
    """Print all articles."""
    for article_id, article in enumerate(articles, 1):
        print(article_id, article)


def generate_html(articles):
    """Generate HTML content for articles."""
    html = '<!DOCTYPE html><html><head><meta charset="utf-8"><title>Real Python articles</title><head><body><ol>'
    for article in articles:
        html += f'<li><a href="{article[1]}">{article[0]}</a>'
        if article[3]:
            html += '<b> ! JOIN !</b>'
    html += '</ol></body></html>'
    print(html)


def main():
    """Main function."""
    parser = argparse.ArgumentParser(description='Real Python article overview generator.')
    parser.add_argument('--version', action='version', version=VERSION)
    parser.add_argument('url_file', help='Input file with URLs.')
    parser.add_argument('--print', action='store_true', help='Display raw format list.')
    parser.add_argument('--html', action='store_true', help='Display HTML content.')
    args = parser.parse_args()
    try:
        urls = read_data(args.url_file)
    except ValueError as err:
        print('An error has occurred!')
        print(err)
    else:
        articles = retrieve_articles(urls)
        if args.print:
            print_articles(articles)
        if args.html:
            generate_html(articles)


if __name__ == '__main__':
    main()
