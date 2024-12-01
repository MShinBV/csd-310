# Miles Shinsato 11/30/2024 Assignment 8.2 Movies Uodates & Deletes CSD310-A339

# Importing MySQL Connector
import mysql.connector
from mysql.connector import errorcode

# Database configuration using a dictionary
config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

try:
    # Attempt to connect to the MySQL database
    db = mysql.connector.connect(**config)

    print("\n  Database user {} connected to MySQL on host {} with database {}".format(
        config["user"], config["host"], config["database"]))

    input("\n\n  Press any key to continue...")

    # Create a cursor to interact with the database
    cursor = db.cursor()

    # Function to display selected films with their associated labels
    def show_films(cursor, title):

        # Execute the inner join query to get film details for the rest of the syntax to run
        cursor.execute("""
            SELECT film_name AS Name, film_director AS Director, 
                   genre_name AS 'Genre Name ID', studio_name AS 'Studio Name' 
            FROM film 
            INNER JOIN genre ON film.genre_id = genre.genre_id 
            INNER JOIN studio ON film.studio_id = studio.studio_id
        """)

        # Get the results from the cursor object
        films = cursor.fetchall()

        # Print Format for how the titles should all be printed
        print("\n -- {} --".format(title))

        # Print format for the film data set and how to display the results
        for film in films:
            print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))

    # Display films before any changes (initial data)
    show_films(cursor, "DISPLAYING FILMS")

    # Insert a new entry into the database for the film 'Alien: Romulus' directed by Fede Álvarez, a horror film by 20th Century Fox that released in 2024 with a runtime of 119
    # Using the example INSERT syntax from the material
    insert_query = """
        INSERT INTO film (film_name, film_director, genre_id, studio_id, film_releaseDate, film_runtime)
        VALUES('Alien: Romulus', 'Fede Álvarez', 1, 1, '2024', 119);
    """
    cursor.execute(insert_query)

    # Commiting to the DB inserting the film Alien: Romulus
    db.commit()

    # Prompt to display films after inserting the new film
    show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

    # Update the genre of 'Alien' to 'Horror'
    # Using the example UPDATE syntax from the material
    update_query = """
        UPDATE film 
        SET genre_id = 1,  # 1 is the genre_id for Horror
            film_releaseDate = '2024',  # Update release date as needed
            film_runtime = 119  # Update runtime as needed
        WHERE film_name = 'Alien';
    """
    cursor.execute(update_query)

    # Commiting to the DB of changing the Genre for Alien
    db.commit()

    # Prompt to display films after the update
    show_films(cursor, "DISPLAYING FILMS AFTER UPDATE - Change Alien to Horror")

    # Delete 'Gladiator' film
    # Using example DELETE syntax
    delete_query = """DELETE FROM film WHERE film_name = 'Gladiator';"""
    cursor.execute(delete_query)

    # Commiting DB change of deletion of Gladiator
    db.commit()

    # Display films after deletion
    show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

except mysql.connector.Error as err:
    # Error handling based on the error code
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password is incorrect")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
    else:
        print(err)

finally:
    # Close the cursor and the database connection
    if db.is_connected():
        cursor.close()
        db.close()
