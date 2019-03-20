from pony.orm import *
from datetime import datetime


def connect():
    db = Database()
    db.bind(provider='mysql',
            host='127.0.0.1',
            user="BaverageImporter",
            passwd='tintinToblerone542!',
            db='Beverages')
    return db


def create_mapping_for_entities():
    db.generate_mapping(create_tables=True)
