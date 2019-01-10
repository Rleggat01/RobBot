
from flask import Flask, request

...

@app.route('/greet')
def greet_person():
    name = request.values.get('text')
    return f'hi {name}!'


app.run()