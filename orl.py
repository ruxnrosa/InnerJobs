import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# ABRINDO O ARQUIVO CVS PARA IMPUTAR OS DADOS
with open('inner.csv', 'w') as file:
    file.write("Empreendimento; Localização; Valor; ValorM2 \n")

# DEFINIÇÕES DO NAVEGADOR
driver = webdriver.Firefox()
driver.get('https://www.orulo.com.br/buildings?map_address=Rio+de+Janeiro%2C+Rio+de+Janeiro&map_sw_lat=-23.07652&map_sw_lng=-43.79635&map_ne_lat=-22.74618&map_ne_lng=-43.1019')
# driver.maximize_window()
time.sleep(15)
# cookie = driver.find_element_by_id(
#     'CybotCookiebotDialogBodyLevelButtonCustomize')
# try:
#     cookie.click()
# except:
#     pass

# IDENTIFICANDO OS OBJETOS NA PÁGINA
for w in range(48):
    empreendimento = driver.find_elements(
        By.XPATH, '//*/fieldset/div/div[2]/div/div[1]/b')
    localizacao = driver.find_elements(
        By.XPATH, '//*/fieldset/div/div[2]/div/div[1]/p')
    preco = driver.find_elements(
        By.XPATH, '//*/fieldset/div/div[2]/div/div[2]/div[2]/div/b[2]')
    precom2 = driver.find_elements(
        By.XPATH, '//*/fieldset/div/div[2]/div/div[2]/div[2]/div/b[3]')

    with open('inner.csv', 'a') as file:
        for i in range(len(empreendimento)):
            file.write(empreendimento[i].text + ";" + localizacao[i].text +
                       ";" + preco[i].text + ";" + precom2[i].text + "\n")

        next = driver.find_element(By.CLASS_NAME, 'next-page-button')
        next.click()
        time.sleep(15)
    file.close()
driver.close()
