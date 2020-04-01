
from selenium import webdriver
import time
username='username'
password='password'
browse=webdriver.Chrome(r'chromedriver.exe')
browse.get('http://10.10.0.1/24online/webpages/client.jsp')
count=0

####This loop keeps goind until you login
while 1:
    
    try:
        #####Check the "Agreepolicy"
        browse.find_element_by_css_selector('#agreepolicy').click()
        
        #####Finds the username entry and sends "Username" to it
        browse.find_element_by_xpath(("/html/body/form/div/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/input")).send_keys(username)

        #####Finds the password entry and sends "password" to it
        browse.find_element_by_xpath('//*[@id="jsena"]/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[3]/td[2]/input').send_keys(password)
        
        #####Clicks the login Button
        browse.find_element_by_css_selector('#loginbtn').click()
    
    except :
        #####If already logged in or unavailability of internet, the selenium throws an error caught by this block
        exit()
    




