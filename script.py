from selenium import webdriver
import os

def startBot(username, password, url):
    path = "" # Give the path to the installed chromedriver here

    driver = webdriver.Chrome(path)