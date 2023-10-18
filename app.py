from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reviews.db'
db = SQLAlchemy(app)

CORS(app)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    comment = db.Column(db.String(500), nullable=False)
    stars = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Review('{self.name}', '{self.comment}', '{self.stars}', '{self.date}')"


@app.route('/', methods=['GET', 'POST'])
def reviews():
    if request.method == 'GET':
        reviews = Review.query.all()
        return ({'data':[{'name': review.name, 'comment': review.comment, 'stars': review.stars, 'date': review.date} for review in reviews]})
    elif request.method == 'POST':
        data = request.get_json()
        name = data['name']
        comment = data['comment']
        stars = data['stars']
        review = Review(name=name, comment=comment, stars=stars)
        db.session.add(review)
        db.session.commit()
        return ({'message': 'Review added to database successfully!'})
