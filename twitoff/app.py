from flask import Flask, render_template
from .models import DB, User, Tweet
from .twitter import add_or_update_user

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

    @app.route('/update')
    def update():
        users = User.query.all()
        usernames = [user.username for user in users]
        for username in usernames:
            add_or_update_user(username)
        return "updated"

    # Make our "Home" or "root" route
    @app.route('/populate')
    def populate():
        add_or_update_user('ryanallred')
        add_or_update_user('nasa')
        return '''Created some users. 
        <a href='/'>Go to Home</a>
        <a href='/reset'>Go to reset</a>
        <a href='/populate'>Go to populate</a>'''

    # Test another route
    @app.route('/reset')
    def test():
        # removes everything from the DB
        DB.drop_all()
        # creates a new DB with indicated tables
        DB.create_all()
        # Make some Users
        # create a user object from our .models class
        
        return '''The database has been reset. 
        <a href='/'>Go to Home</a>
        <a href='/reset'>Go to reset</a>
        <a href='/populate'>Go to populate</a>'''

    return app