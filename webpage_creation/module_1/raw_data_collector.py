import requests
import os
from bs4 import BeautifulSoup

# This module takes the path argument and creates the raw data from the list of articles provided
# The input command is "python run.py articles.txt" (This is for the example, default case). It will take the articles.txt and ensures it is a file (even if it is a file path).
# Once it is verified as a file, it will open the file and read the first URL. Then the web page will be opened and it will gather all of the raw HTML code and store it in
# article_#_raw.txt, with # being a number. It will then close the article and increase the counter variable, named articleNum, by one, and go until all of the URLs have been
# read. Then it will return the articleNum variable, which will be used in the processor module.

def rdc(arguments):
    articleFile = arguments[1] # Gets the path/file for the articles to be read
    if(os.path.isfile(articleFile)): # Checks if the path leads to a valid file
        articleList = open(articleFile, "r") # Opens the file as read only
        articleNum = 1
        for URL in articleList.readlines():
            URL = str(URL[:-1]) # Removes the newline tag from each URL
            articleName = "article_" + str(articleNum) + "_raw.txt" # Generates the raw file name
            directory = "Data/raw" # Path for which the file will be made
            file_path = os.path.join(directory, articleName) # Joins the file name and the file path
            article = open(file_path, "w", encoding="utf-8") # Opens a writeable file
            page = requests.get(URL) # Requests the webpage
            soup = BeautifulSoup(page.content, "html.parser") # Parses the webpage
            article.write(str(soup)) # Writes the raw HTML into the file
            articleNum += 1 # Increases the count number
            article.close() # Closes the file
    return articleNum
