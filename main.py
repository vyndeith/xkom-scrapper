from camoufox import Camoufox

def read_links_from_file(filename):
    with open(filename, 'r') as file:
        links = []
        for line in file:
            line = line.strip()
            if line:
                links.append(line)
        return links
    
def get_product_info(page, url):
    page.goto(url, wait_until='domcontentloaded') #little optimization for no waiting images and other rsc :P
    page.wait_for_selector('[data-name="productPrice"]') 
    
    full_title = page.title()
    product_name = full_title.split('-')[0].strip()

    price_element = page.query_selector('[data-name="productPrice"] span:first-child')
    product_price = price_element.inner_text() if price_element else 'Price not found'
    return product_name, product_price

def main():
    links = read_links_from_file('links.txt')
    
    with Camoufox(headless=True) as browser:
        page = browser.new_page()
        
        for link in links:
            name, price = get_product_info(page, link)
            print(f"{name}: {price}")

main()