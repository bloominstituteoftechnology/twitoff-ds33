from flask import Flask, render_template
from .models import DB, User, Tweet

# Create a "factory" for serving up the app when it is launched 
def create_app():

    #initializes our Flask app
    app = Flask(__name__)

    # configuration stuff
    app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

    # Connect our database to our app object
    DB.init_app(app)

    # Make our "Home" or "root" route
    @app.route('/')
    def root():
        users = User.query.all()
        # Do this when somebody hits the home page
        return render_template('base.html', users=users)

    # Test another route
    @app.route('/test')
    def test():
        # removes everything from the DB
        DB.drop_all()
        # creates a new DB with indicated tables
        DB.create_all()
        # Make some Users
        # create a user object from our .models class
        ryan = User(id=1, username='ryanallred')
        julian = User(id=2, username='julian')
        # add the user to the database
        DB.session.add(ryan)
        DB.session.add(julian)
        
        # Make some tweets
        # display our new user on the page
        # Make some tweets
        tweet1 = Tweet(id=1, text='this is some tweet text', user=ryan)
        tweet2 = Tweet(id=2, text='this is some other tweet text', user=julian)
        # add the tweets to the DB Session
        DB.session.add(tweet1)
        DB.session.add(tweet2)
        
        # save the database
        DB.session.commit()

        # query to get all users
        users = User.query.all()
        return render_template('base.html', users=users, title='test')




    return app