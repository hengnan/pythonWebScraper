# preq
# Install mongodb (pip install pymongo)
import requests
from bs4 import BeautifulSoup
import pandas as pd
import pymongo
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Done on windows powershell
# To test db queries
# run: mongosh mongodb://localhost:27017/
# run: use rotten_tomatoes

# start time
start_time = time.time()

# Connection to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["rotten_tomatoes"] # Create a new database named "rotten_tomatoes"
movies_collection = db["movies"]

# Simple database schema which supports all data collected from scraped website
movie_schema = {
    "title": str,
    "audience_score": int,
    "critics_score": int,
    "stream_date": str
}

# Doing this because I didn't realize that this page defaults to page 5 if you attempt to access a page > 5
# rotten tomato defaults this to page 5 no matter what number you input
# HORRIBLE SPEED
# base_url = 'https://www.rottentomatoes.com/browse/movies_at_home/?page=' + page
# driver = webdriver.Chrome()
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
driver = webdriver.Chrome(options=chrome_options)
driver.set_page_load_timeout(3000)
driver.get("https://www.rottentomatoes.com/browse/movies_at_home/")
# prompts user to input the number of pages
# they would like to scrap from rottentomato
# Note: 1 page is about 20 movies
page = int(input("Enter the number of pages you want to scrap from rottentomato: "))
for i in range(page):
    try:
        load_more_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-qa="dlp-load-more-button"]'))
        )
        load_more_button.click()
    except Exception as e:
        print("No more 'Load more' button available.")
        break
# html of whatever selenium browser ended on
page_source = driver.page_source

# Getting the contents from each url
# response = requests.get("https://www.rottentomatoes.com/browse/movies_at_home/?page=20")
# retrieving the target web page
# if response.status_code == 200:
#     print("Success!")
# else:
#     print("Error:", response.status_code)
# # parsing the target web page with Beautiful Soup
soup = BeautifulSoup(page_source, 'html.parser')
#
movies = soup.find_all('div', class_="flex-container")
# Data for csv file
data = []
# Data for mongo database
DBdata = []
for movie in movies:
    title = movie.find("span", class_="p--small", attrs={"data-qa": "discovery-media-list-item-title"}).text.strip()
    score_pairs = movie.find("score-pairs-deprecated")
    audience_score = 0
    critics_score = 0
    if score_pairs:
        audience_score = int(score_pairs["audiencescore"]) if score_pairs.get("audiencescore") else 0
        critics_score = int(score_pairs["criticsscore"]) if score_pairs.get("criticsscore") else 0
    stream_date = movie.find("span", class_="smaller", attrs={"data-qa": "discovery-media-list-item-start-date"}).text.strip()
    data.append([title, audience_score, critics_score, stream_date])
    DBdata.append({
        "title": title,
        "audience_score": audience_score,
        "critics_score": critics_score,
        "steam_date": stream_date
    })

# Create csv file
df = pd.DataFrame(data, columns=['Title', 'Audience Score', 'Critics Score', 'Steam Date'])
df.to_csv('rotten_tomatoes_movies.csv', index=False)

# Insert into Mongo Database
movies_collection.insert_many(DBdata)
# stop selenium
driver.quit()

end_time = time.time()

# Calculate elapsed time
elapsed_time = end_time - start_time

print("Elapsed time:", elapsed_time, "seconds")
