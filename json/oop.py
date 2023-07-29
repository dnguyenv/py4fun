import json
from json import JSONEncoder

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User('Hoa', 40)

def encode_user(o):
    if isinstance(User):
        return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
    else:
        raise TypeError('Object of type user is not JSON serializable')

class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self,o)



#userJSON = json.dumps(user,cls = UserEncoder)
userJSON = UserEncoder().encode(user)
print(userJSON)

user = json.loads(userJSON)

print(user)

print(type(user))

def decode_user(dict):
    if User.__name__ in dict:
        return User(name=dict['name'], age=dict['age'])
    else:
        return dict

user = json.loads(userJSON, object_hook=decode_user)

print(type(user))

print(user.name)
