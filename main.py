from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
             form {
                 background-color: #eee;
                 padding: 20px;
                 margin: 0 auto;
                 width: 540px;
                 font: 16px sans-serif;
                 border-radius: 10px;
             }
             textarea {
                 margin: 10px 0;
                 width: 540px;
                 heigth: 120px;
             }
        </style>
    </head>
    <body>
        <!-- create your form here -->
        <form action"/" method="post">
            <lable>
                Rotate by:
                <input type="text" name="rot" value="0" />
            </lable>
            <input type="text" name="message" />
            <input type="submit"/>
        </form>
    </body>
</html>
"""

@app.route("/", methods=['POST'])
def encrypt():
    rotation = request.form['rot']
    rotation = int(rotation)
    message = request.form['message']

    encrypted_text = rotate_string(message,rotation)
    
    return "<h1>" + encrypted_text + "</h1>"


@app.route("/")
def index():
    content = form
    
    return content

app.run()
