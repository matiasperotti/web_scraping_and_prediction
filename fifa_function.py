

def statistics(name):


    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    import time
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.common.by import By
    import pandas as pd


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
    options.add-argument('--disable-gpu')

    driver = webdriver.Chrome(options=options)
    driver.executable_path = '/usr/bin/chromedriver'

    driver.set_window_size(1920, 1080)


    url = 'https://www.fifaindex.com'

    driver.set_page_load_timeout(15)
    driver.implicitly_wait(2)

    try:
        driver.get(url)

    except:
        pass


    input_field = driver.find_element(By.ID, 'site-search')


    input_field.send_keys(name)

    driver.execute_script("document.getElementById('site-search').click();")
    actions = ActionChains(driver)

    actions.click(input_field).perform()

    time.sleep(5) # idealmente esto es reemplazado con algo que checkea que ya aparecio la lista

    input_field.send_keys(Keys.RETURN)



    elementos_indice = driver.find_elements(By.XPATH, '//*[@class="item"]')
    aa = []

    for elemento in elementos_indice:
        aa.append(elemento.text)



    listapalabras = []


    for elemento in aa:
        if '\n' in elemento:
            palabras = elemento.split('\n')

            listapalabras.append(palabras)



    lista_plana = []

    for sublist in listapalabras:
        lista_plana.extend(sublist)


    if(len(lista_plana) > 20):
            
        #####
        
        anterior = ''
        for i in range(len(lista_plana)):
            if anterior == 'Ball Control':  Ball_Control =      lista_plana[i]
            if anterior == 'Dribbling':     Dribbling =         lista_plana[i]
            if anterior == 'Marking':       Marking =           lista_plana[i]
            if anterior == 'Slide Tackle':  Slide_Tackle =      lista_plana[i]
            if anterior == 'Stand Tackle':  Stand_Tackle =      lista_plana[i]
            if anterior == 'Aggression':    Aggression =        lista_plana[i]
            if anterior == 'Reactions':     Reactions =         lista_plana[i]
            if anterior == 'Att. Position': Att_Position =      lista_plana[i]
            if anterior == 'Interceptions': Interceptions =     lista_plana[i]
            if anterior == 'Vision':        Vision =            lista_plana[i]
            if anterior == 'Short Pass':    Short_Pass =        lista_plana[i]
            if anterior == 'Long Pass':     Long_Pass =         lista_plana[i]
            if anterior == 'Acceleration':  Acceleration =      lista_plana[i]
            if anterior == 'Stamina':       Stamina =           lista_plana[i]
            if anterior == 'Strength':      Strength =          lista_plana[i]
            if anterior == 'Balance':       Balance =           lista_plana[i]
            if anterior == 'Sprint Speed':  Sprint_Speed =      lista_plana[i]
            if anterior == 'Agility':       Agility =           lista_plana[i]
            if anterior == 'Jumping':       Jumping =           lista_plana[i]
            if anterior == 'Heading':       Heading =           lista_plana[i]
            if anterior == 'Shot Power':    Shot_Power =        lista_plana[i]
            if anterior == 'Finishing':     Finishing =         lista_plana[i]
            if anterior == 'Long Shots':    Long_Shots =        lista_plana[i]
            if anterior == 'Curve':         Curve =             lista_plana[i]
            if anterior == 'FK Acc.':       FK_Acc =            lista_plana[i]
            if anterior == 'Penalties':     Penalties =         lista_plana[i]
            if anterior == 'Volleys':       Volleys =           lista_plana[i]
            if anterior == 'GK Positioning':GK_Positioning =    lista_plana[i]
            if anterior == 'GK Diving':     GK_Diving =         lista_plana[i]
            if anterior == 'GK Handling':   GK_Handling =       lista_plana[i]
            if anterior == 'GK Kicking':    GK_Kicking =        lista_plana[i]
            if anterior == 'GK Reflexes':   GK_Reflexes =       lista_plana[i]

            anterior = lista_plana[i]





        elementos_indice = driver.find_elements(By.XPATH, '//*[@class="card-body"]')
        aa = []

        for elemento in elementos_indice:
            aa.append(elemento.text)


        listapalabras = []

        variable_anterior = ''
        for elemento in aa:
            if '\n' in elemento:
                palabras = elemento.split('\n')

                listapalabras.append(palabras)

        lista_plana = []

        for sublist in listapalabras:
            lista_plana.extend(sublist)

        
        import re
        anterior = ''
        for i in range(len(lista_plana)):
            if anterior == 'Height':  Height =      re.findall(r'\d+', lista_plana[i])[0]
            if anterior == 'Weight':  Weight =      re.findall(r'\d+', lista_plana[i])[0]
            if anterior == 'Age':     Age =         re.findall(r'\d+', lista_plana[i])[0]
            anterior = lista_plana[i]


    else:
        Ball_Control, Dribbling, Marking, Slide_Tackle, Stand_Tackle, Aggression, Reactions, Att_Position, Interceptions, Vision, Short_Pass, Long_Pass, Acceleration, Stamina, Strength, Balance, Sprint_Speed, Agility, Jumping, Heading, Shot_Power, Finishing, Long_Shots, Curve, FK_Acc, Penalties, Volleys, GK_Positioning, GK_Diving, GK_Handling, GK_Kicking, GK_Reflexes ,Height, Weight, Age = ['None']*35


    driver.quit()


    if 'Ball_Control'     not in locals(): Ball_Control   = 'None'
    if 'Dribbling'        not in locals(): Dribbling      = 'None'
    if 'Marking'          not in locals(): Marking        = 'None'
    if 'Slide_Tackle'     not in locals(): Slide_Tackle   = 'None'
    if 'Stand_Tackle'     not in locals(): Stand_Tackle   = 'None'
    if 'Aggression'       not in locals(): Aggression     = 'None'
    if 'Reactions'        not in locals(): Reactions      = 'None'
    if 'Att_Position'     not in locals(): Att_Position   = 'None'
    if 'Interceptions'    not in locals(): Interceptions  = 'None'
    if 'Vision'           not in locals(): Vision         = 'None'
    if 'Short_Pass'       not in locals(): Short_Pass     = 'None'
    if 'Long_Pass'        not in locals(): Long_Pass      = 'None'
    if 'Acceleration'     not in locals(): Acceleration   = 'None'
    if 'Stamina'          not in locals(): Stamina        = 'None'
    if 'Strength'         not in locals(): Strength       = 'None'
    if 'Balance'          not in locals(): Balance        = 'None'
    if 'Sprint_Speed'     not in locals(): Sprint_Speed   = 'None'
    if 'Agility'          not in locals(): Agility        = 'None'
    if 'Jumping'          not in locals(): Jumping        = 'None'
    if 'Heading'          not in locals(): Heading        = 'None'
    if 'Shot_Power'       not in locals(): Shot_Power     = 'None'
    if 'Finishing'        not in locals(): Finishing      = 'None'
    if 'Long_Shots'       not in locals(): Long_Shots     = 'None'
    if 'Curve'            not in locals(): Curve          = 'None'
    if 'FK_Acc'           not in locals(): FK_Acc         = 'None'
    if 'Penalties'        not in locals(): Penalties      = 'None'
    if 'Volleys'          not in locals(): Volleys        = 'None'
    if 'GK_Positioning'   not in locals(): GK_Positioning = 'None'
    if 'GK_Diving'        not in locals(): GK_Diving      = 'None'
    if 'GK_Handling'      not in locals(): GK_Handling    = 'None'
    if 'GK_Kicking'       not in locals(): GK_Kicking     = 'None'
    if 'GK_Reflexes'      not in locals(): GK_Reflexes    = 'None'
    if 'Height'           not in locals(): Height         = 'None'
    if 'Weight'           not in locals(): Weight         = 'None'
    if 'Age'              not in locals(): Age            = 'None'
    
    
    return [Ball_Control, Dribbling, Marking, Slide_Tackle, Stand_Tackle, Aggression, Reactions, Att_Position, Interceptions, Vision, Short_Pass, Long_Pass, Acceleration, Stamina, Strength, Balance, Sprint_Speed, Agility, Jumping, Heading, Shot_Power, Finishing, Long_Shots, Curve, FK_Acc, Penalties, Volleys, GK_Positioning, GK_Diving, GK_Handling, GK_Kicking, GK_Reflexes ,Height, Weight, Age]

    
        
    


     
