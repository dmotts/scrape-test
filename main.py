from seleniumbase import SB

with SB(uc=True, browser='chrome', headless=False, headed=True) as sb:
    sb.driver.get("https://www.yahoo.com/")