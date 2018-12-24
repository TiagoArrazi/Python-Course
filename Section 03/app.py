"""
-Enter 'a' to add a movie, 'l' to list your movies, 'f' to find your movies, and 'q' to quit

-Add movies
-List movies
-Find movie
-Stop running the program

"""
from os import system
from time import sleep
import json


def add_movie():

    movie = dict()
    
    movie_name = input('Enter the name of the movie: ')
    movie_director = input('Who directed it? ')
    year_of_production = int(input('When was it made? '))

    movie['name'] = movie_name
    movie['director'] = movie_director
    movie['year'] = year_of_production

    with open('movies.json', 'a+') as movie_file:
        json.dump(movie, movie_file)
        movie_file.write('\n')


def list_movies():

    with open('movies.json', 'r') as movie_file:
        for line in movie_file:
            movie = json.loads(line)
            print(f"Movie name: {movie['name']}")
            print(f"Director: {movie['director']}")
            print(f"Year: {movie['year']}\n")


def find_movie():

    search_by = input('How would you like to search it (name, director, year)? ')

    if search_by.lower() == 'name':
        print('searching by name...')
        movie_name = input('What is the name of the movie? ')
        by_name(movie_name.upper())

    elif search_by.lower() == 'director':
        print('searching by director...')
        director_name = input('What is the director\'s name? ')
        by_director(director_name.upper())

    elif search_by.lower() == 'year':
        print('searching by year of production...')
        year = int(input('When was it made? '))
        by_year(year)

    else:
        print('Invalid field!')


def by_name(name):
    with open('movies.json', 'r') as movie_file:
        for line in movie_file:
            movie = json.loads(line)
            if name in movie['name'].upper():
                print(f"\nMovie name: {movie['name']}")
                print(f"Director: {movie['director']}")
                print(f"Year: {movie['year']}\n")


def by_director(director):
    with open('movies.json', 'r') as movie_file:
        for line in movie_file:
            movie = json.loads(line)
            if director in movie['director'].upper():
                print(f"\nMovie name: {movie['name']}")
                print(f"Director: {movie['director']}")
                print(f"Year: {movie['year']}\n")


def by_year(year):
    with open('movies.json', 'r') as movie_file:
        for line in movie_file:
            movie = json.loads(line)
            if year == movie['year']:
                print(f"\nMovie name: {movie['name']}")
                print(f"Director: {movie['director']}")
                print(f"Year: {movie['year']}\n")


# user interface
while True:
    print('------------------')
    print('\n')
    print('a - Add a movie\n')
    print('l - List your movies\n')
    print('f - Find your movies\n')
    print('q - Quit\n')
    opt = input('Welcome, please select an option \n')

    if opt.lower() == 'a':
        system('clear')
        add_movie()

    elif opt.lower() == 'l':
        system('clear')
        list_movies()

    elif opt.lower() == 'f':
        system('clear')
        find_movie()

    elif opt.lower() == 'q':
        print('Quitting')
        sleep(1)
        system('clear')
        break

    else:
        system('clear')
        print('Invalid option')
        continue
