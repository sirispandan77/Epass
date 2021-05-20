from flask import Flask
from flask import render_template

app = Flask(__name__)

'''@app.route('/')
def hello_world():
    return 'Hello World!'
    '''


@app.route('/')
#@app.route('/templates')
def index():
    name = 'Rosalia'
    return render_template('index.html', title='Welcome', username=name)
   # return "hiji"

@app.route('/product/<name>')
def get_product(name=0):
  return "The product is " + str(name)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=4000)