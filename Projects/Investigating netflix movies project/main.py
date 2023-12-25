# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Start coding!
netflix_df = pd.read_csv("Investigating netflix movies project\\netflix_data.csv")

# Subset the netflix_df DataFrame such that only rows where the type is a "Movie" are preserved
netflix_subset = netflix_df[netflix_df['type']=='Movie']

# Investigate the Netflix movie data, keeping only the columns "title", "country", "genre", "release_year", "duration"
netflix_movies = netflix_subset[["title", "country", "genre", "release_year", "duration"]]

# find the movies that are shorter than 60 minutes
short_movies = netflix_movies[netflix_movies['duration'] < 60]

# Create a dictionary to map genres to colors
genre_colors = {
    "Children": "blue",
    "Documentaries": "green",
    "Stand-Up": "orange",
    "Other": "red"
}

# Initialize an empty list to store colors
colors = []

# Iterate through the rows of netflix_movies and assign colors based on genre
for index, row in netflix_movies.iterrows():
    genre = row['genre']
    if 'Children' in genre:
        colors.append(genre_colors['Children'])
    elif 'Documentaries' in genre:
        colors.append(genre_colors['Documentaries'])
    elif 'Stand-Up' in genre:
        colors.append(genre_colors['Stand-Up'])
    else:
        colors.append(genre_colors['Other'])

# Create a scatter plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(1,1,1)
ax.scatter(netflix_movies['release_year'], netflix_movies['duration'], c=colors)

# Set labels and title
ax.set_xlabel("Release year")
ax.set_ylabel("Duration (min)")
ax.set_title("Movie Duration by Year of Release")

# Show the plot
plt.show()