#! python3
# Get links on a page, check for broken links on each page.

# Requirements:
# pip3 install beautifulsoup4
# pip3 install requests

import requests
from bs4 import BeautifulSoup, SoupStrainer
from urllib.parse import urlsplit


def get_page_links(url):
    response = requests.get(url)

    # Get the content of the page as text
    content = response.text

    # Get base URL in case we need it for relative URL links. No trailing slash after .com, .org, etc.
    base_url = "{0.scheme}://{0.netloc}".format(urlsplit(url))
    
    # Will contain all the links on this page
    link_list = []
    
    # For every link found on the page...
    for link in BeautifulSoup(content, 'html.parser', parse_only=SoupStrainer('a')):
        # Make sure the <a> has an href and is not an email link
        if link.has_attr('href') and not link['href'].startswith('mailto:'):
            # Check if URLs start with /, #, or ?. If they do, first put the current URL or host in front of it to make a full path
            if link['href'].startswith('?') or link['href'].startswith('#'):
                link_list.append(url + link['href'])
            elif link['href'].startswith('/'):
                link_list.append(base_url + link['href'])
            else:
                link_list.append(link['href'])
    
    return link_list


def check_page_links(url_list):
    broken_link_list = []
    for url in url_list:
        try:
            print(url)
            res = requests.get(url)
            res.raise_for_status()
            print("Status: " + str(res.status_code))
        except requests.exceptions.HTTPError as e:
            print(e)
            broken_link_list.append(url)

        print('\n\n')

    return broken_link_list



# When you run... 
# python3 link-checker.py
# ...in the command line, it will run this:
if __name__ == "__main__":
    # Prompt user to provide the URL to check
    url = input("### Check a page's links for 404 errors ###\n\n\nEnter the URL:\n\n")

    # Get list of links found on this page
    url_list = get_page_links(url)

    # For each page link, check the status
    broken_links = check_page_links(url_list)

    # Print report of broken links:
    if broken_links:
        print("\x1b[31m### Broken Links Found: ###\x1b[0m")
        for link in broken_links:
            print(link)
    else:
        print("\x1b[32m### No Broken Links on Page! ###\x1b[0m")
    
    print("\n\t*\t*\t*\n")
