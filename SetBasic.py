# Python 3.6
# A set contains unique values
# Sets in this program contain names of actors

# Initialization with an empty set
actors_set = set()
print(actors_set)              # To show what an empty set looks like when printed

# Inserting into a set
actors_set.add('Johnny Depp')
actors_set.add('Jennifer Lawrence')
actors_set.add('Ryan Gosling')
print(actors_set)

# Initialization with a set of items
actors_set = {'Leonardo DiCaprio', 'Tom Hardy', 'Chris Hemsworth'}
print(actors_set)

# Inserting into a set (again)
actors_set.add('Jason Statham')
actors_set.add('Christian Bale')
actors_set.add('Joseph Gordon-Levitt')
print(actors_set)

# Reading a single item from a set, not possible, unless
# ... done through an iteration
# ... done through a search

# Updating a single item in a set, not possible, unless
# ... done using remove and add

# Removing an item from a set
actors_set.remove('Jason Statham')      # not a safe way - if item not in the set, an error will occur
print(actors_set)

actor = 'Channing Tatum'                # safe way - even if item is not in the set
if actor in actors_set:
    actors_set.remove(actor)
print(actors_set)

actor = 'Leonardo DiCaprio'             # safe way - example of removing item already existing in the set
if actor in actors_set:
    actors_set.remove(actor)
print(actors_set)

# Set iteration
for actor in actors_set:
    print(actor)

# Searching an item in a set
actor = 'Channing Tatum'                # example of search - when the searched item is not in the set
if actor in actors_set:
    print(actor,'is in the set')
else:
    print(actor,'is not in the set')

actor = 'Chris Hemsworth'               # example of search - when the searched item is in the set
if actor in actors_set:
    print(actor,'is in the set')
else:
    print(actor,'is not in the set')