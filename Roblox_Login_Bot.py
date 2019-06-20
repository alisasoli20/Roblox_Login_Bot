import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import re
from selenium.common.exceptions import NoSuchElementException
from urllib import request
 
# ====== CONF ======

username = "YOUR_EMAIL"
password= "YOUR_PASSWORD"

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome('C:\Python\chromedriver.exe',options=options)
driver.get('https://www.roblox.com/login')

username_box = driver.find_element_by_name('username')
username_box.clear()
username_box.send_keys( username )

password_box = driver.find_element_by_name('password')
password_box.clear()
password_box.send_keys( password )

password_box.send_keys(Keys.RETURN)

time.sleep(15)

if not os.path.exists('images'):
    os.makedirs('images')

i=1
while True:    
    if( "Hello, {}!".format(username) not in driver.page_source ):
        driver.get('https://www.roblox.com/home?nl=true')
    try:
        home_ad_left = driver.find_element_by_name('Roblox_MyHome_Left_160x600')

        driver.switch_to.frame(home_ad_left)

        elem = driver.find_element_by_xpath("/html/body/a/img")
        src = elem.get_attribute('src')
        
        request.urlretrieve(src,'images/Roblox_MyHome_Left_'+str(i)+'_160x600.png')
        print("SOURCE Left = " + src)

        driver.get('https://www.roblox.com/home?nl=true')
        home_ad_right = driver.find_element_by_name('Roblox_MyHome_Right_160x600')
        driver.switch_to.frame(home_ad_right)
        elem = driver.find_element_by_xpath("/html/body/a/img")
        src = elem.get_attribute('src')    
        request.urlretrieve(src,'images/Roblox_MyHome_Right_'+str(i)+'_160x600.png')
        print("SOURCE Right = " + src)
    except NoSuchElementException:  #spelling error making this code not work as expected
        print("MASLAA")
    pass

    driver.get('https://www.roblox.com/users/1113446630/profile')

    try:
        profile_ad = driver.find_element_by_name('Roblox_Profile_Top_728x90')

        driver.switch_to.frame(profile_ad)

        elem = driver.find_element_by_xpath("/html/body/a/img")
        src = elem.get_attribute('src')
        request.urlretrieve(src,'images/Roblox_Profile_Top_'+str(i)+'_728x90.png')
        print("SOURCE profile = " + src)
    except NoSuchElementException:
        print("MASLAA")
    pass

    driver.get('https://www.roblox.com/user-sponsorship/3')

    try:
        elem = driver.find_element_by_xpath("html/body/a/img")
        src = elem.get_attribute('src')
        request.urlretrieve(src,'images/Roblox_User_Sponsorship'+str(i)+'_300x250.png')
        print("SOURCE user = " + src)
    except NoSuchElementException:
        print("MASLAA")
    pass
    i+=1
