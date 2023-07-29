import json

person = {
    "name": "Duy",
    "age": 43,
    "city": "Cary",
    "hasChildren": True,
    "titles": [
        "engineer",
        "programmer"
    ]
}
def func3():
    personJSON = json.dumps(person, indent=4, sort_keys=True)
    loadedPerson = json.loads(personJSON)
    print(loadedPerson)


def func1():
    personJSON = json.dumps(person, indent=4, sort_keys=True)
    print(personJSON)

def func2():
    with open('person.json', 'w') as file:
        json.dump(person, file, indent=4)

def open_file():
    with open('example.json','r') as file:
        person = json.load(file)
        print(person)



#func1()

#func2()

#func3()

open_file()