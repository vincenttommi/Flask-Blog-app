from app  import app

@app.route('/')
@app.route('/index')
#decorators that modifies a function that allows it
#decorators  register functions as callback for certain events
def index():
    
    #templates that inform of dict
    user = {"username":"vincenttommi"}
    return render_template('index.html', title='Home', user=user)
    
    


