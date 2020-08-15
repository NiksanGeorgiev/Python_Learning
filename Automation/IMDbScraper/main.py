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
action = ActionChains(driver)

TITILE = input("Type in a title of a movie or Tv series: ")
movie = True
seasons = 0

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
    print("Something went wrong. See if you spelled correctly the titile")
    driver.quit()

sleep(5)
#driver.execute_script("window.scrollTo(0,1000)")
#Series check
episodes = driver.find_element_by_class_name('article')
if "Episodes" in episodes.text:
    movie = False
    try:
        siteObject = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="title-episode-widget"]/div/div[3]/a[1]')))
        seasons = int(siteObject.text)
    except:
        print('error')

if movie:
    print('Movie')
else:
    print('Tv Series')

#Rating
rating = driver.find_element_by_class_name('ratingValue')
print('Rating: ' + rating.text)

#Release date
titleDetails = driver.find_elements_by_id("titleDetails")
for element in titleDetails:
    elText = element.text
    if "Release Date" in elText:
        startIndex = elText.find("Release Date")
        endindex = elText.find(" See more »")
        print(elText[startIndex:endindex])


#Direcetor
plotSummary = driver.find_elements_by_class_name('plot_summary')
for element in plotSummary:
    elText = element.text
    if "Director" in elText:
        startIndex = elText.find("Director")
        endindex = elText.find("Writer")
        print(elText[startIndex:endindex])

#Genres
titleStoryLine = driver.find_elements_by_id("titleStoryLine")
for element in titleStoryLine:
    elText = element.text
    if "Genres" in elText:
        startIndex = elText.find("Genres")
        endindex = elText.find("Certificate")
        print(elText[startIndex:endindex])

#Cast
print()
try:
    titleCast = driver.find_elements_by_id('titleCast')
    characters = driver.find_elements_by_class_name('character')
    print("Cast:")
    z = 2
    for i in range(len(characters)):
        if movie:
            actors = driver.find_element_by_xpath('//*[@id="titleCast"]/table/tbody/tr[' + str(i+2) + ']/td[2]/a') 
        else:
            actors = driver.find_element_by_xpath('//*[@id="titleCast"]/table/tbody/tr[' + str(z) + ']/td[2]/a')
        
        actorName = actors.text
        characterName = characters[i].text.split('\n')[0]
        print(actorName +' - ' + characterName)
        z+=2
except:
    print()

#Seasons count
if not movie:
    print('Seasons: ' + str(seasons))

#Runtime
print()
titleDetails = driver.find_elements_by_id("titleDetails")
for element in titleDetails:
    elText = element.text
    if "Runtime" in elText:
        startIndex = elText.find("Runtime")
        endindex = elText.find(" min")
        if movie:
            print(elText[startIndex:endindex+4])
        else:
            print('Runtime for an episode:'+ elText[startIndex+7:endindex+4]) 

#Storyline
print()
print('Storyline:')
storyline = driver.find_element_by_xpath('//*[@id="titleStoryLine"]/div[1]/p/span')
print(storyline.text)

#Trailer link
print()
try:
    siteObject = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,'//*[@class = "slate"]/a')))
    action.move_to_element(siteObject)
    action.click(siteObject)
    action.perform()
    sleep(10)
    print('Link for the trailer: ' + driver.current_url)
    sleep(5)
except:
    print("Trailer link error ")
    
print()
print("Thanks for using my program!")
print()

driver.quit()
