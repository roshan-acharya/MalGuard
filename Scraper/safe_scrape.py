from playwright.async_api import async_playwright
import asyncio
import pandas as pd

async def Scrape(url):
   async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto(url)
        await page.select_option('select[name="top-domains-table_length"]', value="5000")
        await page.wait_for_selector("td.text-left")

        await page.wait_for_function(
            """() => document.querySelectorAll('#top-domains-table td').length >= 5000"""
        )
        td_elements = await page.query_selector_all("td.text-left")
        # Await inner_text() for each element inside async comprehension
        texts = [await td.inner_text() for td in td_elements]
        texts = [text.strip() for text in texts]
        return texts

if __name__ == "__main__":
    urls=asyncio.run(Scrape('https://www.domcop.com/top-10-million-websites'))
    label="Safe"
    
    for i in range(0,5000):
        links=[]
        urls[i]=urls[i]
        links.append({
                            "url": urls[i],
                            "label" : label
                        })
                        
        
        df=pd.DataFrame(links)
        df=df['url'].apply(lambda x:"https://"+str(x))
        print(links)
        df.to_csv('../Data/safe_link.csv', mode='a', index=False, header=False)