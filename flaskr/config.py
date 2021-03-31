from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request, Response
from sqlalchemy import Table, Column, Integer, ForeignKey, String, Float, DateTime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:senhatop#@localhost:5433/weather'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
