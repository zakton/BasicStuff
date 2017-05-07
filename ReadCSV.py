# Python 3.6
# Read CSV.
# For Mac users, save the data file to Windows comma separated .csv (not the standard Mac OSX csv)

import unicodecsv

# --- 1 ---
# Reading a csv
# File name: actors.csv. Key: actor's name. Values: birthdate; birth place city, state and country;
# ... number of facebook likes.

with open('actors.csv', 'rb') as f:
    reader = unicodecsv.DictReader(f)
    actors_list = list(reader)

print(actors_list)

# --- 2 ---
# Reading a csv with duplicate keys
# Use of set come up with unique items
# File name: actor_movie.csv
# How many unique actors are there in the csv file?

with open('actor_movie.csv', 'rb') as f:
    reader = unicodecsv.DictReader(f)
    actor_movie_list = list(reader)

print(actor_movie_list)
print(len(actor_movie_list))

actor_set = set()
for a in actor_movie_list:
    actor_set.add(a['actor_name'])

print(actor_set)
print(len(actor_set))

# --- 3 ---
#  What movies does Ryan Gosling star in? How many?
# Again use set to keep unique movie titles

searched_actor = 'Ryan Gosling'
movie_set = set()
for a in actor_movie_list:
    if a['actor_name'] == searched_actor:
        movie_set.add(a['movie_title'])

print('Ryan Gosling stars in these movies: ')
print(movie_set)
print(len(movie_set))

