from config import app
from controller import index, add_user, login, welcome, new_tweet, add_like, delete_tweet, edit_tweet, update_tweet, show_users, logout

app.add_url_rule('/', view_func=index)
app.add_url_rule('/process', view_func=add_user, methods=['POST'])
app.add_url_rule('/login', view_func=login, methods=['POST'])
app.add_url_rule('/success', view_func=welcome)
app.add_url_rule('/tweets/create',view_func=new_tweet, methods=['POST'])
app.add_url_rule('/tweets/<tweet_id>/add_like', view_func=add_like, methods=['POST'])
app.add_url_rule('/tweets/<tweet_id>/delete', view_func=delete_tweet)
app.add_url_rule('/tweets/<tweet_id>/edit', view_func=edit_tweet)
app.add_url_rule('/tweets/<tweets_id>/update', view_func=update_tweet, methods=['POST'])
app.add_url_rule('/users', view_func=show_users)
app.add_url_rule('/logout', view_func=logout)
