from seleniumbase import SB

with SB(uc=True, browser='firefox', headless=False, headed=True) as sb:
    sb.driver.get("https://www.yahoo.com/")