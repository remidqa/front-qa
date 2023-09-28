# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Flask modules
from flask   import render_template, request, redirect
from jinja2  import TemplateNotFound
import requests

import os
from dotenv import load_dotenv
load_dotenv()

data_api_url=os.environ.get('DATA_API_INT_URL')

# App modules
from apps import app

# App main route + generic routing
@app.route('/', defaults={'path': 'index.html'})
@app.route('/')
def index():
  try:
    return render_template( 'hp.html', segment='analytics', parent='pages')
  except TemplateNotFound:
    return render_template('hp.html'), 404


# Pages 
@app.route('/dashboard')
def pages_dashboard():
  return render_template('dashboard.html', segment='dashboard', parent='pages')

@app.route('/resume')
def pages_resume():
  experiences_request=requests.get(f"{data_api_url}/experiences")
  experiences=experiences_request.json()
  return render_template('resume.html', segment='resume', parent='pages', experiences=experiences)

@app.route('/presentation-qa-framework')
def presentation_qa_framework():
  return render_template('presentation-qa-framework.html', segment='presentation-qa-framework', parent='pages')

@app.route('/live-demo')
def live_demo():
  return render_template('live-demo.html', segment='live-demo', parent='pages')

@app.route('/repository/api-qa/')
def api_qa():
  return render_template('repository/api-qa.html', segment='api-qa', parent='repository')

@app.route('/repository/front-qa/')
def front_qa():
  return render_template('repository/front-qa.html', segment='front-qa', parent='repository')

@app.route('/repository/cy-runner/')
def cy_runner():
  return render_template('repository/cy-runner.html', segment='cy-runner', parent='repository')

@app.route('/repository/newman-runner/')
def newman_runner():
  return render_template('repository/newman-runner.html', segment='newman-runner', parent='repository')

@app.route('/repository/data-api/')
def data_api():
  return render_template('repository/data-api.html', segment='data-api', parent='repository')

@app.route('/documentation/functional/')
def doc_functional():
  return render_template('documentation/functional.html', segment='functional', parent='documentation')

@app.route('/documentation/technical/')
def doc_technical():
  return render_template('documentation/technical.html', segment='technical', parent='documentation')


def get_segment( request ): 
  try:
    segment = request.path.split('/')[-1]
    if segment == '':
      segment = 'index'
    return segment    
  except:
    return None  

# Custom Filter
@app.template_filter('replace_value')
def replace_value(value, arg):
  return value.replace(arg, ' ').title()