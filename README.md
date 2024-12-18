#TopRatingMoviesWebScraping
Project Description
TopRatingMoviesWebScraping is a full-stack web application that scrapes and displays top-rated movies from IMDb and Rotten Tomatoes. It uses web scraping techniques to gather movie data, stores the data in a MongoDB database, and serves it through a dynamic user-friendly interface built with Node.js, Express.js, and EJS templates.

#Features
1-Web Scraping

IMDb Scraper: Collects top-rated movies with metadata like title, director, actors, release date, and IMDb rating.
Rotten Tomatoes Scraper: Gathers similar movie data along with Rotten Tomatoes ratings.
Scripts: IMDB_scraper.py and rottentomatoes_scraper.py.

2-Data Storage

The scraped data is stored in CSV files:
IMDB_Top_Movies.csv
rotten_tomatoes_top_movies.csv
Combined data in movies_combined.csv.
Data can also be transferred to a MongoDB database.


3-Backend and API

Node.js with Express.js: Handles routes, controllers, and database interactions.
Routes:
imdbtomatoe.js (handles IMDb-Rotten Tomatoes comparisons)
movie.js (general movie-related routes)
tomatoe.js (Rotten Tomatoes routes).


4-Frontend

Dynamic EJS Views:
index.ejs: Home page.
imdbtomatoe.ejs: IMDb vs Rotten Tomatoes comparison.
tomatoe.ejs: Rotten Tomatoes view.
topmovie.ejs: Top movies listing.

5-Data Visualization

Users can browse movie data in a table format with:
Search functionality.
Pagination for better navigation.

-----------------------------------------------------------------

│   [image](https://github.com/user-attachments/assets/2f501ff1-dbb4-4364-af58-11e6c756cb4d)

│   │[image](https://github.com/user-attachments/assets/f9a2b340-4181-409a-892f-571b8a240fbe)





-----------------------------------------------------------------------------------


-------------------------------------------------------------------------------------------------------------------


--------------------------------------------------------------------
Technologies Used
Frontend
HTML5, CSS3
JavaScript (for dynamic functionality)
EJS (Embedded JavaScript templates)
Backend
Node.js
Express.js
MongoDB (for database storage)
Mongoose (ODM for MongoDB)
Web Scraping
Python Libraries:
BeautifulSoup or Scrapy for HTML parsing.
Requests for HTTP requests.
Data Storage
CSV Files
MongoDB
----------------------------------------------------------------------------------------

![image](https://github.com/user-attachments/assets/461d84af-89e9-4e07-9e0b-521e73cef5ae)


