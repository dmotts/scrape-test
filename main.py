from seleniumbase import SB

with SB(uc=True, headed=True) as sb:
    sb.driver.get("https://www.yahoo.com/")