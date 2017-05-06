# Python 3.6
# A dictionary contains {key: value}. Keys in a dictionary are unique.
# Dictionaries in this program contain {actor_name: birth_place}
# Dictionaries are mutable, i.e. it can be changed, after it is created.

# Initialization with empty dictionary
actors_dict = {}
print(actors_dict)              # to show what an empty dictionary looks like when printed

# Inserting into dictionary
actors_dict['Johnny Depp'] = 'Kentucky'
actors_dict['Jennifer Lawrence'] = 'Kentucky'
actors_dict['Ryan Gosling'] = 'Ontario'
print(actors_dict)

# Read value from dictionary - you can do this, but if actor is not in dictionary, then
# ... it will produce an error. See the following script to make it safe.
actor = actors_dict['Jennifer Lawrence']
print(actor)

# Read value from dictionary - Safe method. Safe when key is not in dictionary
# Dictionary Search based on key
actor = None
some_actor = 'Brad Pitt'
if some_actor in actors_dict:
    actor = some_actor
print(actor)

# Updating value in a dictionary, but if the actor is not in the dictionary, it will be added.
actors_dict['Ryan Gosling'] = "Canada"
print(actors_dict)

# Deleting an entry from dictionary. Safer to check if the key is in the dictionary, then delete.
# ... because if the key is not in the dictionary, it will result an error.
actor = 'Brad Pitt'
if actor in actors_dict:
    del actors_dict[actor]
print(actors_dict)

# ... example when actor is not in the dictionary.
actor = 'Chris Hemsworth'
if actor in actors_dict:
    del actors_dict[actor]
print(actors_dict)

# Dictionary Iteration
for i in actors_dict:
    print(i)                # reading the key
    print(actors_dict[i])   # reading the value

# Dictionary Search for value
searched_birth_place = 'Kentucky'
selected_actors = {}
for i in actors_dict:
    if actors_dict[i] == searched_birth_place:
        selected_actors[i] = searched_birth_place
print(selected_actors)

