import re
from urllib.parse import urljoin

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
    # create and compile regular expression(s)

    # 1. find all the anchor tags, then
    a_pat = re.compile(r"<a[^>]+>", flags=re.IGNORECASE)
    # 2. find the urls href attributes
    src_pat = re.compile(r'href="([^"#]+)')
    src_set = set()

    for a_tag in a_pat.findall(html):
        # then, find the src attribute of the img, if any
        match = src_pat.search(a_tag)

        if match:
            url = match.group(1)

            if url.startswith("//"):
                url = "https:" + url

            elif url.startswith("/"):
                url = base_url + url

            src_set.add(url)


    # Write to file if requested
    if output:
        print(f"Writing to: {output}")
        f = open(output, "w", encoding="utf-8")
        for txt in src_set:
            f.write(txt)
            f.write("\n")

    return src_set


def find_articles(html: str, output=None, english=False) -> set:
    """Finds all the wiki articles inside a html text. Make call to find urls, and filter
    arguments:
        - text (str) : the html text to parse
        - english (bool) : If you only want english articles returned
    returns:
        - (set) : a set with urls to all the articles found
    """
    urls = find_urls(html, output=output)
    pattern = re.compile(r'https://\w+.wikipedia.org\/wiki[^:"]+', flags = re.IGNORECASE)
    # if english:
    #     pattern = re.compile(r'https://en.wikipedia.org\/wiki[^:"]+', flags = re.IGNORECASE)
    articles = set()
    for url in urls:
        match = pattern.search(url)
        if match:
            articles.add(match.group(0))

    # Write to file if wanted
    if output:
        print(f"Writing to: {output}")
        f = open(output, "w", encoding="utf-8")
        for txt in articles:
            f.write(txt)
            f.write("\n")

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
