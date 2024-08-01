from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser=playwright.chromium.launch(headless=False, slow_mo=5000) 
    #headless is for LIVE gui execution, slow_mo for each line execution delay time
    page=browser.new_page()
    url="https://bootswatch.com/default/"
    page.goto(url)
    #get_by_role
    #docs_button=page.get_by_role("link", name="Docs").click()
    button=page.get_by_role("button", name="Default button").click()
    checkbox=page.get_by_role("checkbox", name="Default checkbox").check()
    radio_button=page.get_by_role("radio", name="Option two can be something else and selecting it will deselect option one")
    radio_button.click()
    radio_button.highlight()
    #input field by label
    email_input=page.get_by_label("Email address")
    email_input.highlight()
    page.get_by_label("password").highlight()
    page.get_by_label("Example textarea").highlight()
    #input field by placeholder
    page.get_by_placeholder("Enter email").highlight()
    #text locator
    page.get_by_text("Middle").click()
    page.get_by_text("fine print", exact=True).highlight()
    #Alt txt locator(to locate images)
    url1="https://unsplash.com/"
    page1=browser.new_page()
    page1.goto(url1)
    page1.get_by_alt_text("a wooden table topped with plates and cups").highlight()
    print("url:", page1.url)
    #xpath
    
    browser.close()