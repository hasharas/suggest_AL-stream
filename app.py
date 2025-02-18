from flask import Flask

print('Hello World!')
app = Flask(__name__)

@app.route('/')
def hello_world():
   return "Hello Wolds"

if __name__ == '_main_':
    app.run()