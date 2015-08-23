from vocab_test import db

class Word(db.Model):
    __tablename__ = 'word'
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(50))
    definition = db.Column(db.String(140))
    confidence = db.Column(db.Integer)    
    
    def __repr__(self):
        return '%d: %s (%s)' % (self.confidence, self.word, self.definition)