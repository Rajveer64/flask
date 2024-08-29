from flask import flask
app = flask(_name_)

@app.route('/')
def hello_world():
    return 'hello,world!'

if__name__ == '__main__':
    app.run(host='0.0.0.0',port=5000) 
