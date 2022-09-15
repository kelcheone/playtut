from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=50)
    page = browser.new_page()
    page.goto("https://chrome.google.com/webstore/category/ext/11-web-development")

    html = page.inner_html("role=row")
    soup = BeautifulSoup(html, "html.parser")

    page.evaluate(
    """
    var intervalID = setInterval(function () {
        var scrollingElement = (document.scrollingElement || document.body);
        scrollingElement.scrollTop = scrollingElement.scrollHeight;
    }, 200);

    """
        )
    prev_height = None
    while True:
        curr_height = page.evaluate('(window.innerHeight + window.scrollY)')
        if not prev_height:
            prev_height = curr_height
            time.sleep(1)
        elif prev_height == curr_height:
            page.evaluate('clearInterval(intervalID)')
            break
        else:
            prev_height = curr_height
            time.sleep(1)
    # find all rows
    # print(soup.find_all( "div", {"role": "row"}))