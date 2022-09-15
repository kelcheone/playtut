from playwright.sync_api import Playwright, sync_playwright
import time


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # page.goto('https://www.youtube.com/')
    page.goto('https://chrome.google.com/webstore/category/ext/11-web-development')

    # page.mouse.wheel(horizontally, vertically(positive is 
    # scrolling down, negative is scrolling up)
    for i in range(5): #make the range as long as needed
        page.mouse.wheel(0, 15000000)
        time.sleep(2)
        i += 1
    
    time.sleep(15)
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)