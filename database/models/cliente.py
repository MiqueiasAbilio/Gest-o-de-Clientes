from peewee import Model, CharField, DateTimeField
from email.policy import default
import datetime

from peewee import Model, CharField, DateField
from database.database import db

class Cliente(Model):
    nome = CharField()
    email = CharField()
    data_criacao = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db