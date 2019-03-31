from flask import render_template, request, redirect, session, url_for, flash
from config import db 
from models import Users, Tweets

def index():
    #rendering the form
    return render_template('index.html')

def add_user():
    #import validations
    errors = User.validate(request.form)
    if errors:
        for error in errors:
            flash(error)
        return redirect(url_for('index'))
    user_id = User.add_user(request.form)
    session['user_id'] = user_id
    return redirect(url_for('success'))

#add log in route and function
def login():
####check to see if username exists in database####

####Add Query for users#####
    errors, warnings = User.login_assist(request.form)
    if not errors:
        flash(warnings)
        return redirect(url_for('index'))
    session['user_id'] = warnings
    return redirect(url_for('/success'))

def welcome():
    if 'user_name' not in session:
        return redirect(url_for('/'))
    ####Add new Query Here ####
    #my_tweets
    #mysql = connectToMySQL('baseRegis')
    #my_tweets = mysql.query_db('SELECT tweets.id, tweets, users.first_name, users.id, tweets.created_at FROM tweets LEFT JOIN users on tweets.user_id = users.id ORDER BY tweets.created_at DESC;')
    #print(my_tweets)
    #converting created_at to time....
    #session['tweets'] = my_tweets[0]['tweets']
    #sq_time = my_tweets[0]['created_at']
    #print(sq_time)
    #fmt = '%M-%D-%Y %H:&M:%s'
    #new_time = datetime.datetime.strftime(sq_time, fmt)
    #print(session)
    return render_template('success.html',
    name = session['user_name'])
    #,tweets = my_tweets )


def new_tweet():
    #adding validations
    if len(request.form['tweet']) < 1:
    #or len(request.form['tweet']) > 240:
        flash("Tweets must be between 1 and 240 characters long.")
        return redirect('/success')

    if not '_flashes' in session.keys():
        mysql = connectToMySQL('baseRegis')
        query = 'INSERT INTO tweets(user_id, tweets) VALUES (%(id)s, %(tw)s);'
        data = {
            'id': session['userid'],
            'tw': request.form['tweet']
            }
        new_tweet = mysql.query_db(query, data)
    return redirect('/success')

#creating likes for tweets

def add_like(tweet_id):
    print('*'*90)
    print(tweet_id)
    mysql = connectToMySQL('baseRegis')
    query = 'INSERT INTO likes(likes, user_id, tweet_id) VALUES (%(li)s, %(uid)s, %(tid)s);'
    data ={
        'li':  request.form['likes'],
        'uid': session['userid'],
        'tid': tweet_id
    }
    new_like = mysql.query_db(query,data)
    print('*'*90)
    print(new_like)
    return redirect('/success')

#deleting Tweets

def delete_tweet(tweet_id):
    mysql = connectToMySQL('baseRegis')
    #query = mysql.query_db(f'ALTER TABLE tweets DROP FOREIGN KEY users_id, ADD CONSTANT likes.id FOREIGN KEY {tweet_id} REFERENCES likes.id ON DELETE CASCADE')
    #query = mysql.query_db(f'DELETE FROM tweets LEFT JOIN likes on tweets.id = likes.tweet_id WHERE tweet_id = {tweet_id};')
    query = mysql.query_db(f'DELETE FROM likes WHERE tweet_id = {tweet_id}')
    mysql = connectToMySQL('baseRegis')
    query = mysql.query_db(f'DELETE FROM tweets WHERE id = {tweet_id}')
    print('*'*90)
    print('Tweet sucessfully deleted')
    return redirect('/success')

####edit tweets####

def edit_tweet(tweet_id):
    up_tweet = session['tweets']
    print('*'*90)
    print('rendering edit page')
    print(tweet_id, )
    return render_template('edit.html',
    name = session['user_name'],
    up_tweet = up_tweet)

#update tweets_id

def update_tweet(tweets_id):
    #adding validations
    if len(request.form['tweet']) < 1:
    #or len(request.form['tweet']) > 240:
        flash("Tweets must be between 1 and 240 characters long.")
        return render_template('edit.html')

    if not '_flashes' in session.keys():
        mysql = mysqlconnection('baseRegis')
        query = (f'INSERT tweets SET tweets = %(t)s, user_id = %(id)s WHERE id = %(tid)s')
        data = {
            't': request.form['tweets'],
            'id': session['userid'],
            'tid': tweets_id
        }
        db = connectToMySQL('baseRegis')
        db.query_db(query, data)
    return redirect('/success')

#printing users from the database

def show_users():
    #mysql = connectToMySQL('baseRegis')
    #users = mysql.query_db('SELECT first_name, last_name, email FROM users ORDER BY users.last_name')
    all_users = Users.query.all()
    print('*'*90)
    print('Printing users')
    print(all_users)
    return render_template('users.html',
    name = session['user_name'],
    users = all_users, )

####logout####
def logout():
    session.clear()
    return redirect(url_for('index'))
