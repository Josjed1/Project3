from bs4 import BeautifulSoup
import os
from module_3 import summary

def process(articleNum):
    num = 1
    rawDirectory = "Data/raw"  # Directory for RAW data
    p_Directory = "Data/processed"  # Directory for processed data
    while num < articleNum:  # While the number is less than or equal to the number of articles
        rawArticleName = "article_" + str(num) + "_raw.txt"  # The raw file names
        p_articleName = "article_" + str(num) + "_full.txt"  # The processed file names
        rawPath = os.path.join(rawDirectory, rawArticleName)  # The raw file path
        p_Path = os.path.join(p_Directory, p_articleName)  # The processed file path
        article = open(rawPath, "r", encoding="utf-8")  # Opens the raw file to read
        rawData = article.read()  # Reads the raw file
        rawData = BeautifulSoup(rawData, "html.parser")  # Parses the raw file
        article.close()  # Closes the raw file
        article = open(p_Path, "w", encoding="utf-8")  # opens the blank file, for the processed data

        # Extract and write the header
        header = rawData.find("h1").text.strip()  # Extract the header
        article.write(header + "\n\n")  # Write the header to the processed file

        # Extract and write the paragraphs
        elements = rawData.find_all("p", class_="paragraph inline-placeholder")  # Find paragraphs
        for element in elements:
            text = element.text.strip() + "\n"  # Extract and format paragraphs
            article.write(text)  # Write the paragraphs to the processed file

        article.close()  # Close the new file, meaning all of the processed data should be in there
        num += 1  # Increases num by 1
