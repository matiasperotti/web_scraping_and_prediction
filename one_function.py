

def matches(date):
        
    from selenium.webdriver.chrome.options import Options
    from selenium import webdriver
    import selenium


    adblock = '/home/user/Desktop/futbol/Adblock-Plusfree-ad-blocker.crx'



    options = Options()
    options.add_extension(adblock)


    options.headless = False#original con True

    chrome_options = webdriver.ChromeOptions()

    chrome_options.add_argument('--blink-settings=imagesEnabled=false')

    chrome_options.add_experimental_option(
        "prefs", {"profile.managed_default_content_settings.images": 2}
    )

    driver = webdriver.Chrome(options=options, chrome_options=chrome_options, executable_path='/usr/bin/chromedriver')


    if(date == ''):
        driver.get('https://onefootball.com/es/partidos/yesterday')

    else:

        driver.get('https://onefootball.com/es/partidos?date='+date) # format 2-03-27

    clase = 'MatchCard_matchCard__JSuaw'

    elementos = driver.find_elements_by_css_selector('.' + clase)

    hrefs = []
    for elemento in elementos:
        href = elemento.get_attribute('href')
        hrefs.append(href)

    driver.quit()

    return hrefs
