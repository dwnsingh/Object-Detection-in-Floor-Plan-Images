import os
import urllib.request as ulib
from bs4 import BeautifulSoup as Soup
import json
from urllib.request import urlopen, Request 

url_a = 'https://www.google.com/search?q={}'
url_b = '\&client=ubuntu&hs=pWC&channel=fs&source=lnms'
url_c = '\&tbm=isch&sa=X&ved=0ahUKEwiZ3ZGB0MHdAhUHtY8KHVe2AAYQ_AUIDigB&biw=1301&bih=670'
# url_d = '\.i&ijn=1&asearch=ichunk&async=_id:rg_s,_pms:s'
url_base = ''.join((url_a, url_b, url_c))

headers = {'User-Agent': 'Chrome/41.0.2228.0 Safari/537.36 Mozilla/5.0'}


def get_links(search_name):
    search_name = search_name.replace(' ', '+')
    url = url_base.format(search_name)
    request = Request(url, None, headers)
    # json_string = ulib.urlopen(request).read()
    # page = json.loads(json_string)
    page = urlopen(request).read()
    new_soup = Soup(page, "html.parser")
    images = new_soup.find_all('img')
    links = [image['src'] for image in images]
    return links


def save_images(links, search_name):
    directory = search_name.replace(' ', '_')
    if not os.path.isdir(directory):
        os.mkdir(directory)

    for i, link in enumerate(links):
        savepath = os.path.join(directory, '{:06}.jpg'.format(i))
        ulib.urlretrieve(link, savepath)


if __name__ == '__main__':
    search_name = 'car img'
    links = get_links(search_name)
    save_images(links, search_name)

