from flask import Flask, request

app = Flask(__name__)

@app.route('/weather', methods=['GET', 'POST'])
def weather():
    temp = request.values.get('text')
    temp = int(temp)
    if temp > 30:
        return "It's so hot!"
    else:
        return f"The temperature is {temp}"
    
    
if __name__ == '__main__':
    app.run()

