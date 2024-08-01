from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser=playwright.chromium.launch(headless=False, slow_mo=5000) 
    #headless is for LIVE gui execution, slow_mo for each line execution delay time
    page=browser.new_page()
    url="https://bootswatch.com/default/"
    page.goto(url)
    webtitle=page.locator("xpath=/html/head/title")
    print(webtitle)
    page.locator("xpath=//h1").highlight()
    page.locator("//h1[@id='navbars']").highlight() #xpath variable is optional
    page.locator("//input[@readonly]").highlight()
    page.locator("//*[@value='wrong value']").highlight()
    #text()
    page.locator("//h1[text(),'Heading 1']")
    #contains()
    page.locator("//h1[contains(text(),'Head')]").highlight()
    page.locator("//button[contains(@class,'btn-outline-primaary')]").highlight()






