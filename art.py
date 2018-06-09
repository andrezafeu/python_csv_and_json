import json

with open('148.json') as artfile:
    # load() takes an object-like file and tries to turn it into a Python object
    art = json.load(artfile)
    print(art['description'])

kenneth = {'first_name': 'Kenneth', 'last_name': 'Love', 'topic': 'Python'}
craig = {'first_name': 'Craig', 'last_name': 'Dennis', 'topic': 'Java'}

with open('teachers.json', 'a') as teacherfile:
    json.dump([kenneth, craig], teacherfile)