# Miles Shinsato 11/30/2024 Assignment 7.2 Table Queries CSD310-A339

import mysql.connector
from mysql.connector import errorcode

# Database connection configuration
config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

try:
    # Attempting to connect to MySQL Database
    db = mysql.connector.connect(**config)

    # If connection is successful, print connection message
    print("\n  Database user {} connected to MySQL on host {} with database {}".format(
        config["user"], config["host"], config["database"]))

    # Prompt for User to acknowledge connection
    input("\n\n  Press any key to continue...")

    # Create cursor object to interact with the db
    cursor = db.cursor()

    # 1st Query: Select all fields from the studio table
    cursor.execute("SELECT studio_id, studio_name FROM studio")

    # Fetch all results from query
    studios = cursor.fetchall()
    print("\n\n-- DISPLAYING Studio RECORDS --")


    # Iterate through 'studio' records and print them
    for studio in studios:
        print("Studio ID: {}\nStudio Name: {}".format(studio[0], studio[1]))
        print("\n")

    # 2nd Query: Select all fields from the genre table
    cursor.execute("SELECT genre_id, genre_name FROM genre")

    # Fetch all results from query
    genres = cursor.fetchall()
    print("\n-- DISPLAYING Genre RECORDS --")

    # Iterate through 'genre' records and print them
    for genre in genres:
        print("Genre ID: {}\nGenre Name: {}".format(genre[0], genre[1]))
        print("\n")

    # 3rd Query: Select movie names for movies with a runtime less than 120 minutes (less than two hours)
    cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")
    short_movies = cursor.fetchall()
    print("\n-- DISPLAYING Short Film RECORDS --")
    for movie in short_movies:
        print("Film Name: {}\nFilm Runtime: {}".format(movie[0], movie[1]))
        print("\n")

    # 4th Query: List of film names and directors grouped by director
    cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")
    films = cursor.fetchall()
    print("\n-- DISPLAYING Director RECORDS in Order --")

    # Iterate through 'films' records and print them
    for film in films:
        print("Film Name: {}\nDirector: {}".format(film[0], film[1]))
        print("\n")

except mysql.connector.Error as err:

    # Error handling for two different errors
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        # Print message is login credentials are incorrect
        print("The supplied username or password is incorrect")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        # Print message for missing database
        print("The specified database does not exist")
    else:
        # General error message for other errors
        print(err)

# Finally block to ensure cursor and db connection is closed and release resources
finally:
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'db' in locals() and db:
        db.close()
