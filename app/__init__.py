from flask import Flask
from config import  Config

app  = Flask(__name__)
#initilising our flask app  with its name
app.config.from_object(Config)



from app import routes

