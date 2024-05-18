from seleniumbase import SB

with SB(uc=True, demo=True) as sb:
    sb.open("https://www.google.com/")
    sb.type("#lst-ib", "test")
    sb.click("input[type='submit']")
    sb.click("div[class='r']")

    