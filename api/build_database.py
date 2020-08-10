import csv
from config import db
from models import Newborn

# Delete old db
db.drop_all()

# Create the database
db.create_all()

# Read csv
with open('babies-first-names-all-names-all-years.csv', 'r') as f:
    reader = csv.DictReader(f)
    for line in reader:
        newborn = Newborn(
            year=line["yr"],
            name=line["FirstForename"],
            number=line["number"],
            position=line["rank"]
        )
        # add to the db session
        db.session.add(newborn)

# Commit to db
db.session.commit()
