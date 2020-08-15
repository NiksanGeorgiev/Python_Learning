from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get('https://www.imdb.com')

TITILE = 'Work It'
YEAR = '2020'

try:
    siteObject = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "suggestion-search")))
    siteObject.send_keys(TITILE)
    siteObject.send_keys(Keys.RETURN)
except:
    print("search failed")

try:
    siteObject = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, TITILE)))
    siteObject.click()
except:
    print("failed")

sleep(10)

#Print runtime and release date
titleDetails = driver.find_elements_by_id("titleDetails")
for element in titleDetails:
    elText = element.text
    if "Release Date" in elText:
        startIndex = elText.find("Release Date")
        endindex = elText.find(" See more »")
        print(elText[startIndex:endindex])
    if "Runtime" in elText:
        startIndex = elText.find("Runtime:")
        endindex = elText.find(" min")
        print(elText[startIndex:endindex+4])

plotSummary = driver.find_elements_by_class_name('plot_summary')
for element in plotSummary:
    elText = element.text
    if "Director" in elText:
        startIndex = elText.find("Director")
        endindex = elText.find("Writer")
        print(elText[startIndex:endindex])

titleCast = driver.find_elements_by_id('titleCast')
characters = driver.find_elements_by_class_name('character')
for i in range(len(characters)):
    actors = driver.find_element_by_xpath('//*[@id="titleCast"]/table/tbody/tr[' + str(i+2) + ']/td[2]/a')
    actorName = actors.text
    characterName = characters[i].text
    print(actorName + ' - ' + characterName)

sleep(10)
driver.quit()
