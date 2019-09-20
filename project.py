from marshmallow import Schema, fields, pprint, post_load, ValidationError, validates


class Person(object):
    def __init__(self, name, age, address, email):
        self.name = name
        self.age = age
        self.address = address
        self.email = email

    def __repr__(self):
        return f'Hello I am{self.name} and currrently {self.age} old. I live in {self.address}. My current email is {self.email}'
'''
def validate_age(age):
    if age < 25:
        #return False
        raise ValidationError('That is to young')
'''
class PersonSchema(Schema):
    address = fields.String(required = True)
    name = fields.String()
    age = fields.Integer()
    email = fields.Email()

    @post_load
    def create_person(self, data):
        return Person(**data)
    
    @validates('age')
    def validate_age(self, age):
        if age < 25:
            raise ValidationError('Too young')
            # return False

input_dict = {}

input_dict['name'] = input('What is your name? ')
input_dict['age'] = input('What is your age? ')
input_dict['address'] = input('What is your address? ')
input_dict['email'] = input('What is your email? ')

schema = PersonSchema()

result = schema.load(input_dict)

print(result.errors)