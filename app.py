from flask import Flask, redirect, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! ' + request.args.get('aaa', 'NOT WORKING')

@app.route('/redir')
def redir():
    return redirect('/foo', code=301)

@app.route('/foo')
def foo():
    return 'FOO'
