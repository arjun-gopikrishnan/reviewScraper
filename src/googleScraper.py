from selenium import webdriver
from config import PATH


def googleScraper(movieName):
    driver = webdriver.Chrome(PATH)
    movieName=movieName.replace(" ","+")
    driver.maximize_window() 
    url = "https://www.google.com/search?q="+movieName+"+movie"
    driver.get(url)
    button = driver.find_element_by_xpath("//*[contains(text(),'More audience reviews (')]")
    button.click()
    driver.quit()
    



