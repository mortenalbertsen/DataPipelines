import unicodecsv
from database import connect
from pony import db_session
from pony.orm import commit
from beer_review import BeerReview
from datetime import datetime

batch_size = 2000


@db_session
def read_csv_file(filepath):
    with open(filepath) as csv_file:
        csv_reader = unicodecsv.reader(csv_file)

        # Skip first line -> header
        next(csv_reader)

        counter = 0
        for row in csv_reader:
            brewery_id = int(row[0])
            brewery_name = row[1]
            epoch_duration = int(row[2])
            review_date = parse_datetime(epoch_duration)
            overall_rating = float(row[3])
            aroma_rating = float(row[4])
            appearance_rating = float(row[5])
            profilename = row[6]
            beer_style = row[7]
            palate_rating = float(row[8])
            taste_rating = float(row[9])
            beer_name = row[10]

            # Have no clue what this describes
            beer_abv = None
            if row[11].strip():
                beer_abv = float(row[11])

            beer_id = int(row[12])
            try:
                BeerReview(brewery_id=brewery_id,
                           brewery_name=brewery_name,
                           review_time=review_date,
                           overall=overall_rating,
                           aroma=aroma_rating,
                           appearance=appearance_rating,
                           profilename=profilename,
                           beer_style=beer_style,
                           palate=palate_rating,
                           taste=taste_rating,
                           beer_name=beer_name,
                           beer_abv=beer_abv,
                           beer_id=beer_id)
            except Exception as e:
                print('Error occured for' + str(row) +
                      ' , exception: ' + str(e))

            if counter % batch_size == 0:
                print('Committing, current count: ' + str(counter))
                commit()
            counter = counter + 1


def parse_datetime(epoch_duration):
    try:
        return datetime.utcfromtimestamp(epoch_duration)
    except Exception as e:
        print(str(e))
        return None
