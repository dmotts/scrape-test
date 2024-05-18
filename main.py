from seleniumbase import Driver

driver = Driver(uc=True, browser='chrome', headless=False)
url = "https://gitlab.com/users/sign_in"
try: 
    driver.uc_open(url)
    print(f"Opened {url}")
    driver.sleep(1000)
finally:
    driver.quit()