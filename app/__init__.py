from flask import Flask
#from config import Config

myobj = Flask(__name__)
myobj.config.from_mapping(SECRET_KEY = 'hr738rgh3q2[qp[2dq//2dqjd9q8/2jd2dm2d')

from app import routes
