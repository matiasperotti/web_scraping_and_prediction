
def get_info(url):
    from selenium import webdriver

    driver = webdriver.Chrome()

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

    # hace falta una funcion que se fije si el partido fue suspendido
    #########################3
    # y arreglar la funcion de fifa para que no se rompa si no tiene resultados

    spans = driver.find_elements_by_css_selector("span.MatchLineupFormation_playerNameText__39DAI")


    first_team = return_names()

    import time
    time.sleep(5)


    try:
        boton = driver.find_element_by_id('onetrust-accept-btn-handler')#cookies button
        boton.click()
    except:
        pass

    import time
    time.sleep(3)

    ####
    p = driver.find_element_by_xpath("//p[contains(@class, 'MatchScore_scores__UWw03 title-2-bold')]")

    spans = p.find_elements_by_tag_name("span")

    points = []
    for span in spans:
        text = span.text
        if text.isdigit():
            points.append(int(text))
    ###


    boton = driver.find_element_by_xpath("//button[contains(@class, 'title-7-medium ToggleButton_button__d5K77')]")

    boton.click()


    spans = driver.find_elements_by_css_selector("span.MatchLineupFormation_playerNameText__39DAI")


    second_team = return_names()

    driver.quit()

    return points, first_team, second_team