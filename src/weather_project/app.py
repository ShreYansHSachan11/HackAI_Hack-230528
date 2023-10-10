from uagents import Agent, Context, Model
from flask import Flask, render_template, request, session, redirect, url_for, flash
import subprocess
import os

app = Flask(__name__)

get_value = Agent(name="temp", seed = "temp recovery phrase")
@app.route("/")
def index():
    return render_template("index.html")

@app.route('/process_form', methods=['POST'])
def process_form():
    location = request.form.get('location')
    minTemp = request.form.get('minTemp')
    maxTemp = request.form.get('maxTemp')
    os.environ['LOCATION'] = location
    os.environ['MIN_TEMP'] = minTemp
    os.environ['MAX_TEMP'] = maxTemp
    result = subprocess.run(["python", "C:/Users/devan/uAgents/python/src/weather_project/temperature.py"])
    return redirect('/result.html')
    
    

@app.route('/result_page')
def result_page(ctx: Context):
     return "hello"

if __name__ == "__main__":
    app.run()
