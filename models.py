# Import from peewee
from peewee import *
from flask import session
from playhouse.dataset import DataSet
from playhouse.postgres_ext import *


from config import Config

# Connect to a postgresql database
db = PostgresqlDatabase(database=Config.DATABASE, user=Config.USERNAME, password=Config.SECRET_KEY,
                         host=Config.HOST, port=Config.PORT)
db.connect()
# db = DataSet('sqlite:///datatest.db')

# new_table = db['data']
# new_table.thaw(format='csv', filename='data/data.csv')

class EarthQuake(Model):
    time = DateTimeField()
    lat = DecimalField()
    lon = DecimalField()
    magnitude = DecimalField()
    
    class Meta:
    # data is coming from rsvps.db
        database = db
        db_table = 'test'



