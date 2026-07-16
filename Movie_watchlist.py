#==== Movie Watchlist ====
#1. Add movie
movies = []

def add_movie(movies, title, genre):
    new_movie = {"title" : title,
                 "genre" : genre,
                 "watched" : False
    }
    movies.append(new_movie)
    print(f"{title} has been added to the movie list")


#2. List all movies

def list_movies(movies):
    if len(movies) == 0:
        print("There are no movies saved")
        return
    
    print(f"There are {len(movies)} saved")

    for movie in movies:
        print(f"title: {movie["title"]}")
        print(f"genre: {movie["genre"]}") 
        print(f"watched": {"watched" if movie["watched"] else "not watched"})
        print("-" * 30)



#3. Search by title

def search_movie(movies, search_term):
    results = []
    for movie in movies:
        if search_term.lower() in movie["title"].lower():
            results.append(movie)
    return results

        


#4. Mark as watched
def mark_watched(movies, search_watched):
    for movie in movies:
        if search_watched.lower() in movie["title"].lower():
            movie["watched"] = True
            print(f"You have watched {movie['title']}")
            return

    print("Movie not found")



#5. Delete movie

def delete_movie(movies, title):
    for index, movie in enumerate(movies):
        if title.lower() == movie["title"].lower():
            movies.pop(index)
            print(f"You have deleted {movie['title']}")
            return
    print("Movie not found")





movies = []
def main():
    while True:
        print("\n==== Movie Watchlist ====")
        print("1. Add a movie")
        print("2. List all movies")
        print("3. Search a movie")
        print("4. Mark a movie as watched")
        print("5. Delete a movie")
        print("6. Quit")

        option = input("Choose an option between 1-6: ")

        if option == "1":
            title = input("Enter movie title: ")
            genre = input("Enter movie genre: ")
            add_movie(movies, title, genre)

        elif option == "2":
            list_movies(movies)

        elif option == "3":
            search_term = input("Search a movie:")
            results = search_movie(movies, search_term)
            if len(results) == 0:
                print("No results founds")
            else:
                for movie in results:
                    print(f"title: {movie['title']}")
                    print(f"genre: {movie['genre']}")
                    print('✅ Watched' if movie['watched'] else ' ⏳ Not watched yet')

            

        elif option == "4":
            search_watched = input("Which movie have you watched?: ")
            mark_watched(movies, search_watched)

        elif option == "5":
            title = input("Which movie do you want to delete?: ")
            delete_movie(movies, title)

        elif option == "6":
            print("Watch list closed, Goodbye!!")
            break

        else:
            print("You have entered an invalid option, please choose between 1 & 6")

if __name__ == "__main__":
    main()



    


 