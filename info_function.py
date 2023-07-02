
def get_info(url):
    from selenium.webdriver.chrome.options import Options
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import time

    adblock = '/Adblock-Plusfree-ad-blocker.crx'

    #options = Options()

    options = webdriver.ChromeOptions()

    options.add_argument('--blink-settings=imagesEnabled=false')
    options.add_argument('--headless')
    #options.binary_location = '/usr/bin/google_chrome-stable'
    options.add_argument('--display=99')
    options.add_argument('--no-sandbox')
    options.add_argument('--user-data-dir= /home/ubuntu/user-data-dir')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--desable-gpu')

    driver = webdriver.Chrome(options=options)
    driver.executable_path = '/usr/bin/chromedriver'

    driver.get(url)


    def clean_names(input_text):
        for i, char in enumerate(input_text):
            if char.isalpha():
                return input_text[i:]
        return ''

    def return_names():

        names = []
        for span in spans:
            names.append(clean_names(span.text))

        return names


    #spans = driver.find_elements_by_css_selector("span.MatchLineupFormation_playerNameText__39DAI")
    spans = driver.find_elements(By.CSS_SELECTOR, "span.MatchLineupFormation_playerNameText__39DAI")
    first_team = return_names()
    
    if(len(first_team) == 0):
        flag = 1
        
    else:
        flag = 0
        

    if(flag == 1):
        #spans = driver.find_elements_by_xpath("//a[contains(@class, 'title-7-medium MatchLineupFlat_playerName__igpy2')]")
        spans = driver.find_elements(By.XPATH, "a[contains(@class, 'title-7-medium MatchLineupFlat_playerName__igpy2')]")
        first_team = return_names()
        

    time.sleep(7)
    try:
        #boton = driver.find_element_by_id('onetrust-accept-btn-handler')#cookies button
        boton = driver.find_element(By.ID, "onetrust-accept-btn-handler")
        boton.click()
        
    except:
        pass
    time.sleep(3)

    
    try:
        #p = driver.find_element_by_xpath("//p[contains(@class, 'MatchScore_scores__UWw03 title-2-bold')]")
        p = driver.find_element(By.XPATH, "//p[contains(@class, 'MatchScore_scores__UWw03 title-2-bold')]")
        
        #spans = p.find_elements_by_tag_name("span")
        spans = p.find_elements(By.TAG_NAME, "span")
        
        points = []
        for span in spans:
            text = span.text
            if text.isdigit():
                points.append(int(text))
        ###


        try:
            #boton = driver.find_element_by_xpath("//button[contains(@class, 'title-7-medium ToggleButton_button__d5K77')]")
            
            boton = driver.find_element(By.XPATH, "//button[contains(@class, 'title-7-medium ToggleButton_button__d5K77')]")
            
            boton.click()


            if(flag == 0):
                #spans = driver.find_elements_by_css_selector("span.MatchLineupFormation_playerNameText__39DAI")
                spans = driver.find_elements(By.CSS_SELECTOR, "span.MatchLineupFormation_playerNameText__39DAI")
                second_team = return_names()
                
            elif(flag == 1):
                #spans = driver.find_elements_by_xpath("//a[contains(@class, 'title-7-medium MatchLineupFlat_playerName__igpy2')]")
                spans = driver.find_elements(By.XPATH, "//a[contains(@class, 'title-7-medium MatchLineupFlat_playerName__igpy2')]")
                second_team = return_names()
                

        except:
            points = first_team = second_team = []
            
    except:
        points = first_team = second_team = []


    driver.quit()
    
    return points, first_team, second_team


    # hay que probar usar los nombres alternativos que tiene onefootball pero que no muestra
