from pony.orm import *
from datetime import datetime


class BeerReview(db.Entity):
    brewery_id = Required(int)
    brewery_name = Required(unicode)
    review_time = Required(datetime)
    overall = Required(float)
    aroma = Required(float)
    appearance = Required(float)
    profilename = Optional(unicode)
    beer_style = Required(unicode)
    palate = Required(float)
    taste = Required(float)
    beer_name = Required(unicode)
    # Got no idea what _abv is...not required either
    beer_abv = Optional(float)
    beer_id = Required(int)
