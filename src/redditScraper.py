from selenium import webdriver
from config import PATH

def discussionLinks(search_results):
    links=[]
    
    for search_result in search_results:
        if ("https://www.reddit.com" in search_result.get_attribute("href")) and ("https://www.google.com" not in search_result.get_attribute("href")):
           links.append(search_result.get_attribute("href"))

    return links

def redditScraper(movie):
    
    movie = movie.replace(" ","+")
    driver = webdriver.Chrome(PATH)    
    url = "https://www.google.com/search?q="+movie+"+reddit+discussion"
    
    driver.get(url)
    
    search_results = driver.find_elements_by_xpath("//a[@href]")
    linksArray=discussionLinks(search_results)
    
    for link in linksArray:
        print(link)
    
    driver.quit()
        