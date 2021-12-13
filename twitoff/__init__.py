from .app import create_app

# telling flask to use our create_app function (factory)
# now our app will be named "APP"
APP = create_app()