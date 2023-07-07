from app import app
from  flask import render_template
@app.route('/')
#decorators modifies the function that follows it
@app.route('/index')
def index():
    user = {'username': 'vincenttomi'}
    #creating fake posts
    posts = [
        {
        'author':{'username':'kennedy kawawa'},
        'body':'Beatiful day in Moringa!'
        },
        {
            
            'author':{'username':'Daniel Karanja'},
            'body':'The Avengers movie was so cool!'

        },
        { 
            
            'author':{'username':'Lilian Mwangi'},
            'body': 'Travelling is my hobby'
            
        },
        {
        'author':{'username':'simon mwanngi'},
        'body':'I love coding in python and Flask'
        },
        {
            'author':{'username':'korir'},
            'body':'you need a loving a girl to father'
        },
        {
            'author':{'username':'calvin'},
            'body':'you are a good frontend engineer Men'
        }
    ]
    return  render_template('index.html', title='Home', user=user,posts=posts)

