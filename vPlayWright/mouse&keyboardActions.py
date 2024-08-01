from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser=playwright.chromium.launch(headless=False, slow_mo=5000) 
    #headless is for LIVE gui execution, slow_mo for each line execution delay time
    page=browser.new_page()
    url="https://bootswatch.com/default/"
    page.goto(url)
    #click()
    page.get_by_role("button", name="Block button").first.click()
    #doubleclick
    page.get_by_role("button", name="Block button").first.dblclick(delay=500)
    #defaultCLICK-mouse left button)
    page.get_by_role("button", name="Block button").first.click(button="right")
    page.get_by_role("button", name="Block button").first.click(modifiers=["Shift"])
    page.get_by_role("button", name="Block button").first.click(modifiers=["Shift", "Control"])
    page.get_by_role("button", name="Block button").first.hover()
    #inputActions
    input=page.get_by_label("Email address").first
    #or
    input=page.get_by_placeholder("Enter email")
    input.fill("example@email.com")
    input.clear()
    input.type("example123@email.com", delay=200)
    enteredvalue=input.input_value()
    print(enteredvalue)