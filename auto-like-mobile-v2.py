from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from myid import ID, PW
import time, os

from dotenv import load_dotenv
from ppadb.client import Client as AdbClient

load_dotenv()

# Pixel 2 API 30 / 1080 x 1920: 420dpi / Android 11.0
serial = "emulator-5554"

# adb shell getevent -il /dev/input/event2 | grep ABS_MT_POSITION
max_x = max_y = 32767
# adb shell wm size
act_x = 1080
act_y = 1920

client = AdbClient(host="127.0.0.1", port=5037)
adb_device = client.device(serial)

# open instagram application
adb_device.shell("am start -a android.intent.action.MAIN -n com.instagram.android/com.instagram.mainactivity.MainActivity")
time.sleep(3)

''' first login (with ID/PW)
adb_device.shell("input touchscreen tap %d %d" % (0x40b5*act_x/max_x, 0x4a00*act_y/max_y))
time.sleep(1)

adb_device.shell("input touchscreen tap %d %d" % (0x1fa4*act_x/max_x, 0x31ee*act_y/max_y))
adb_device.shell("input text '%s\n'" % ID)
adb_device.shell("input touchscreen tap %d %d" % (0x1eee*act_x/max_x, 0x2c43*act_y/max_y))
adb_device.shell("input text '%s\n'" % PW)

time.sleep(3)
'''

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
feedCtn = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[4]/div/a[1]/div/div/div[2]/span/span').text
search.send_keys(Keys.ENTER)

time.sleep(5)

# go first feed
feed = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div/div/div/a')
feed.send_keys(Keys.ENTER)

time.sleep(2)

i = 0
while i < 500:
    # open instagram application with url
    adb_device.shell("am start -a android.intent.action.VIEW -d %s" % driver.current_url)
    time.sleep(2)

    # like macro
    adb_device.shell("input touchscreen tap %d %d" % (0x4b23*act_x/max_x, 0x1333*act_y/max_y))
    time.sleep(0.1)
    adb_device.shell("input touchscreen tap %d %d" % (0x63ca*act_x/max_x, 0x4aee*act_y/max_y))
    time.sleep(1.5)
    adb_device.shell("input touchscreen tap %d %d" % (0x3bd9*act_x/max_x, 0x43bb*act_y/max_y))

    print('%d like' % (i+1))
    i += 1
    
    # get next feed
    feed = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/a[2]')
    ac = ActionChains(driver)
    ac.move_to_element(feed)
    ac.click()
    ac.perform()
    time.sleep(1)
    

print('total like : %d' % i)
