from seleniumbase import Driver

driver = Driver(uc=True, browser='chrome', headless=False)
url = "https://google.com/"
try: 
    driver.open(url)
    print(f"Opened {url}")
    driver.sleep(100)
finally:
    driver.quit()