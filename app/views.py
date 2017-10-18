import json
import os
import requests

from flask import render_template, request
from flask import jsonify

from app import app
from .forms import searchForm

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])

def index():
    """
        Main view
    """
    # Variables to build the PAI request
    base_url = "https://content.googleapis.com/youtube/v3/search"
    query_string = ""
    api_key = "AIzaSyAI4AxAYqbf0VFaDAXfOeWt_MQstyi_p7I"
    call_format = "json"
    
    form = searchForm()

    # Submited?
    if form.validate_on_submit():
        query_string = form.query.data
    
    call_url = "{}?q={}&maxResults=25&part=snippet&key={}&alt={}".format(base_url, query_string, api_key, call_format)
    
    request =  requests.get(call_url)
    results = json.loads(request.text)
    results_list = json.dumps(results['items'])

    # os.system('stty sane')
    # import pdb; pdb.set_trace()
    if not query_string:
        query_string = "Last uploads"

    response = {}
    response['result_list'] = results_list
    response['total_items'] = results['pageInfo']['totalResults']
    response['page_items'] = results['pageInfo']['resultsPerPage']
    response['query'] = query_string

    return render_template('index.html',  page_title='Home', response=response, form=form)