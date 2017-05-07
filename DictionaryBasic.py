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
for k in actors_dict:
    print(k)                # reading the key
    print(actors_dict[k])   # reading the value

# Dictionary Iteration - reading the values
print("\nDictionary Iteration - reading the values")
for v in actors_dict.values():
    print(v)

# Dictionary Iteration - reading both key and value pairs
print("\nDictionary Iteration - reading both key and value pairs")
for k, v in actors_dict.items():
    print(k, 'was born in', v)

# Dictionary Search for value
searched_birth_place = 'Kentucky'
selected_actors = {}
for i in actors_dict:
    if actors_dict[i] == searched_birth_place:
        selected_actors[i] = searched_birth_place
print(selected_actors)

# Alternatively, using key and value as for item; contain result in a set
searched_birth_place = 'Kentucky'
selected_actors = set()
for a, bp in actors_dict.items():
    if bp == searched_birth_place:
        selected_actors.add(a)
print(selected_actors)
print()

# defaultdict
print("defaultdict demo")
from collections import defaultdict
actors_dict2 = defaultdict(lambda:'Unknown birth place')
actors_dict2['Jimmy Stewart'] = 'USA'
actors_dict2['Kenny Rogers'] = 'USA'
print(actors_dict2['Kenneth Branagh'])              # Not sure what's the use of the defaultdict'. Can just use None for value.
print(actors_dict2)

# new pointer vs new instance; assigning vs copying
print("\nNew pointer vs New Instance")
dict_pointer = actors_dict                          # a new pointer is assigned to the same instance pointed by actors_dict
dict_pointer['Kenneth Branagh'] = 'Northern Ireland'
print(actors_dict)                                  # New actor added as a new actor added through dict_pointer
print(dict_pointer)
print()
another_dict = actors_dict.copy()                   # a new instance is created, content of actor_dict is copied to it
another_dict['Kevin Spacey'] = 'USA'
print(actors_dict)                                  # Unchanged
print(another_dict)                                 # New actor added


