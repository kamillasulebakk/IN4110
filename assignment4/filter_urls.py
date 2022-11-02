import re
from urllib.parse import urljoin
from requesting_urls import get_html

## -- Task 2 -- ##

def find_urls(
    html: str,
    base_url: str = "https://en.wikipedia.org",
    output: str = None,
) -> set:
    """Find all the url links in a html text using regex
    Arguments:
        html (str): html string to parse
    Returns:
        urls (set) : set with all the urls found in html text
    """
    # finding full URL matches
    anchor_pat = re.compile(r"<a([^>]+)>", flags=re.IGNORECASE)
    # href_pat = re.compile(r'href="(https?:[^":]+?)(?:\#.*?)?".*?>.*?', flags=re.IGNORECASE)
    href_pat = re.compile(r'href="(https?:[^":]+?)"', flags=re.IGNORECASE)
    # href_pat = re.compile(r'href="([^"]+)"', re.IGNORECASE)
    url_set = set()

    # 1. find all the anchor tags, then
    for anchor_tag in anchor_pat.findall(html):
        # 2. find the urls href attributes
        match = href_pat.search(anchor_tag)
        if match:
            url_set.add(match.group(1))

    # finding path URL matches starting with a single forward slash /
    rel_href_pat = re.compile(r'href="((?:/[^/:]+?)+)(?:\#.*?)?".*?', flags=re.IGNORECASE)

    if base_url:
        for anchor_tag in anchor_pat.findall(html):
            rel_match = rel_href_pat.search(anchor_tag)
            if rel_match:
                match = base_url + rel_match.group(1)
                url_set.add(match)

    # finding URL matches starting with a double forward slash //
    href_pat_2slash = re.compile(r'href="(/(?:/[^:]*?)+)(?:\#.*?)?".*?', flags=re.IGNORECASE)
    # rel2_matches = list(set(rel2_matches))  # remove duplicates
    # start = base_url.split('//')[0]

    if base_url:
        for anchor_tag in anchor_pat.findall(html):
            match_2slash = href_pat_2slash.search(anchor_tag)
            if match_2slash:
                match = 'https:' + match_2slash.group(1)
                url_set.add(match)


    # Write to file if requested
    if output:
        print(f"Writing to: {output}")
        with open(f'{output}', 'w') as f:
            for elem in url_set:
                f.write(elem + "\n")
            f.close()

    return url_set


def find_articles(html: str, output=None) -> set:
    """Finds all the wiki articles inside a html text. Make call to find urls, and filter
    arguments:
        - text (str) : the html text to parse
    returns:
        - (set) : a set with urls to all the articles found
    """
    urls = find_urls(html)
    pattern = re.compile(r'https?://\w+\.wikipedia.org', flags=re.IGNORECASE)
    articles = set()

    for url in urls:
        match = pattern.search(url)
        if match:
            articles.add(url)

    # Write to file if wanted
    if output:
        print(f"Writing to: {output}")
        with open(f'{output}', 'w') as f:
            for elem in articles:
                f.write(elem + "\n")
            f.close()

    return articles


## Regex example
def find_img_src(html: str):
    """Find all src attributes of img tags in an HTML string

    Args:
        html (str): A string containing some HTML.

    Returns:
        src_set (set): A set of strings containing image URLs

    The set contains every found src attibute of an img tag in the given HTML.
    """
    # img_pat finds all the <img alt="..." src="..."> snippets
    # this finds <img and collects everything up to the closing '>'
    img_pat = re.compile(r"<img[^>]+>", flags=re.IGNORECASE)
    # src finds the text between quotes of the `src` attribute
    src_pat = re.compile(r'src="([^"]+)"', flags=re.IGNORECASE)
    src_set = set()
    # first, find all the img tags
    for img_tag in img_pat.findall(html):
        # then, find the src attribute of the img, if any
        match = src_pat.search(img_tag)
        if match:
            src_set.add(match.group(1))
    return src_set

if __name__ == '__main__':
    find_urls('<a id="some-id" href="/relative/path#fragment">relative link</a>', base_url="https://en.wikipedia.org", output='test')