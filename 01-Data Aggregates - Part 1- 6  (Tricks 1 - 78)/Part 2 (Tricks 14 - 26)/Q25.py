data = {'name': 'Peter', 'age': 30}
person = data.copy()
print(id(data) == id(person))