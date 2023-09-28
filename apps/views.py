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

@app.route('/api-qa-presentation')
def qa_framework():
  return render_template('qa-framework.html', segment='qa-framework', parent='pages')

@app.route('/live-demo')
def live_demo():
  return render_template('live-demo.html', segment='live-demo', parent='pages')

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