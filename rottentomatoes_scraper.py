from bs4 import BeautifulSoup
import requests
from lxml import html
import pandas as pd

# Define URL
url = 'https://editorial.rottentomatoes.com/guide/best-movies-of-all-time/'

# Request the page
response = requests.get(url)
if response.status_code != 200:
    print("Failed to retrieve the page.")
    exit()

# Parse the page with BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Convert the BeautifulSoup object to an lxml object for XPath usage
tree = html.fromstring(str(soup))

# Use XPath to select movie details
movies_data = []

# Extract all movie rows using XPath
movies = tree.xpath('//*[@id="article_main_body"]/div[1]/div[2]/div[1]/table/tbody/tr')

# Iterate over the movies and extract data
for movie in movies:
    try:
        # Extracting the rank, title, and rating using XPath
        rank = movie.xpath('.//td[1]//text()')
        rank = rank[0].strip() if rank else "No rank"
        
        title_column = movie.xpath('.//td[2]/p/span[2]/a')
        title = title_column[0].text.strip() if title_column else "No title"
        
        # Updated XPath to get the rating (generalized for all rows)
        rating = movie.xpath('.//td[2]/p/span[1]/span/strong/text()')
        rating = rating[0].strip() if rating else "No rating"
        
        # Save data
        movies_data.append({
            "Title": title,
            "Rating": rating
        })
    except Exception as e:
        print(f"Error processing movie: {e}")
        continue

# Save data to CSV
df = pd.DataFrame(movies_data)
df.to_csv('rotten_tomatoes_top_movies.csv', index=False)

# Print movie name and rating only
for movie in movies_data[:10]:  # Show the first 10 movies
    print(f"{movie['Title']} ({movie['Rating']})")
