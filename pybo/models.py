from pybo import db

# To apply the ManyToMany relationship,
# you must first create a table that means an N:N relationship through db.Table.
# question_voter is a table object having a user_id and a question_id as a pair.
question_voter = db.Table(
    'question_voter',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True),
    db.Column('question_id', db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'), primary_key=True),
)

answer_voter = db.Table(
    'answer_voter',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True),
    db.Column('answer_id', db.Integer, db.ForeignKey('answer.id', ondelete='CASCADE'), primary_key=True),
)


# how to use models
# 1. flask shell
# 2. https://wikidocs.net/81045
# 3. if you change the model:
#       --> flask db migrate
#       --> flask db upgrade

class Question(db.Model):
    # define properties
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)  # limited number of characters
    content = db.Column(db.Text(), nullable=False)  # no limit on the number of characters
    create_date = db.Column(db.DateTime(), nullable=False)  # date and time
    # ref: https://wikidocs.net/81059
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('question_set', cascade='all, delete-orphan'))
    modify_date = db.Column(db.DateTime(), nullable=True)
    # When the recommender is stored through the question model,
    # actual data is stored in the question_voter table,
    # and the stored recommender information can be referred to
    # through the voter attribute of the question model.
    voter = db.relationship('User', secondary=question_voter, backref=db.backref('question_voter_set'))


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'), nullable=False)
    question = db.relationship('Question', backref=db.backref('answer_set', cascade='all, delete-orphan'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('answer_set', cascade='all, delete-orphan'))
    modify_date = db.Column(db.DateTime(), nullable=True)
    voter = db.relationship('User', secondary=answer_voter, backref=db.backref('answer_voter_set'))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
