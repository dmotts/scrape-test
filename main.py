from seleniumbase import Driver

driver = Driver(uc=True)
url = "https://gitlab.com/users/sign_in"
driver.uc_open_with_reconnect(url, 3)
driver.sleep(10)
driver.quit()