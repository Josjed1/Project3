import requests
import os
from bs4 import BeautifulSoup


#This module processes a list of articles specified in a file path provided as an argument, typically in the format "python run.py articles.txt". It verifies the file's existence, then sequentially reads each URL from the file. 
#For each URL, it fetches the corresponding webpage, extracts the raw HTML code, and saves it into a file named article_#_raw.txt, where # increments for each article. Finally, it returns the total number of articles processed.

def rdc(arguments):
    articleFile = arguments[1]  # Gets the path/file for the articles to be read
    
    if os.path.isfile(articleFile):  # Checks if the path leads to a valid file
        articleList = open(articleFile, "r")  
        articleNum = 1
        
        for URL in articleList.readlines():
            #Generating file names, and the paths that they will take
            URL = str(URL[:-1])  
            articleName = "article_" + str(articleNum) + "_raw.txt"  
            directory = "Data/raw" 
            file_path = os.path.join(directory, articleName) 
            
            # We go to the url and grab the data (HTML) and write with it
            article = open(file_path, "w", encoding="utf-8") 
            page = requests.get(URL) 
            soup = BeautifulSoup(page.content, "html.parser")  
            article.write(str(soup))  
            articleNum += 1  
            article.close()
            
    return articleNum
