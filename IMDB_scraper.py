import requests
import csv

# Your OMDb API Key
api_key = "952164d7"

# List of movies to fetch

movie_titles = [
   "L.A. Confidential", "The Godfather", "Casablanca", "Seven Samurai", "Parasite",
   "Schindler's List", "Top Gun: Maverick", "Toy Story 2", "Chinatown", "On the Waterfront",
   "The Battle of Algiers", "Toy Story", "Rear Window", "Modern Times", "How to Train Your Dragon",
   "All About Eve", "Spirited Away", "Up", "The Third Man", "Spotlight", "Spider-Man: Into the Spider-Verse",
   "The Philadelphia Story", "Finding Nemo", "Singin' in the Rain", "12 Angry Men", "Toy Story 3",
   "Sunset Boulevard", "Coco", "The Godfather, Part II", "Three Colors: Red", "Selma", "Zootopia",
   "Citizen Kane", "Annie Hall", "Cool Hand Luke", "The Holdovers", "Inside Out",
   "Dr. Strangelove Or: How I Learned to Stop Worrying and Love the Bomb", "Let the Right One In",
   "The Lord of the Rings: The Two Towers", "Knives Out", "M", "Toy Story 4", "The Wrestler", "Goodfellas",
   "The Wizard of Oz", "Double Indemnity", "Psycho", "Paddington 2", "Before Sunrise", "The Dark Knight",
   "The Maltese Falcon", "It Happened One Night", "The Wages of Fear", "North by Northwest",
   "Bicycle Thieves", "Alien", "Argo", "Get Out", "The Kid", "Mission: Impossible - Dead Reckoning Part One",
   "The Pianist", "Kind Hearts and Coronets", "The 400 Blows", "Grave of the Fireflies", "The Big Sick",
   "Minari", "Portrait of a Lady on Fire", "The Treasure of the Sierra Madre", "Apocalypse Now",
   "Mission: Impossible - Fallout", "The Last Picture Show", "Tampopo", "Mad Max: Fury Road", "Tokyo Story",
   "A Hard Day's Night", "Metropolis", "Good Will Hunting", "The Gold Rush", "Aliens",
   "Spider-Man: Across the Spider-Verse", "The Good, the Bad and the Ugly", "Harry Potter and the Deathly Hallows: Part 2"
]
# Input CSV file for Rotten Tomatoes ratings
rotten_tomatoes_file = "rotten_tomatoes_top_movies.csv"

# Output CSV file for combined data
output_file = "movies_combined.csv"

# Function to fetch IMDb data
def fetch_imdb_data(movie_title):
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()

    if data["Response"] == "True":
        return {
            "Title": data.get("Title", "N/A"),
            "Year": data.get("Year", "N/A"),
            "Director": data.get("Director", "N/A"),
            "Writers": data.get("Writer", "N/A"),
            "Actors": data.get("Actors", "N/A"),
            "Genre": data.get("Genre", "N/A"),
            "IMDb Rating": data.get("imdbRating", "N/A")
        }
    else:
        return {"Title": movie_title, "Year": "N/A", "Director": "N/A", "Writers": "N/A", "Actors": "N/A", "Genre": "N/A", "IMDb Rating": "N/A"}

# Function to load Rotten Tomatoes ratings
def load_rotten_tomatoes_data(file_path):
    rotten_data = {}
    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            title = row["Title"].strip().lower()
            rating = row.get("Rating", "N/A")
            rotten_data[title] = rating
    return rotten_data

# Fetch IMDb data and combine with Rotten Tomatoes ratings
rotten_data = load_rotten_tomatoes_data(rotten_tomatoes_file)
movies_data = []

for title in movie_titles:
    print(f"Fetching IMDb data for: {title}")
    imdb_data = fetch_imdb_data(title)
    normalized_title = imdb_data["Title"].strip().lower()
    imdb_data["Rotten Tomatoes"] = rotten_data.get(normalized_title, "N/A")
    movies_data.append(imdb_data)

# Save combined data to CSV
with open(output_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["Title", "Year", "Director", "Writers", "Actors", "Genre", "IMDb Rating", "Rotten Tomatoes"])
    writer.writeheader()
    writer.writerows(movies_data)

print(f"Combined data saved to {output_file}")

