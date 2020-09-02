from tortoise.models import Model
from tortoise import fields

class Consumption(Model):
    week = fields.IntField()
    day = fields.IntField()
    protein = fields.IntField()
    calories = fields.IntField()
    lipid = fields.IntField()
    glucides = fields.IntField()
    user = fields.ForeignKeyField(model_name='models.User')