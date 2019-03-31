from config import db, bcrypt, func
import re

# create a regular expression object that we'll use later   copy
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PW_REGEX = re.compile('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$')

# Creating the database
# Creating the User db
class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(45), nullable = False)
    last_name = db.Column(db.String(45), nullable = False)
    email = db.Column(db.String(45), nullable = False)
    pw_hash = db.Column(db.String(255), nullable = False)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

def __repr__(self):
    return '<User %r>' % self.username

def __str__(self):
    return "<User: %s>" % self.username

@classmethod
def validate(cls, form):
    warnings = []
    fname_check = request.form['first_name'].isalpha()
    lname_check = request.form['last_name'].isalpha()

    if len(request.form['first_name']) < 1 and fname_check == False:
        warnings.append('* Please enter a valid first name.')
    if len(request.form['last_name']) < 1 and lname_check == False:
        warnings.append('* Please enter a valid last name.')

    if not EMAIL_REGEX.match(request.form['email']):
        warnings.append('* Please enter a valid email address.')

    if not PW_REGEX.match(request.form['password']):
        warnings.append('* Please enter a valid password: 6-20 characters, A-Z and (# $ % @ &)')
    if not len(request.form['password']) == len(request.form['pw_confirm']):
        warnings.append('passwords do not match')
    return warnings

####Add User Model####
@classmethod
def add_user(cls, form):
    pw_hash = bcrypt.generate_password_hash(form['password'])
    print(pw_hash)
####add new query here####
    new_user = cls(
    first_name = form['first_name'],
    last_name = form['last_name'],
    email = form['email'],
    pw_hash = pw_hash
    )
    db.session.add(new_user)
    db.session.commit()
#grab user id and name and add it to session
    session['user_name'] = request.form['first_name']
    return new_user.id

####login model####
@classmethod
def login_assist(cls, form):
    ####check to see if username exists in database####
    login_user = cls.query.filter_by(email = form['email']).first()
    ####add bcrypt hash####
    if len(request.form['email']) < 1:
        flash('* Please enter a valid email address.')
        return redirect('/')

    if login_user:
        if bcrypt.check_password_hash(login_user.pw_hash, form['password']):
            return (True, user.id)
         # if we get True after checking the password, we may put the user id in session
    return (False, "Email or password incorrect.")

@classmethod
def search(cls, form):
    pass


####tweets database####
class Tweets(db.Model):
    __tablename__ = "tweets"
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(240), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
#add a foriegn key and a relationship
    users = db.relationship('Users', foreign_keys=[user_id],
    backref=db.backref("tweets", cascade="all, delete-orphan"))
    #liked_by=db.relationship('User', secondary=likes_table, backref="liked_tweets")

#Likes Database

#followers database
