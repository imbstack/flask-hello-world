from flask import Flask, redirect
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/redir')
def redir():
    return redirect('/foo', code=301)

@app.route('/foo')
def foo():
    return 'FOO'
