from flask import Flask, request
import random
import json
import requests

app = Flask(__name__)

@app.route('/weather', methods=['GET', 'POST'])
def weather():
    temp = request.values.get('text')
    temp = int(temp)
    if temp > 30:
        return "Yeah nah nah yeah it's a tad hot outside I reckon"
    else:
        return f"She'll be right, it's only {temp}"

@app.route('/dice', methods=['GET', 'POST'])
def dice():
    numbers = [1,2,3,4,5,6] 
    human = random.choice(numbers)
    computer = random.choice(numbers)

    ## return f'Human: {human} \n Computer: {computer}'
    if human > computer:
        
        return f'Humans = {human} \n Computers = {computer} ... Humans win!'
    elif human < computer:
        return f'Humans = {human} \n Computers = {computer} ... Computers win!'
    elif human == computer:
        return f'Humans = {human} \n Computers = {computer} ... It is a tie!'

@app.route('/driftgif', methods={'GET', 'POST'})
def drift():
    url = "http://api.giphy.com/v1/gifs/search?q=drift&api_key=dc6zaTOxFJmzC&limit=3"
    response = requests.get(url)
    return f'{response.json()["data"][0]["images"]["original"]["url"]}'
      
    
if __name__ == '__main__':
    app.run(debug = True)

