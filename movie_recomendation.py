
# Movie Recommendation System
# CodSoft Artificial Intelligence Internship

# Movie database with genres
movies = {
    "3 Idiots": ["Comedy", "Drama", "Education"],
    "Chhichhore": ["Comedy", "Drama", "Education"],
    "Taare Zameen Par": ["Drama", "Education"],
    "Dangal": ["Drama", "Sports"],
    "Bhaag Milkha Bhaag": ["Drama", "Sports"],
    "Zindagi Na Milegi Dobara": ["Comedy", "Drama", "Adventure"],
    "Yeh Jawaani Hai Deewani": ["Romance", "Drama", "Comedy"],
    "Dilwale Dulhania Le Jayenge": ["Romance", "Drama"],
    "Jab We Met": ["Romance", "Comedy"],
    "Andhadhun": ["Thriller", "Mystery", "Crime"],
    "Drishyam": ["Thriller", "Mystery", "Crime"],
    "Bhool Bhulaiyaa": ["Comedy", "Horror", "Mystery"],
    "Stree": ["Comedy", "Horror"],
    "Interstellar": ["Sci-Fi", "Adventure", "Drama"],
    "The Martian": ["Sci-Fi", "Adventure"],
    "Inception": ["Sci-Fi", "Thriller", "Action"],
    "Avengers: Endgame": ["Action", "Sci-Fi", "Adventure"],
    "Spider-Man: No Way Home": ["Action", "Sci-Fi", "Adventure"],
    "The Conjuring": ["Horror", "Thriller"],
    "A Quiet Place": ["Horror", "Thriller", "Drama"]
}


# Recommend similar movies
def recommend_movies(selected_movie):

    if selected_movie not in movies:
        print("\nSorry! Movie not found in our database.")
        return

    selected_genres = set(movies[selected_movie])
    recommendations = []

    for movie, genres in movies.items():

        # Do not recommend the same movie
        if movie == selected_movie:
            continue

        # Count matching genres
        matching_genres = selected_genres.intersection(genres)

        # Calculate similarity percentage
        total_genres = selected_genres.union(genres)

        similarity = (
            len(matching_genres) / len(total_genres)
        ) * 100

        if similarity > 0:
            recommendations.append(
                (movie, similarity, matching_genres)
            )

    # Sort by similarity from highest to lowest
    recommendations.sort(
        key=lambda item: item[1],
        reverse=True
    )

    print("\nRecommendations for:", selected_movie)
    print("-" * 45)

    if not recommendations:
        print("No similar movies found.")
        return

    # Display top 5 recommendations
    for movie, score, genres in recommendations[:5]:
        print("\nMovie:", movie)
        print("Similarity:", round(score, 2), "%")
        print("Matching genres:", ", ".join(sorted(genres)))


# Main program
def main():

    print("=" * 45)
    print("     MOVIE RECOMMENDATION SYSTEM")
    print("=" * 45)

    while True:

        print("\nAvailable Movies:")

        for movie in movies:
            print("-", movie)

        selected_movie = input(
            "\nEnter a movie name (or type 'exit'): "
        ).strip()

        if selected_movie.lower() == "exit":
            print("Thank you for using our system!")
            break

        # Find movie regardless of letter case
        matched_movie = None

        for movie in movies:
            if movie.lower() == selected_movie.lower():
                matched_movie = movie
                break

        if matched_movie:
            recommend_movies(matched_movie)
        else:
            print(
                "\nMovie not found. Please enter a name "
                "from the available movies."
            )


# Start the application
if __name__ == "__main__":
    main()
