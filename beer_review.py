from pony.orm import *
from datetime import datetime


class BeerReview(db.Entity):

    brewery_id = Required(int)
    brewery_name = Required(str)
    review_time = Required(datetime)
    overall = Required(float)
    aroma = Required(float)
    appearance = Required(float)
    profilename = Required(str)
    beer_style = Required(str)
    palate = Required(float)
    taste = Required(float)
    beer_name = Required(str)
    # Got no idea what _abv is...
    beer_abv = Required(float)
    beer_id = Required(int)
