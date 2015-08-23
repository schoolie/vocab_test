import csv

from vocab_test import create_app
from vocab_test.models import Word
from vocab_test.extensions import db


app = create_app()

with app.app_context():
    with open('words.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            print row[0], row[1]
            q = Word.query.filter(Word.word == row[0].decode('cp1252'))
            if q.count > 0:
                word = q.first()
                word.definition = row[1].decode('cp1252')
            else:
                word = Word(word=row[0].decode('cp1252'), definition=row[1].decode('cp1252'), confidence=0)
            db.session.add(word)
        db.session.commit()
