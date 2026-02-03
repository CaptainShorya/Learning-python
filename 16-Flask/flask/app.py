## Flask app Skeleton
from flask import Flask
'''
    Creates an instance of the Flask class.
    This instance represents the WSGI (Web Server Gateway Interface) application,
    which handles incoming HTTP requests and routes them to the appropriate
    view functions, acting as an interface between the web server and Flask based app.
'''

##WSGI Application 
app = Flask(__name__) ##__name__ is a special Python variable that identifies whether a file is run directly or imported, and Flask uses it to locate application resources."
'''
    *Each file gets its own __name__
    Possible values of __name__:
        1. "__main__" → When the Python file is executed directly.
        2. "module_name" → When the file is imported as a module.
'''

@app.route("/")
def welcome():
    return "Welcome to my landing page"

@app.route("/index")
def index():
    return "Welcome to index page"


if __name__ == "__main__": ## It is the entry point for any .py file , Execution starting point
    app.run(debug=True)
    ##debug=True -> Any time you are going to make changes over here, it is going to restart the server