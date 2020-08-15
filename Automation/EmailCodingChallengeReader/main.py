from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


def waitingClickWithTextInput(delay, xPath, text):
    try:
        siteObject = WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.XPATH, xPath))
        )
        siteObject.send_keys(text)
        siteObject.send_keys(Keys.RETURN)
    except:
        try:
            siteObject = WebDriverWait(driver, delay).until(
                EC.presence_of_element_located((By.XPATH, xPath))
            )
            siteObject.send_keys(text)
            siteObject.send_keys(Keys.RETURN)
        except:
            try:
                siteObject = WebDriverWait(driver, delay).until(
                    EC.presence_of_element_located((By.XPATH, xPath))
                )
                siteObject.send_keys(text)
                siteObject.send_keys(Keys.RETURN)
            except:
                print('failed ' + text)

def waitingClick(delay, xPath):
    try:
        siteObject = WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.XPATH, xPath))
        )
        siteObject.click()
    except:
        try:
            siteObject = WebDriverWait(driver, delay).until(
                EC.presence_of_element_located((By.XPATH, xPath))
            )
            siteObject.click()
        except:
            print('failed click')

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)


action = ActionChains(driver)
driver.get("https://stackoverflow.com/")

SOsignin = driver.find_element_by_xpath('/html/body/header/div/ol[2]/li[2]/a[2]')
SOsignin.click()

GoogleSignin = driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]')
siteObject = driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]')
GoogleSignin.click()

#Gmail mail address 
waitingClickWithTextInput(10,'//*[@id="identifierId"]','email')

#Gmail password obichampatki
waitingClickWithTextInput(20,'//*[@id="password"]/div[1]/div/div[1]/input','pass')

# Open a new window
time.sleep((10))
driver.execute_script("window.open('');")
# Switch to the new window and open URL B
driver.switch_to.window(driver.window_handles[1])
driver.get("http://gmail.com/")

time.sleep(10)
#Opening the email
try:
    unread = driver.find_element_by_class_name('zE')
    action.move_to_element(unread)
    action.click(unread)
    action.perform()
except:
    unread = driver.find_element_by_class_name('zA')
    action.move_to_element(unread)
    action.click(unread)
    action.perform()
    

bodyText = driver.find_element_by_css_selector('body')
codingChallengetext = bodyText.text
#print(bodyText.text)
startIndex = codingChallengetext.find('Good morning!')
endIndex = codingChallengetext.find('Upgrade to premium')
print(codingChallengetext[startIndex:endIndex])

if startIndex != -1:
    f = open("DailyCoding.txt")
    f.write(codingChallengetext[startIndex:endIndex])
    f.close()

time.sleep(10)
driver.quit()