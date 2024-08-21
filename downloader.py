# MIT License
#
# Copyright (c) [2024] [Rohit Vaidya]
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from bs4 import BeautifulSoup
import requests
import sys

# Install these deps to run the script
# pip install requests
# pip install bs4

def parse_local_html(file_path):
  """Parses a local HTML file using BeautifulSoup.

  Args:
    file_path: The path to the HTML file.

  Returns:
    A BeautifulSoup object representing the parsed HTML.
  """

  with open(file_path, 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')
  return soup

def download_and_save_images(url_list):
  """Iterates throught the list of URLs and downloads them.

  Args:
    url_list: A list of URLs.
  """
  x=1
  for url in url_list:
    download_image(url, str(x)+".jpg")
    x=x+1

def download_image(url, filename):
    print(f"Downloading image: {url}")
    img_data = requests.get(url).content
    print(f'Saving to file: {filename}')
    try:
        with open(filename, 'wb') as file:
            file.write(img_data)
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except PermissionError as e:
        print(f"Permission denied: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def parse_html_get_urls(html_file_path):
    soup = parse_local_html(html_file_path)
    # Procare uses the following prefix for all images
    prefix = 'https://private.kinderlime.com/photos/files/'
    urls = []
    for link in soup.find_all('a', href=True):
        href = link['href']
        if href.startswith(prefix):
          urls.append(href)
    return urls

def main(file_path):
    urls = parse_html_get_urls(file_path)
    download_and_save_images(urls)
    print('Done!')

if __name__ == '__main__':
    print(len(sys.argv))
    if len(sys.argv) > 1:
       main(sys.argv[1])
    else:
       print("Argument missing. Enter path to procare html file")