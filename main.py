from seleniumbase import SB

with SB(uc=True, headless=False) as sb:
    sb.driver.get("https://www.yahoo.com/")