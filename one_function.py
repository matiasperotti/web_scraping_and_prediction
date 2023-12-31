

def matches(date):
        
    from selenium.webdriver.chrome.options import Options
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import selenium

    adblock = './Adblock-Plusfree-ad-blocker.crx'

    #options = Options()
    
    options = webdriver.ChromeOptions()

    options.add_argument('--blink-settings=imagesEnabled=false')
    options.add_argument('--headless')
    options.add_experimental_option(
        "prefs", {"profile.managed_default_content_settings.images": 2}
    )
    #options.binary_location = '/usr/bin/google-chrome-stable'
    options.add_argument('--display=99')
    #options.add_extension(adblock)
    options.add_argument('--no-sandbox')
    options.add_argument('--user-data-dir= /home/ubuntu/user-data-dir')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    
    driver = webdriver.Chrome(options=options)
    driver.executable_path = '/usr/bin/chromedriver'


    if(date == ''):
        driver.get('https://onefootball.com/es/partidos')

    else:

        driver.get('https://onefootball.com/es/partidos?date='+date) # format 2-03-27

    #clase = 'MatchCard_matchCard__JSuaw'
    #clase = 'MatchCard_matchCard__iOv4G'

    import time
    time.sleep(10)


    #elementos = driver.find_elements_by_css_selector('.' + clase)
    #elementos = driver.find_elements(By.CSS_SELECTOR, '.' + clase)
    #elementos = driver.find_elements(By.CSS_SELECTOR, 'a.MatchCard_matchCard__iOv4G')  ##
    #elementos = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a.MatchCard_matchCard__iOv4G')))

    xpath = f"//a[contains(@href, 'partido/')]"
    links = driver.find_elements("xpath", xpath)
    lista_links = [link.get_attribute("href") for link in links]

    """
    hrefs = []
    for elemento in elementos:
        href = elemento.get_attribute('href')
        hrefs.append(href)

    driver.quit()

    #print('date', date)
    #print('hrefs', hrefs)
    #print('elementos', elementos)

    return hrefs
    """

    return lista_links