import random
from flask import Blueprint, render_template, url_for, redirect
from sqlalchemy.sql import func

from vocab_test.models import Word
from vocab_test.extensions import db

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def index():
    counts = []
    for n in range(5):
        counts.append(Word.query.filter(Word.confidence == n).count())
    return render_template('index.html', counts=counts)

@main.route('/word', methods=['GET', 'POST'])
@main.route('/word/<int:level>', methods=['GET', 'POST'])
@main.route('/word/<int:level>/<int:id>', methods=['GET', 'POST'])
def word(level=None, id=None):
    if id is not None:
        word = Word.query.filter(Word.id == id).first()
        return render_template('word.html', word=word)
        
    else:
        if level == None:
            res = db.session.query(func.max(Word.confidence).label("max_conf"), 
                        func.min(Word.confidence).label("min_conf"),
                        ).first()
        
            level = res.min_conf
        
        words = Word.query.filter(Word.confidence == level).all()
        word = random.choice(words)
        return redirect(url_for('.word', level=level, id=word.id))
    
    
    


@main.route('/set_confidence/<int:id>/<int:level>', methods=['GET', 'POST'])
def set_confidence(id, level):
    word = Word.query.filter(Word.id == id).first()
    base_level = word.confidence
    word.confidence = level
    db.session.commit()
    # print word
    
    return redirect(url_for('.word', level=base_level))