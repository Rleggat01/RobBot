from flask import Flask, request

app = Flask(__name__)

@app.route('/weather', methods=['GET', 'POST'])
def weather():
    temp = request.values.get('text')
    temp = int(temp)
    if temp > 30:
        return "Yeah nah nah yeah it's a tad hot outside i reckon"
    else:
        return f"She'll be right, it's only {temp}"
    
    
if __name__ == '__main__':
    app.run(debug = True)

