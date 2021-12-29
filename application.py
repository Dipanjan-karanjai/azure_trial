from flask import Flask
app = Flask(__name__)

@app.route('/get_hello_world')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World'

if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()