from flask import Flask,render_template,request 
'''
 It creates an instance of the Flask class, 
 which will be your WSGI (Web Server Gateway Interface) application.
'''
###WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Welcome to the flask course</H1></html>"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

# Route to display the form
@app.route('/form',methods=['GET']) #Creates a route /form that accepts both GET HTTP requests.
def form():
    return render_template('form.html')

## name attribute(in HTML) → Used to send form data to backend

# Route to handle form submission
@app.route('/submit',methods=['POST']) #Creates a route /submit that accepts POST HTTP requests.
def submit():
    if request.method=='POST': ##request.method -> Responsible for catching request(whether it can be get,post,put,delete)
        name=request.form['Name']  #Retrieves the value entered in the form field named "Name".
        return f'Hello {name}!' 

if __name__=="__main__":
    app.run(debug=True)