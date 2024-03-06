import time
import random

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://portal.svkm.ac.in/usermgmt/login')
browser.maximize_window()

sapid=browser.find_element("id","userName").send_keys("") # Enter your SAP ID
password=browser.find_element("id","userPwd").send_keys("") # Enter your Password
login=browser.find_element("id","userLogin").click()
time.sleep(20)
browser.get("https://portal.svkm.ac.in/MPSTME-NM-M/giveStudentFeedback?feedbackId=2133") # Insert the URL of the feedback form
time.sleep(5)

for j in range(13): # This will change on the basis of the number of pages
    for i in range(0,14): # This will change on the basis of the number of faculty
        id=f"answer{j}"+str(i)
        print(id)
        rando=random.randint(4,7)
        try:
            sel =(browser.find_element(By.ID, id))
            sel.send_keys(rando)
        except:
            print("It is not present,skipping to next")

    buttons=browser.find_elements(By.TAG_NAME, 'button')
    for button in buttons:
        if 'Submit' in button.text or "Finish" in button.text :
            button.click()
            break
    time.sleep(5)
    print(f"{j} Page Done")

print("All Done, Exiting in 10 seconds")
time.sleep(10)