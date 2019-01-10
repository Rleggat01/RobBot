from flask import Flask, request

app = Flask(__name__)

@app.route('/weather')
def weather():
    temp = request.values.get('text')
    temp = int(temp)
    if temp > 30:
        return "It's so hot!"
    else:
        return f"The temperature is {temp}"
    
    

app.run()