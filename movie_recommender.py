import pandas as pd
import ast

# Load dataset
movies = pd.read_csv(r"C:\Users\DELL\Downloads\Movie-recomendation\tmdb_5000_movies.csv")

# Convert JSON string to list
def convert(text):
    try:
        return [i['name'] for i in ast.literal_eval(text)]
    except:
        return []

movies['genres'] = movies['genres'].apply(convert)

# Convert release_date to datetime for sorting
movies['release_date'] = pd.to_datetime(movies['release_date'], errors='coerce')

# Available categories
categories = ["Action", "Adventure", "Animation", "Comedy", "Crime",
              "Documentary", "Drama", "Family", "Fantasy", "History",
              "Horror", "Music", "Mystery", "Romance", "Science Fiction",
              "Thriller", "War", "Western"]

print("=" * 60)
print("🎬 MOVIE CATEGORY RECOMMENDER 🎬".center(60))
print("=" * 60)
print("\nAvailable Categories:")
print(", ".join(categories))

# Ask user to choose a category
choice = input("\nEnter a category from above: ").strip().lower()

# Filter by category (case-insensitive)
filtered_movies = movies[movies['genres'].apply(lambda g: any(choice == genre.lower() for genre in g))]

# Sort by latest release date
filtered_movies = filtered_movies.sort_values(by="release_date", ascending=False)

# Show results
if filtered_movies.empty:
    print(f"\n❌ No movies found for category '{choice}'.")
else:
    print(f"\n📅 Latest Movies in Category '{choice.title()}':\n" + "-" * 60)
    for index, row in filtered_movies.head(10).iterrows():
        print(f"🎥 Title       : {row['title']}")
        print(f"📅 Release Date: {row['release_date'].date() if pd.notnull(row['release_date']) else 'Unknown'}")
        print(f"⭐ Rating      : {row['vote_average']}/10")
        print("-" * 60)
        
