from seleniumbase import Driver

driver = Driver(uc=True, browser='chrome', headless=False)
url = "https://gitlab.com/users/sign_in"
try: 
    driver.uc_open_with_reconnect(url, 3)
    driver.sleep(10)
finally:
    driver.quit()