import csv
from database import connect
from pony import db_session
from beer_review import BeerReview
import io


@db_session
def load_csv_entries_into_db(csv_file):
    entries = read_csv_file(csv_file)

    for entry in entries:
        BeerReview(brewery_id=row[0],
                   brewery_name=row[1],
                   review_time=row[2],
                   overall=row[3],
                   review_aroma=row[4],
                   review_appearance=row[5],
                   review_profilename=row[6],
                   beer_style=row[7],
                   review_palate=row[8],
                   review_taste=row[9],
                   beer_name=row[10],
                   beer_abv=row[11],
                   beer_beerid=row[12])


@db_session
def read_csv_file(filepath):
    with io.open(filepath) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        # Skip first line -> header
        next(csv_reader)
        items = []
        for row in csv_reader:
            print(unicode(row))
            epoch_duration = int(row[2])
            review_date = datetime.utcfromtimestamp(epoch_duration)
            BeerReview(brewery_id=row[0],
                       brewery_name=row[1],
                       review_time=review_date,
                       overall=float(row[3]),
                       aroma=float(row[4]),
                       appearance=float(row[5]),
                       profilename=row[6],
                       beer_style=row[7],
                       palate=float(row[8]),
                       taste=float(row[9]),
                       beer_name=row[10],
                       beer_abv=float(row[11]),
                       beer_id=int(row[12]))
