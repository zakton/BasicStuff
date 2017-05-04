# Python 3.6
# A list contains values
# Lists in this program contain names of actors
# Lists are mutable, i.e. it can be changed, after it is created.
# Common uses for sets are fast membership testing, removing duplicates from a sequence,
# ... and computing mathematical operations such as intersection, union, difference,
# ... and symmetric difference.

# Initialization with an empty list
actors_list = []
print(actors_list)              # To show what an empty list looks like when printed

# Inserting into a list
actors_list.append('Johnny Depp')
actors_list.append('Jennifer Lawrence')
actors_list.append('Ryan Gosling')
print(actors_list)

# Initialization with a starting list
actors_list = ['Leonardo DiCaprio', 'Tom Hardy', 'Chris Hemsworth']
print(actors_list)

# Inserting into a list (again)
actors_list.append('Jason Statham')
actors_list.append('Christian Bale')
actors_list.append('Joseph Gordon-Levitt')
actors_list.append('Robert De Niro')
actors_list.append('Robert Downey Jr.')
print(actors_list)

# Reading value from a list
print(actors_list[0])       # read first item
print(actors_list[1])       # read second item
print(actors_list[2])       # read third item
print(actors_list[-1])      # read last item

# Removing a value from a list
actors_list.pop()           # removing last item
print(actors_list)

actors_list.pop(0)          # removing first item
print(actors_list)

actors_list.pop(1)          # removing second item
print(actors_list)

actors_list.remove('Jason Statham')     # removing a known item, but this is not a safe way
print(actors_list)                      # ... because when item is not in the list, program crashes

# Removing a known item from a list - the safe way - first occurrence is removed.
actor = 'Channing Tatum'                # removing an item not in the list
if actor in actors_list:
    actors_list.remove(actor)
print(actors_list)

actor = 'Joseph Gordon-Levitt'          # removing an item that exists in the list
if actor in actors_list:
    actors_list.remove(actor)
print(actors_list)

# List iteration
for i in actors_list:
    print(i)

# Searching a list - first occurence
actor = "Christian Bale"
if actor in actors_list:
    print(actor)