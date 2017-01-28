import requests
from flask import Flask, render_template, request, redirect
import pandas as pd
import quandl
from bokeh.plotting import figure, show, reset_output
from bokeh.charts import TimeSeries
from bokeh.palettes import Spectral11
from bokeh.embed import components 



quandl.ApiConfig.api_key = 'xx15tPCkmMzchc5HW3mp'

app = Flask(__name__)


TOOLS = "pan,wheel_zoom,box_zoom,reset"

numlines = 2
mypalette=Spectral11[0:numlines]

print('inside app')
@app.route("/")
def index():
  print('at /')
  return render_template("index.html")

@app.route("/about")
def about():
  return render_template("about.html")




if __name__ == "__main__":
 	app.run()
