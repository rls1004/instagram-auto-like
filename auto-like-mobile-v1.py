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

# search
tag = "#whgqks"     # keyboard setting require
adb_device.shell("input touchscreen tap %d %d" % (0x2591*act_x/max_x, 0x72a9*act_y/max_y))
adb_device.shell("input touchscreen tap %d %d" % (0x2591*act_x/max_x, 0x977*act_y/max_y))
time.sleep(1)
adb_device.shell("input touchscreen tap %d %d" % (0x2591*act_x/max_x, 0x977*act_y/max_y))
time.sleep(2)
print("input text '%s'" % tag)
adb_device.shell("input text '%s'" % tag)

adb_device.shell("input touchscreen tap %d %d" % (0x2591*act_x/max_x, 0x1bdd*act_y/max_y))  # go to result
adb_device.shell("input touchscreen tap %d %d" % (0x5a12*act_x/max_x, 0x27bb*act_y/max_y))  # latest post
adb_device.shell("input touchscreen tap %d %d" % (0x1d45*act_x/max_x, 0x3988*act_y/max_y))  # first feed

i = 0
while i < 500:
    time.sleep(2)

    # like macro (with play store application)
    adb_device.shell("input touchscreen tap %d %d" % (0x4b23*act_x/max_x, 0x1333*act_y/max_y))
    time.sleep(0.1)
    adb_device.shell("input touchscreen tap %d %d" % (0x63ca*act_x/max_x, 0x4aee*act_y/max_y))
    time.sleep(1.5)
    adb_device.shell("input touchscreen tap %d %d" % (0x3bd9*act_x/max_x, 0x43bb*act_y/max_y))

    print('%d like' % (i+1))
    i += 1

    # refresh for new feed
    like_x = 0x3c8f*act_x/max_x
    like_y = 0x1d66*act_y/max_y
    like_y2 = 0x4510*act_y/max_y
    adb_device.shell("input swipe %d %d %d %d %d" % (like_x, like_y, like_x, like_y2, 200))
    

print('total like : %d' % i)
