from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser=playwright.chromium.launch(headless=False, slow_mo=500) 
    #headless is for LIVE gui execution, slow_mo for each line execution delay time
    page=browser.new_page()
    url="https://bootswatch.com/default/"
    page.goto(url)
    #selecting radio and checkbox
    checkbox=page.get_by_label("Default checkbox")
    checkbox.check()
    if checkbox.is_checked():
        checkbox.uncheck()
    #select opt/opts
    select=page.get_by_label("Example select")
    select.select_option("4")
    multi_select=page.get_by_label("Example multiple select")
    # multi_select.select_option('1','4')

    #dropdown
    dropdown=page.locator("//button[@class='btn btn-primary dropdown-toggle']")
    dropdown.click()
    page.locator("/html/body/div[2]/div[3]/div[2]/div[1]/div[1]/div[1]/div/div/a[2]")
    #upload files
    file_input=page.get_by_label("Default file input example")
    file_input.set_input_files("rffrh.py")
    page.pause()



