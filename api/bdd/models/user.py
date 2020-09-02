from tortoise.models import Model
from tortoise import fields


class User(Model):
    """
        Table qui représente l'utilisateur
    """
    uuid = fields.CharField(max_length=32)
    username = fields.CharField(max_length=20, unique=True)
    hashed_password = fields.CharField(max_length=64)
    salt = fields.CharField(max_length=32)
    sex = fields.IntField()
    user_is_validate = fields.BooleanField()
    email = fields.CharField(max_length=30, unique=True)
    goal = fields.IntField()
    # See date and time formats : https://www.w3.org/TR/NOTE-datetime
    birthday = fields.DateField()
    weight = fields.FloatField()
    size = fields.FloatField()
    sportfrequency = fields.FloatField()
