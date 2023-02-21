# Project-2-Flights-Ticket-Price-Analysis

Project idea: Project Idea: For this project, you can pick a website like Expedia or Kayak, fill in your details using automated fashion, and then crawl the website to extract the price information.
https://www.projectpro.io/article/web-scraping-projects-ideas/475


# Part 1: How to Install selenium and Use ChromeDriver

1. getting the Selenium Library : pip install selenium 
2. import webdriver from selenium : atuomating opening a web browser 
3. driver = webdriver.Chrome()
4. we will use Chrome so we need to get chrome driver 
5. To get your chrome driver 
    - get your chrome version : chrome://version/
    - got to https://chromedriver.storage.googleapis.com/index.html and find your chrome version 
    - download the zip file 
    - extract the zip file 
    - Save it somewhere in your computer 
6. import os to access the driver in a code level not system level to be able to make it more accessible if we want to use the code in different server
7. Mac Uswer save it in /usr/local/bin
8. os.enviorn['PATH'] +=  adding the path to already existing path 
9. You may get an error that says the chromedriver cannot be oppend then so what to do: 
    - go to your terminal 
    - run this: 
    which chromedriver
    - take away the wall by running this 
    xattr -d com.apple.quarantine /usr/local/bin/chromedriver
    - if you still not able to do it comment below and I will help you 
10. Open Chrome : driver = webdriver.Chrome()
11. got to 'https://www.expedia.com/' 
