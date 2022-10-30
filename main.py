import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

with  open("cred.txt","r") as f:
    cred = f.read()
with  open("recv.txt","r") as f:
    recv = f.read()
credarr = cred.split("\n")
name = credarr[0];
passwd = credarr[1];
recv_list = recv.split("\n")
subject = "Subject"


if (sys.argv[1] == "firefox"):	
	from selenium.webdriver.firefox.options import Options as FFOptions
	options = FFOptions()
	driver = webdriver.Firefox(options=options)
else:
	from selenium.webdriver.chrome.service import Service as ChromeService
	from webdriver_manager.chrome import ChromeDriverManager
	driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))

driver.implicitly_wait(20)

driver.get("https://nwm.iitk.ac.in/")

driver.find_element(by = By.ID , value="rcmloginuser").send_keys(name)
driver.find_element(by = By.ID , value="rcmloginpwd").send_keys(passwd)
driver.find_element(by = By.ID , value="rcmloginsubmit").click()
for to in recv_list :
    driver.find_element(by = By.ID , value="rcmbtn109").click()
    sleep(1)
    driver.find_element(by = By.CSS_SELECTOR , value = "#compose_to > div > div > ul > li > input").send_keys(to)
    sleep(1)
    driver.find_element(by = By.ID, value = "compose-subject").send_keys(subject)
    sleep(1)
    iframe = driver.find_element(by = By.ID, value = "composebody_ifr")
    driver.switch_to.frame(iframe)
    driver.find_element(by = By.CSS_SELECTOR, value = "#tinymce > p").send_keys ("Hello Guys")
    sleep(1)
    driver.switch_to.default_content()
    driver.find_element(by = By.ID , value = "rcmbtn115" ).click()
    sleep(6)
driver.quit()
