from playwright.sync_api import sync_playwright
import pandas as pd
import os
def fetch_text(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        content = page.text_content("body")  # raw .txt file, no classes expected
        browser.close()
        return content

if __name__ == "__main__":
    text_data = fetch_text('https://raw.githubusercontent.com/openphish/public_feed/refs/heads/main/feed.txt')
    label ='Phishing'
    links=[]
    urls=text_data.strip().split('\n')
    for url in urls:
         links.append({
                            "url": url,
                            "label" : label
                        })

    df=pd.DataFrame(links)
    df.to_csv('../Data/phishing_link.csv', mode='a', index=False, header=False)
    #write text data to .file

