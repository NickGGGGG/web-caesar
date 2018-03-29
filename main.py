from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {background-color: red;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <!-- create your form here -->
        <form action"/" method="post">
            <lable>
                Rotate by:
                <input type="text" name="rot" value="0" />
            </lable>
            <br>
            <textarea type="text" name="message">{0}</textarea>
            <br>
            <input type="submit"/>
        </form>
    </body>
</html>
"""
#<input type="text" name="message" />
@app.route("/", methods=['POST'])
def encrypt():
    rotation = request.form['rot']
    rotation = int(rotation)
    message = request.form['message']

    #global encrypted_text
    encrypted_text = rotate_string(message,rotation)
    
    return form.format(encrypted_text)


@app.route("/")
def index():
    
    encrypted_text = ''
    return form.format(encrypted_text)

app.run()
