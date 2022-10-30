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

driver.get("https://webmail.iitk.ac.in/squirrelmail/src/login.php")

captcha = driver.find_element(by = By.CSS_SELECTOR, "table center img")
captcha.save_screenshot("captcha.png")