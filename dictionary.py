person={
    "name":"mark",
    "age": 24,
    "gender":"male"
}
print(type(person))
print(person)
print(person["name"])

#dictionary methods
#.key returns all keys in the dictionary
print(person.keys())

#.values returns all the values
print(person.values())

#.items returns a list key value pairs
print(person.items())

#pop removes value of specific key
print(person.pop('gender'))

#.get returns the value of a specified key
print(person.get('name'))
