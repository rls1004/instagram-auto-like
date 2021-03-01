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

# Searches for posts that contain at least one tag belonging to tag2
# among the search results of tag1
tag1 = "고양이"
tag2 = ["좋반", "좋아요반사"]

# search tag1
driver.get('https://instagram.com/explore/tags/'+tag1)

time.sleep(5)

# get first feed
feed = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div/div/div/a')
feed.send_keys(Keys.ENTER)

time.sleep(5)

i = 0
while True:
    # variable that detemines whether you like or pass
    do_like = False

    # check if any of the tags belonging to tag2 are included
    for multi_tag in tag2:
        try:
            tag = driver.find_element_by_xpath('//*[@href="/explore/tags/%s/"]' % multi_tag)
            do_like = True
            break
        except:
            pass

    # posts with too many likes are passed.
    if do_like:
        try:
            num_of_like = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/artical/div[3]/section[2]/div/div/button/span').text
            num_of_like = int(num_of_like)
            if num_of_like > 100:
                do_like = False
                print('post with %d likes is passed.' % num_of_like)
        except:
            pass

    # only like posts that you haven't liked yet
    if do_like:
        like = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section/span/button')
        try:
            alt = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[2]/div[1]/div[1]/div[2]/div/div/div/ul/li[2]/div/div/div/div[1]/div/img').get_attribute("alt")
        except:
            try:
                alt = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[2]/div[1]/div[1]/div[1]/img').get_attribute("alt")
            except:
                alt = "video?"
        try:
            likeBtn = driver.find_element_by_xpath('//*[@aria-label="좋아요"]')
        except:
            break

        if "소액" not in alt and "수익" not in alt and "대출" not in alt and "재테크" not in alt and "투자" not in alt and "유머" not in alt:
            like.send_keys(Keys.ENTER)
            print('%d like' % (i+1))
            i += 1
            if i >= 100:
                break
        time.sleep(1.5)

    # get next feed
    nextFeed = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/a[2]')
    ac = ActionChains(driver)
    ac.move_to_element(nextFeed)
    ac.click()
    ac.perform()
    time.sleep(2.5)

print('total like : %d' % i)