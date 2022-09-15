from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://demo.opencart.com/admin/")
    page.fill("input#input-username", "demo")
    page.fill("input#input-password", "demo")
    page.click("button.btn-primary")
    
    page.click("button.btn-close")
    
    html = page.inner_html("#content")
    soup = BeautifulSoup(html, "html.parser")
    total_orders = soup.find('h2', {'class': 'float-end'}).text

    print (f"Total Orders: {total_orders}")