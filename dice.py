from flask import Flask, request
import random
app = Flask(__name__)

@app.route('/dice')
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


if __name__ == '__main__':
      app.run(debug = True)