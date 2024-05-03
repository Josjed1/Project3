from bs4 import BeautifulSoup
import os
from module_3 import summary

def process(articleNum):
    num = 1
    rawDirectory = "Data/raw"  # Directory for RAW data
    p_Directory = "Data/processed"  # Directory for processed data
    
    while num < articleNum: 
        
        
        # Construct file paths
        rawArticleName = "article_" + str(num) + "_raw.txt"  
        p_articleName = "article_" + str(num) + "_full.txt"  
        rawPath = os.path.join(rawDirectory, rawArticleName) 
        p_Path = os.path.join(p_Directory, p_articleName)  
        
        # Open raw file, read content, and parse HTML
        article = open(rawPath, "r", encoding="utf-8")  
        rawData = article.read()  # Reads the raw file
        rawData = BeautifulSoup(rawData, "html.parser")  
        article.close()  # Closes the raw file
        
        # Open processed file for writing
        article = open(p_Path, "w", encoding="utf-8") 
        
        # Extract and write header
        header = rawData.find("h1").text.strip()  
        article.write(header + "\n\n")  
        
        # Extract and write paragraphs
        elements = rawData.find_all("p", class_="paragraph inline-placeholder")  
        for element in elements:
            text = element.text.strip() + "\n"  
            article.write(text) 
        
        article.close()  
        num += 1  # Increases num by 1
