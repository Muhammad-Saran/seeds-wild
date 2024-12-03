from playwright.sync_api import sync_playwright
import time

def wait_for_cloudflare_to_bypass(page):
    print("Cloudflare protection detected. Please complete the CAPTCHA or wait for it to pass.")
    
    # Loop to check if the Cloudflare protection is still present
    while page.query_selector("xpath=/html/body/div[1]/div") is not None:
        print("Waiting for Cloudflare protection to be bypassed...")
        time.sleep(5)  # Wait for a few seconds before checking again
    
    print("Cloudflare protection bypassed. Resuming normal execution.")

def main():
    link = "https://davesgarden.com/products/ps/c/759/0"
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(link)
        
        # Check if the Cloudflare protection page is present
        if page.query_selector("xpath=/html/body/div[1]/div") is not None:
            wait_for_cloudflare_to_bypass(page)
        
        # Once bypassed, continue with the normal script execution
        print("Continuing with the normal script execution...")
        
        # Example: Wait for a specific element on the page to load
        page.wait_for_selector("table")
        rows = page.query_selector_all("table tr")
        for row in rows:
            cells = row.query_selector_all("td")
            row_data = [cell.text_content().strip() for cell in cells]
            print(row_data)
        
        browser.close()

if __name__ == "__main__":
    main()
