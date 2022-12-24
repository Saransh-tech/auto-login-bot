from selenium import webdriver
import os

def startBot(username, password, url):
    path = "C:\\Users\\hp\\Downloads\\chromedriver"

    driver = webdriver.Chrome(path)

    driver.get(url)

    driver.find_element_by_name(
        "id/class/name of username").send_keys(username)

    driver.find_element_by_name(
        "id/class/name of password").send_keys(password)

    driver.find_element_by_css_selector(
        "id/class/name/css selector of login button").click()
username = "enter your Username"
password = "Enter your password"

url = "https://www.youtube.com/"
startBot(username, password, url)

