from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from myid import ID, PW
import time

# connect
driver = webdriver.Chrome('./chromedriver')
driver.get('https://instagram.com')

time.sleep(2)

# login
login_id = driver.find_element_by_name('username')
login_id.send_keys(ID)
login_pw = driver.find_element_by_name('password')
login_pw.send_keys(PW)
login_pw.send_keys(Keys.RETURN)

time.sleep(4)

# search tag
search = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
search.send_keys('#좋반')
time.sleep(2)
search = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[4]/div/a[1]')
search.send_keys(Keys.ENTER)

time.sleep(5)

# get first feed
feed = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div/div/div/a')
feed.send_keys(Keys.ENTER)

time.sleep(2)

i = 0
while True:
    # get the like button
    like = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section/span/button')
    
    # check if like has already been hit
    try:
        likeBtn = driver.find_element_by_xpath('//*[@aria-label="좋아요"]')
    except:
        break

    # hit the like
    like.send_keys(Keys.ENTER)
    print('%d like' % (i+1))
    i += 1
    time.sleep(1.5)

    # get next feed
    nextFeed = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/a[2]')
    ac = ActionChains(driver)
    ac.move_to_element(nextFeed)
    ac.click()
    ac.perform()
    time.sleep(1.5)

print('total likes : %d' % i)
